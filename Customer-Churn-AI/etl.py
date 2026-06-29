import pandas as pd
import pyodbc


# 1- Extract

df = pd.read_csv(
    "WA_Fn-UseC_-Telco-Customer-Churn.csv"
)


print(df.head())

#transform

df['TotalCharges'] = pd.to_numeric(
    df['TotalCharges'],
    errors='coerce'
)



df.dropna(inplace=True)


print(df.info())

#load

conn = pyodbc.connect(
    "Driver={SQL Server};"
    "Server=localhost;"
    "Database=ChurnDB;"
    "Trusted_Connection=yes;"
)


cursor = conn.cursor()


for index, row in df.iterrows():

    cursor.execute(
        """
        INSERT INTO Customers
        VALUES (?,?,?,?,?,?,?,?,?,?)
        """,
        row.customerID,
        row.gender,
        row.SeniorCitizen,
        row.Partner,
        row.Dependents,
        row.tenure,
        row.PhoneService,
        row.MonthlyCharges,
        row.TotalCharges,
        row.Churn
    )


conn.commit()


cursor.close()
conn.close()


print("ETL Completed")