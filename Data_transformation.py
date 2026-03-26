import pandas as pd
import numpy as np
from sqlalchemy import create_engine
path_file="C:/Users/Purche Lorenz/Documents/flats_data.csv"
def load_data():
    df=pd.read_csv(path_file, sep=',', engine='python', quotechar='"',
                     encoding="latin1", on_bad_lines="skip")
    return  df
def clean_square_feet(df):
    df['clean_square_feet'] = df['square_feet'].str.extract(r'(\d+)', expand=False)
    df['clean_square_feet'] = pd.to_numeric(df['clean_square_feet'], errors='coerce')
    return df

def clean_price_data(df):

    df['clean_price'] = df['price'].str.extract(r'(\d+\.\d+|\d+)', expand=False)
    df['clean_price'] = pd.to_numeric(df['clean_price'], errors='coerce')
    df['unit_price'] = df['price'].str.extract(r'([a-zA-Z]+)', expand=False).str.lower()

    # add multiplier column, establishing the values according to unit_price
    df['multiplier'] = np.nan
    df.loc[df['unit_price'] == 'cr', 'multiplier'] = 1
    df.loc[df['unit_price'] == 'lac', 'multiplier'] = 0.01
    df.loc[df['unit_price'] == 'call', 'multiplier'] = np.nan

    # normalize prices---convert to one unit price. All prices will be translated to CR.
    df['price_to_cr'] = df['clean_price'] * df['multiplier']

    # obtain the absolute price which is the price expressed as as full numeric value-Cr=10.000.000
    df['price_absolute'] = df['price_to_cr'] * 10000000
    df['price_per_sqft_cleaned'] = round(df['price_absolute'] / df['clean_square_feet'], 2)

    return df

def create_final_dataset(df):
    df_final = df.loc[:,
               ['property_name', 'clean_square_feet', 'price_per_sqft_cleaned', 'price_to_cr', 'price_absolute',
                'status', 'facing']]
    return df_final

df=load_data()
df=clean_square_feet(df)
df=clean_price_data(df)
df_final=create_final_dataset(df)

#load data in a database(MySQL)
engine=create_engine("mysql+pymysql://root:12345@localhost/project_pipeline")
df_final.to_sql("clean_flats_data",engine, if_exists='replace',index=False)