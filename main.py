"""
FINANCIAL MODELING OF INSURANCE COMPANY (AUTO INSURANCE) USING MONTE CARLO SIMULATION
AUTHORS
ANTARA CHANSARKAR
SAKET NAIK
SPARSH SADAFAL
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from random import randint
import warnings

warnings.filterwarnings("ignore")


def dict_generator():
    """
    This function generates a list of dictionary with key as the bucket of that variable and value as its
    relativity
    :return: List of dictionaries
    """
    age = {"18-24 years": 1.2, "25-45 years": 1, "45-60 years": 1.15,
           "60+ years": 1.25}
    driving_hist_dui = {"No": 1, "Yes": 1.2}
    driving_hist_reckless = {"No": 1, "Yes": 1.1}
    driving_hist_speeding = {"No": 1, "Yes": 1.05}
    credit_score = {"300-579": 1.2, "580-669": 1.1, "670-739": 1,
                    "740-799": 0.95, "800-850": 0.88}
    driving_exp = {"less than 1 year": 1.1, "1-5 years": 1.05,
                   "6-15 years": 1, "15+ years": 0.97}
    location = {"Urban": 1.05, "Rural": 0.97, "Suburban": 1}
    insurance_hist = {"No coverage": 1.2, "Coverage (past 6 months)": 1.05,
                      "Coverage (past 1 year)": 1.05, "Coverage (past 6 months)": 1.05}
    annual_mileage = {"0-7500 miles": 1, "7500-10000 miles": 1.1,
                      "10001-15000 miles": 1.15, "15000+ miles": 1.2}
    marital_status = {"Married": 0.95, "Single/Divorced/Widowed": 1}
    claims_hist = {"Filed within last 1 year": 1.25, "Filed within last 1-3 years": 1.15,
                   "No claims filed": 1}
    coverage_level = {"10-20k": 0.94, "20k-30k": 0.97, "30k-40k": 1, "40k-50k": 1.05,
                      "50-60k": 1.09, "60k-70k": 1.12, "70k-80k": 1.15, "80k-90k": 1.18,
                      "90k-100k": 1.22, "100k-110k": 1.25, "110-120k": 1.28, "120k-130k": 1.32,
                      "130k-140k": 1.35, "140k-150k": 1.38}
    deductible = {"No deductible": 1.2, "$250": 1, "$500": 0.9, "$1000": 0.8}
    vehicle_safety = {"0 NCAP": 1.15, "1 NCAP": 1.1, "2 NCAP": 1.05, "3 NCAP": 1,
                      "4 NCAP": 0.95, "5 NCAP": 0.9}
    information_list = list([age, driving_hist_dui, driving_hist_reckless, driving_hist_speeding, credit_score,
                             driving_exp, location, insurance_hist, annual_mileage, marital_status, claims_hist,
                             coverage_level, deductible, vehicle_safety]
                            )
    return information_list


def create_df(number_of_customers):
    """
    Creates a dataframe with values of all the variables being considered for the auto insurance financial model
    :return: dataframe with relativity of all the variables
    """
    column_names = ['Age', 'Driving_History_DUI', 'Driving_History_reckless', 'Driving_History_speeding' 'Credit_Score',
                    'Years_of_Driving', 'Location', 'Insurance_History', 'Annual_Mileage', 'Marital_Status',
                    'Claims_History', 'Coverage_level', 'Deductible', 'Vehicle']
    fm_dataframe = pd.DataFrame(columns=column_names)
    for i in range(0, number_of_customers):
        data = []
        for info_dict in dict_generator():
            x = np.random.randint(0, len(info_dict))
            value = list(info_dict.values())[x]
            data.append(value)
        fm_dataframe = fm_dataframe.append(
            {"Age": data[0], "Driving_History_DUI": data[1], "Driving_History_reckless": data[2],
             "Driving_History_speeding": data[3], "Credit_Score": data[4],
             "Years_of_Driving": data[5], "Location": data[6], "Insurance_History": data[7],
             "Annual_Mileage": data[8], "Marital_Status": data[9],
             "Claims_History": data[10], "Coverage_level": data[11], "Deductible": data[12],
             "Vehicle": data[13]}, ignore_index=True)
    calculate_premium(fm_dataframe)


def calculate_premium(dataframe, n):
    """
    This function returns the total insurance premium of n customers based on their relativity of each variable that
    we have considered
    :param df:
    :param dataframe: dataframe with relativities of all the factors affecting insurance premium
    :param n: No. of customers
    :return: total insurance premium
    """
    baseline_premium = 1600
    df['Calculated_premium'] = baseline_premium*df['Age']*df['Driving_History_DUI']*df['Driving_History_reckless']*\
                               df['Driving_History_speeding']*df['Credit_Score']*df['Years_of_Driving']*df['Location']*\
                               df['Insurance_History']*df['Annual_Mileage']*df['Marital_Status']*df['Claims_History']*\
                               df['Coverage_level']*df['Deductible']*df['Vehicle']
    print(df['Calculated_premium'].mean())
    return df


if __name__ == '__main__':
    df = create_df(1000)
    print(df.describe())
