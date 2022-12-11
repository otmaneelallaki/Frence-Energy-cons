import pandas as pd
import numpy as np
import datetime as dt
import xgboost as xgb
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm
from fec.src.xgboost import path_target


sns.set()


class Dos():
    """ 
    Class Dos is  a class that could daily predect and plot three sources 
    of three sources of enrergy: Electricity Consumption, Gaz and Nuclear.

    
    :param data: This is the data training, it is the output of :ref:`Data Collection <DataCol>`.
    :type data: Dataframe

    :param energy: This model predict three sources of energy: Electricity Consumption, Gaz and Nuclear.
            0 : Electricity Consumption
            1 : Gaz
            2: Nuclear
    :type energy: int

    :param Year: The Year for which day we want to predict.
    :type Year: int

    :param month: The month for which day we want to predict.
    :type month: int
    
    :param day: The day for which day we want to predict.
    :type day: int
    """
    def __init__(self, data, energy, year, month, day):
        self.data = data
        self.energie = energy
        self.year = year
        self.month = month
        self.day = day
        self.xgboost = xgb.XGBRegressor(base_score=0.5,
                               booster='gbtree',
                               n_estimators=500,
                               objective='reg:linear',
                               max_depth=3,
                               learning_rate=0.01)

        
    def fitModel(self):
        """
        This method is for the trining model part and saving it as tst file.

        .. Note::
            it takes about 1 minute to execute, it is recommended to use it once a year 
            (whenever you see that's the forecasting is no longer gives a good result).
            Then use **louad_mod()** method instead.
        """
        target = self.data.columns[self.energie]
        target_map = self.data[target].to_dict()
        self.data = self.data.copy()
        ind = self.data.index
        self.data['minute'] = ind.minute
        self.data['dayofweek'] = ind.dayofweek
        self.data['month'] = ind.month
        self.data['year'] = ind.year
        self.data['dayofyear'] = ind.dayofyear
        self.data['dayofmonth'] = ind.day
        self.data['lag1'] = (ind - pd.Timedelta('364 days')).map(target_map)
        self.data['lag2'] = (ind - pd.Timedelta('30 days')).map(target_map)
        self.data['lag3'] = (ind - pd.Timedelta('7 days')).map(target_map)

        target = self.data.columns[self.energie]
        FEATURES = ['dayofyear', 'minute', 'dayofweek', 'month', 'year',
                    'lag1', 'lag2', 'lag3']
        TARGET = target
        X_all = self.data[FEATURES]
        y_all = self.data[TARGET]
        self.xgboost.fit(X_all, y_all,
                eval_set=[(X_all, y_all)],
                verbose=100)
        self.xgboost.save_model(path_target)

        return self.xgboost

    def louad_mod(self):
        """ After the model was saved by calling **fitModel()** method, you have just call this method to relouad it again."""
        self.xgboost.load_model(path_target)
                
    def DayPred(self):
        """
        This method return to a DataFrame contains the date and hour of the day that we eant to forecast.

        :return: day_pred
        :rtype: DataFrame  

        :return: DayDate 
        :rtype: DataFrame
        """
        liste = []
        for i in range(96):
            liste.append(str(dt.datetime(self.year, self.month,
                         self.day, 0, 0) + dt.timedelta(minutes=(i)*15)))
        DayDate = pd.to_datetime(np.array(liste))

        dayFeaturs = pd.DataFrame()
        dayFeaturs['dayofyear'] = DayDate.dayofyear
        dayFeaturs['minute'] = DayDate.minute
        dayFeaturs['dayofweek'] = DayDate.dayofweek
        dayFeaturs['month'] = DayDate.month
        dayFeaturs['year'] = DayDate.year

        target = self.data.columns[self.energie]
        target_map = self.data[target].to_dict()
        dayFeaturs['lag1'] = (
            DayDate - pd.Timedelta('364 days')).map(target_map)
        dayFeaturs['lag2'] = (
            DayDate - pd.Timedelta('30 days')).map(target_map)
        dayFeaturs['lag3'] = (DayDate - pd.Timedelta('7 days')).map(target_map)

        pred = self.xgboost.predict(dayFeaturs)
        Date = DayDate.strftime('%Y-%m-%d')
        Hour = DayDate.strftime('%H:%M')
        day_pred = pd.DataFrame()
        day_pred["Date"] = Date
        day_pred["Heure"] = Hour
        day_pred[target] = pred

        return day_pred, DayDate

    def plot(self, day_pred, DayDate):
        """ This method plot daily energy predection indexing by Time 

        :param day_pred: the out put of the **DayPred()** method
        :type day_pred: DataFrame

        :param DayDate: the out put of the **DayPred()** method
        :type DayDate: DataFrame
        """

        target = self.data.columns[self.energie]

        day_pred = day_pred[target].values
        day_pred = pd.DataFrame(day_pred, index=DayDate,
                                columns=['{}'.format(target)])
        f, ax = plt.subplots(figsize=(12, 6), dpi=200)
        plt.suptitle('{}-{}-{}, forecasting {}'.format(self.year,
                     self.month, self.day, target), fontsize=24)
        day_pred.plot(ax=ax, rot=90, ylabel='MW', legend="Predicted day ")
        plt.show()
