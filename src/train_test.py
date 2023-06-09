from sklearn.model_selection import train_test_split
import pandas as pd
from sklearn.compose import ColumnTransformer, make_column_transformer
from sklearn.pipeline import Pipeline, make_pipeline
from sklearn.preprocessing import OneHotEncoder, OrdinalEncoder, StandardScaler

state = 123

# ' Split the dataset into X, y training and testing sets.
# '
# ' @param df: The original dataframe.
# '
# ' @return Return X, y training and testing sets.
def split(df):
    train_df, test_df = train_test_split(df, test_size=0.3, random_state=state)
    X_train = train_df.drop(columns=["Smog Rating", 
                                     "Engine Size(L)",
                                     "CO2 Emissions(g/km)",
                                     "Fuel Consumption (City (L/100 km)",
                                     "Fuel Consumption(Hwy (L/100 km))",
                                     "Fuel Consumption(Comb (L/100 km))",
                                     "Fuel Consumption(Comb (mpg))",
                                     "Log Fuel Consumption(Comb (L/100 km))"
                                    ])
    X_test = test_df.drop(columns=["Smog Rating", 
                                   "Engine Size(L)",
                                   "CO2 Emissions(g/km)",
                                   "Fuel Consumption (City (L/100 km)",
                                   "Fuel Consumption(Hwy (L/100 km))",
                                   "Fuel Consumption(Comb (L/100 km))",
                                   "Fuel Consumption(Comb (mpg))",
                                   "Log Fuel Consumption(Comb (L/100 km))"
                                  ])
    y_train = train_df["Smog Rating"]
    y_test = test_df["Smog Rating"]

    return X_train, X_test, y_train, y_test