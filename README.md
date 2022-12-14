# Welcome to fecdv
This package was made as a project in the software devlopment course.
## Introduction : 
This project aims to : <br/>

-Create  a python package allowing any user to predict for a desired day different sources of energy consumption in France. <br/>

### Usage

- Just install the package `pip install fecdv`
- Import it to you project `import fec` and use as you want😊

### Install

```
    pip install fecdv
````

### Example

## Once you install `fecdv` use this code below to gain time after. 
```
    import fec
    df = fec.Load().save_as_df()
    model = fec.Dos(df, 0, 2022, 12, 12)
    model.fitModel()
    pred, date = model.DayPred()
```
## OUTPUT
```
    Date	Heure	Consommation (MW)
    0	2022-12-12	00:00	61938.777344
    1	2022-12-12	00:15	61938.777344
    2	2022-12-12	00:30	61279.824219
    3	2022-12-12	00:45	59455.636719
    4	2022-12-12	01:00	58968.359375
    ... 	   ... 	  ...	         ...
    91	2022-12-12	22:45	65976.734375
    92	2022-12-12	23:00	65245.457031
    93	2022-12-12	23:15	65245.457031
    94	2022-12-12	23:30	64151.945312
    95	2022-12-12	23:45	64159.773438
```
## This code below do the same work as the above with less time. <br/>
Note : At first time it is necessary to run the code above to save data and the model fitting 

```
    import fec
    df = fec.Load().save_as_df()
    model = fec.Dos(df, 0, 2022, 12, 20)
    model.louad_mod()
    pred, date = model.DayPred()
```
## OUTPUT
```
        Date	Heure	Consommation (MW)
    0	2022-12-20	00:00	67157.078125
    1	2022-12-20	00:15	67157.078125
    2	2022-12-20	00:30	67020.390625
    3	2022-12-20	00:45	66242.390625
    4	2022-12-20	01:00	65936.226562
    ...        ...	  ...	         ...
    91	2022-12-20	22:45	67696.882812
    92	2022-12-20	23:00	68242.476562
    93	2022-12-20	23:15	68242.476562
    94	2022-12-20	23:30	67696.882812
    95	2022-12-20	23:45	67696.882812
  ```

