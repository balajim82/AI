import mysql.connector
import pandas as pd
from sqlalchemy import create_engine, text


def get_rdbms_connection():
    try:
        # conn = mysql.connector.connect(
        #     host="localhost",
        #     user="root",
        #     password="Balu456$$",
        #     database="WASDE_REPORT_DB",
        # )
        conn = create_engine("mysql+pymysql://root:Balu456$$@localhost/WASDE_REPORT_DB")
        print("data connection Suceessfully Created ")
    except Exception as e:
        print("[RDBMS] failed to connect to DB:", e)
    return conn


def insert_data(df: pd.DataFrame):
    try:
        conn = get_rdbms_connection()
        # cursor = conn.cursor()
        # insert_query = """
        # INSERT INTO WASDE_REPORT (commodity, country, wr_description)
        # VALUES (%s, %s, %s)
        # """
        # # Convert DataFrame → List of tuples
        # data = [
        #     (row["commodity"], row["country"], row["wr_description"])
        #     for _, row in df.iterrows()
        # ]
        # cursor.executemany(insert_query, data)
        # conn.commit()
        # print(f"{cursor.rowcount} records inserted successfully!")
        with conn.begin() as conn:
            conn.execute(
                text(
                    """
                    INSERT INTO WASDE_REPORT (commodity, country, wr_description)
                    VALUES (:commodity, :country, :wr_description)
                    """
                ),
                [
                    {
                        "commodity": row["commodity"],
                        "country": row["country"],
                        "wr_description": row["wr_description"],
                    }
                    for _, row in df.iterrows()
                ],
            )
    except Exception as e:
        print("Error:", e)
    # finally:
    #     # cursor.close()
    #     # conn.close()


def retrive_data():
    try:
        conn = get_rdbms_connection()
        query = "SELECT * FROM WASDE_REPORT"
        df = pd.read_sql(query, conn.connect())
        # conn.close()
    except Exception as e:
        print("[RDBMS] failed to retrive data:", e)
    return df
