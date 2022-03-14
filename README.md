Project Goal
---------------------

The ultimate objective is to determine the main drivers behind churn for our customers, and then to build a model that will predict  future customer churn in an effort to prevent the that future churn.



Project Description
-------------------

With the implimentaion of 5G networks across the country and the recent increase of people working from home, it is important now more than ever that we provide satisfation to our customers to retain their business.  Here we will analyze our current customer base (with a focus on those whose churned) and determine what were some of the key factors in their depature from Telco. Furthermore we can find out how likely those factors were to contribute to a customer churning, thus giving us an idea of what measure we can take to keep those at risk customers from churning.



Initial Questions
---------------------


- What customers are most important to prevent churning?

    How long are customers that churn staying with us?
    What's their lifetime charges (total charges)?
    How do their total charges differ from those that did not churn?


- What were the services that those higher value accounts looked for, and do they differ from their lower value counterparts?

    These will more than likely be good indicators for churn

- Will the customers household be a good indicator of churn? (Married, senior, children)








Data Dictionary
---------------------

Features

    churn
    tenure
    monthly_charges
    total_charges
    is_male
    married
    senior_citizen
    children
    phone_service
    multiple_lines
    online_security
    online_backup
    device_protection
    tech_support
    streaming_tv
    streaming_movies
    paperless_billing
    one_year_contract
    two_year_contract
    fiber_optic
    no_internet
    card_auto_pay
    electronic_check
    mailed_check

Dataframes

    df = The main dataframe we will work with
    telco_df = An unprepped copy of the original dataframe
    df_customer_id = A prepped copy of the original df, used to create our prediction CSV
    train = A sample of df, used to practice on different models
    validate = A sample of df, used to verify on different models
    test = A sample of df, ONLY USED ON BEST FITTING MODEL

