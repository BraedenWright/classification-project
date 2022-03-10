import env
import numpy as np
import pandas as pd
import acquire_telco as aq
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split

# telco dataframe

def prep_telco(df):
    '''
    takes in the telco df and cleans the dataframe up for use. also changes total_charges from type(obj) to type(float)
    '''
    
    df = df.drop(columns=['customer_id', 'payment_type_id', 'internet_service_type_id', 'contract_type_id'])
    df.total_charges = df.total_charges.replace(' ', 0).astype(float)

    cat_columns = ['gender', 'partner', 'dependents', 'phone_service', 'multiple_lines', 'online_security', 'online_backup', 'device_protection', 'tech_support', 'streaming_tv', 'streaming_movies', 'paperless_billing', 'churn', 'contract_type', 'internet_service_type', 'payment_type']

    for col in cat_columns:
        telco_dummy = pd.get_dummies(df[col],
                                     prefix=df[col].name,
                                     dummy_na=False,
                                     drop_first = True)
        df = pd.concat([df, telco_dummy], axis=1)
        df = df.drop(columns=[col])
    
    return df



# function to split our data


def train_validate_test_split(df):
    ''' 
    This function takes in a dataframe and splits it 80:20.  The 20% will be our testing datafrme for our final model.  The 80% will be split a second time (70:30), creating our final training dataframe and a dataframe to validate our model with before testing.  Leaving us we a Train (56%), Validate(24%) and Test (20%) Dataframe from our original data (100%)
    '''
    
    train, test = train_test_split(df, 
                               train_size = 0.8,
                               random_state=1313)
    
    train, validate = train_test_split(train,
                                  train_size = 0.7,
                                  random_state=1313)
    
    return train, validate, test
