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
    
    df = df.drop(columns=['payment_type_id', 'internet_service_type_id', 'contract_type_id'])
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


