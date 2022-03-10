import pandas as pd
import seaborn as sns
import env
import os

# Aquire.py Exercises/Function Setup


# Exercise 1 -- get_titanic_data

def get_titanic_data():

    filename = 'titanic_df.csv'
    
    if os.path.exists(filename):
        print('Reading from csv file...')
        return pd.read_csv(filename)

    database = 'titanic_db'
    url = f'mysql+pymysql://{env.user}:{env.password}@{env.host}/{database}'
    query = '''SELECT * FROM passengers'''

    df = pd.read_sql(query, url)
    df.to_csv(filename, index=False)

    return df

get_titanic_data()

# Exercise 2 -- get_iris_data

def get_iris_data():

    filename = 'iris_df.csv'
    
    if os.path.exists(filename):
        print('Reading from csv file...')
        return pd.read_csv(filename)

    database = 'iris_db'
    url = f'mysql+pymysql://{env.user}:{env.password}@{env.host}/{database}'
    
    query = '''
            SELECT 
                species_id,
                species_name, 
                sepal_length, 
                sepal_width,
                petal_length,
                petal_width
            FROM measurements
            JOIN species USING(species_id)
            '''

    df = pd.read_sql(query, url)
    df.to_csv(filename, index=False)

    return df



# Exercise 3 -- get_telco_data

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