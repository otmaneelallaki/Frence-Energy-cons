# Welcome to fecdv

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
...	...	...	...
91	2022-12-12	22:45	65976.734375
92	2022-12-12	23:00	65245.457031
93	2022-12-12	23:15	65245.457031
94	2022-12-12	23:30	64151.945312
95	2022-12-12	23:45	64159.773438
```
## Once you install `fecdv` use this code below to gain time after. 

