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
    Takes in the telco df and cleans the dataframe up for use. Also changes total_charges from type(obj) to type(float) and removes any accounts with a tenure of 0 to keep information relevant
    '''
    
    df = df.drop(columns=['payment_type_id', 'internet_service_type_id', 'contract_type_id'])
    df.total_charges = df.total_charges.replace(' ', 0).astype(float)
    df = df[df.tenure != 0]

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


# other useful functions for metrics



def get_metrics(tp, fn, fp, tn):
    '''
    This function takes the True Positive, False Negative, False Positive, and True Negatives from a confusion matrix and uses them to give us the metrics of the model used for the matrix.
    '''
    
    accuracy = (tp + tn) / (tp + tn + fp + fn)
    recall = tp / (tp + fn)
    precision = tp / (tp + fp)
    f1_score = (2 * (precision * recall) / (precision + recall))
    true_pos = recall
    true_neg = tn / (tn + fp)
    false_pos = fp / (tn + fp)
    false_neg = fn / (tp + fn)
    support_pos = tp + fn
    support_neg = tn + fp

    print(f'Accuracy: {accuracy: .2%}')
    print(f'---------------')
    print(f'Recall: {recall: .2%}')
    print(f'---------------')
    print(f'Precision: {precision: .2%}')
    print(f'---------------')
    print(f'F1 Score: {f1_score: .2%}')
    print(f'---------------')
    print(f'True Positive Rate: {true_pos: .2%}')
    print(f'---------------')
    print(f'True Negative Rate: {true_neg: .2%}')
    print(f'---------------')
    print(f'False Positive Rate: {false_pos: .2%}')
    print(f'---------------')
    print(f'False Negative Rate: {false_neg: .2%}')
    print(f'---------------')
    print(f'Support (Did Not Survive(0)): {support_pos}')
    print(f'---------------')
    print(f'Support (Survived(1)): {support_neg}')