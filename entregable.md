# Roberto Alvarado
El github se encuentra en
https://github.com/Robdres/TrabajoAcademicoFinal

## El dataset inicial se encuentra en kaggle

https://www.kaggle.com/datasets/zahidmughal2343/global-cancer-patients-2015-2024

## Pero de manera local esta en
-CSV: [global\_cancer\_patients\_2015\_2024.csv](./data/global_cancer_patients_2015_2024.csv)
-SQL: [./data/global-cancer-patients.db](./data/global_cancer_patients.db)
## El script para crear el database es

```
sqlite3 cancer.db
sqlite3> .mode csv
sqlite3> .import global\_cancer\_patients\_2015\_2024.csv
sqlite3> .exit
```
## El notebook con los graficos estan en

-NOTEBOOK: [./data/main.ipynb](./data/main.ipynb)

## El dataset final esta dentro del notebook
