from sqlalchemy import create_engine
import pymysql
import pandas as pd

from google_news_headlines import GoogleNewsHeadlines
import secret_variables


def lambda_handler(event, context):
    dataFrame   = GoogleNewsHeadlines().pandas_dataframe()
    engine = create_engine(
        secret_variables.url, 
        pool_recycle=3600)
    con = engine.connect()

    try:
        dataFrame.to_sql(name='headlines',con=con,if_exists='append', index=False)
    except ValueError as vx:
        print(vx)
    except Exception as ex:   
        print(ex)
    else:
        print('''
Table 'headlines' in the 'google' database has updated successfully.
''')
    finally:
        con.close()
