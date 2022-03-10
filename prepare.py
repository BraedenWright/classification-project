import env
import numpy as np
import pandas as pd
import acquire as aq
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split

# telco dataframe

def prep_telco(telco_df):
    '''
    takes in the telco_df and cleans the dataframe up for use. also changes total_charges from type(obj) to type(float)
    '''
    
    telco_df = telco_df.drop(columns=['payment_type_id', 'internet_service_type_id', 'contract_type_id'])
    telco_df.total_charges = telco_df.total_charges.replace(' ', 0).astype(float)

    cat_columns = ['gender', 'partner', 'dependents', 'phone_service', 'multiple_lines', 'online_security', 'online_backup', 'device_protection', 'tech_support', 'streaming_tv', 'streaming_movies', 'paperless_billing', 'churn', 'contract_type', 'internet_service_type', 'payment_type']

    for col in cat_columns:
        telco_dummy = pd.get_dummies(telco_df[col],
                                     prefix=telco_df[col].name,
                                     dummy_na=False,
                                     drop_first = True)
        telco_df = pd.concat([telco_df, telco_dummy], axis=1)
        telco_df = telco_df.drop(columns=[col])
    
    return telco_df

# titanic dataframe

def prep_titanic(titanic_df):
    '''
    takes in the titanic_df and cleans up the data and encodes it
    '''
    titanic_df = titanic_df.drop(columns=['deck', 'embarked', 'class', 'age', 'passenger_id'])
    titanic_df = titanic_df.rename(columns={'pclass':'passenger_class'})
    titanic_df['embark_town'] = titanic_df.embark_town.fillna('Southampton')
    titanic_dummy = pd.get_dummies(titanic_df[['sex', 'embark_town']],
                          dummy_na=False,
                         drop_first = [True, True])
    titanic_df = pd.concat([titanic_df, titanic_dummy], axis=1)
    
    return titanic_df


# iris dataframe

def prep_iris(iris_df):
    '''
    takes in the iris_df and cleans it by removing species_id,
    renaming certain columns and setting up dummies for species type
    '''
    
    iris_df = iris_df.drop(columns=['species_id'])
    iris_df = iris_df.rename(columns={'species_name':'species'})
    iris_dummy = pd.get_dummies(iris_df['species'], dummy_na=False, drop_first=True)
    iris_df = pd.concat([iris_df, iris_dummy], axis=1)
    
    return iris_df


