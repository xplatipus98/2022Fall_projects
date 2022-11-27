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
import random

def dict_generator():
    """

    :return:
    """
    age = {"18-24 years": 1.5, "25-45 years": 1, "45-60 years": 1.3,
           "60+ years": 1.6}
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
    claims_hist = {"Filed within last 1 year": 1.3, "Filed within last 1-3 years": 1.2,
                   "No claims filed": 1}
    coverage_level = {"10-20k": 0.9, "20k-30k": 0.95, "30k-40k": 1, "40k-50k": 1.05,
                      "50-60k": 1.1, "60k-70k": 1.15, "70k-80k": 1.2, "80k-90k": 1.25,
                      "90k-100k": 1.3, "100k-110k": 1.35, "110-120k": 1.4, "120k-130k":1.45,
                      "130k-140k": 1.5, "140k-150k": 1.55}
    deductible = {"No deductible": 1.2, "$250": 1, "$500": 0.9, "$1000": 0.8}
    vehicle_safety = {"0 NCAP": 1.15, "1 NCAP": 1.1, "2 NCAP": 1.05, "3 NCAP": 1,
                      "4 NCAP": 0.95, "5 NCAP": 0.9}
    information_list = list([age, driving_hist_dui, driving_hist_reckless, driving_hist_speeding, credit_score,
                            driving_exp, location, insurance_hist, annual_mileage, marital_status, claims_hist,
                            coverage_level, deductible, vehicle_safety]
                            )
    return information_list


def create_df():
    """
    Creates a dataframe with values of all the variables being considered for the auto insurance financial model
    :return: dataframe with relativity of all the variables
    """
    data = []
    column_names = ['Age', 'Driving_History_DUI', 'Driving_History_reckless', 'Driving_History_speeding' 'Credit_Score',
                    'Years_of_Driving', 'Location', 'Insurance_History', 'Annual_Mileage', 'Marital_Status',
                    'Claims_History', 'Coverage_level', 'Deductible', 'Vehicle']
    fm_dataframe = pd.DataFrame( columns=column_names)
    for info_dict in dict_generator():
        x = np.random.randint(0, len(info_dict)-1)
        key = list(info_dict)[x]
        data.append(info_dict[key])
        fm_dataframe.append(data)
    return fm_dataframe


def calculate_premium(dataframe, n):
    """
    This function returns the total insurance premium of n customers based on their relativity of each variable that
    we have considered
    :param dataframe: dataframe with relativities of all the factors affecting insurance premium
    :param n: No. of customers
    :return: total insurance premium
    """


if __name__ == '__main__':
    df = create_df()
    print(df)