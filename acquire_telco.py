import pandas as pd
import seaborn as sns
import env
import os

# Aquire.py Exercises/Function Setup


# Exercise  -- get_telco_data

def get_telco_data():

    filename = 'telco.csv'
    
    if os.path.exists(filename):
        print('Reading from csv file...')
        return pd.read_csv(filename)

    database = 'telco_churn'
    url = f'mysql+pymysql://{env.user}:{env.password}@{env.host}/{database}'
     
    query = '''
            SELECT * 
            FROM customers
            JOIN contract_types USING(contract_type_id)
            JOIN internet_service_types USING(internet_service_type_id)
            JOIN payment_types USING(payment_type_id)
            '''
     
    df = pd.read_sql(query, url)
    df.to_csv(filename, index=False)

    return df


# Exercise 4 -- caching (done)