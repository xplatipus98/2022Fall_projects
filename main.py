"""
FINANCIAL MODELING OF INSURANCE COMPANY (AUTO INSURANCE) USING MONTE CARLO SIMULATION
AUTHORS
ANTARA CHANSARKAR
SAKET NAIK
SPARSH SADAFAL
"""

import pandas as pd
import numpy as np
from scipy.stats import truncnorm
import matplotlib.pyplot as plt
from random import randint
import warnings

warnings.filterwarnings("ignore")


def get_truncated_normal(mean=0, sd=1, low=0, upp=10):
    """Returns randomly generated value from normal distribution with a set maximum and minimum value
    :return: Random floating point number
    """
    return truncnorm(
        (low - mean) / sd, (upp - mean) / sd, loc=mean, scale=sd)


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
                      "Coverage (past 1 year)": 1.05}
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
    information_dict = {'age': age, 'driving_hist_dui': driving_hist_dui,
                        'driving_hist_reckless': driving_hist_reckless, 'driving_hist_speeding': driving_hist_speeding,
                        'credit_score': credit_score, 'driving_exp': driving_exp, 'location': location,
                        'insurance_hist': insurance_hist, 'annual_mileage': annual_mileage,
                        'marital_status': marital_status, 'claims_hist': claims_hist, 'coverage_level': coverage_level,
                        'deductible': deductible, 'vehicle_safety': vehicle_safety}
    return information_dict


def get_age_relativity(age_dict):
    relativity = 1
    random_age = int(get_truncated_normal(mean=40, sd=20, low=300, upp=850).rvs())
    if 18 <= random_age < 25:
        relativity = age_dict["18-24 years"]
    elif 25 <= random_age <= 45:
        relativity = age_dict["25-45 years"]
    elif 45 < random_age <= 60:
        relativity = age_dict["45-60 years"]
    elif 60 < random_age:
        relativity = age_dict["60+ years"]
    return relativity


def get_credit_relativity(credit_dict):
    relativity = 1
    random_credit = int(get_truncated_normal(mean=700, sd=100, low=350, upp=850).rvs())
    if 300 <= random_credit < 580:
        relativity = credit_dict["300-579"]
    elif 580 <= random_credit < 670:
        relativity = credit_dict["580-669"]
    elif 670 <= random_credit < 740:
        relativity = credit_dict["670-739"]
    elif 740 <= random_credit < 800:
        relativity = credit_dict["740-799"]
    elif 800 <= random_credit:
        relativity = credit_dict["800-850"]
    return relativity

def get_general_relativity(val_dict, variable):
    """
    Finds random relativity of varibales not associated with any distribution
    :return: relativity
    """
    d = val_dict[variable]
    relativity = list(d.values())[np.random.randint(0, len(d))]
    return relativity
def get_relativity(info_dict):
    """

    :param info_dict:
    :return: dictionary with relativity values
    """
    age_relativity = get_age_relativity(info_dict['age'])
    driving_history_dui_relativity = get_general_relativity(info_dict,'driving_hist_dui')
    driving_hist_reckless_relativity = get_general_relativity(info_dict,'driving_hist_reckless')
    driving_hist_speeding_relativity = get_general_relativity(info_dict,'driving_hist_speeding')
    credit_score_relativity = get_credit_relativity(info_dict['credit_score'])
    driving_exp_relativity = get_general_relativity(info_dict,'driving_exp')
    location_relativity = get_general_relativity(info_dict,'location')
    insurance_hist_relativity = get_general_relativity(info_dict,'insurance_hist')
    annual_mileage_relativity = get_general_relativity(info_dict,'annual_mileage')
    marital_status_relativity = get_general_relativity(info_dict,'marital_status')
    claims_hist_relativity = get_general_relativity(info_dict,'claims_hist')
    coverage_level_relativity = get_general_relativity(info_dict,'coverage_level')
    deductible_relativity = get_general_relativity(info_dict,'deductible')
    vehicle_safety_relativity = get_general_relativity(info_dict,'vehicle_safety')
    relativity_dict = {"Age": age_relativity, "Driving_History_DUI": driving_history_dui_relativity, "Driving_History_reckless": driving_hist_reckless_relativity,
             "Driving_History_speeding": driving_hist_speeding_relativity, "Credit_Score": credit_score_relativity,
             "Years_of_Driving": driving_exp_relativity, "Location": location_relativity, "Insurance_History": insurance_hist_relativity,
             "Annual_Mileage": annual_mileage_relativity, "Marital_Status": marital_status_relativity,
             "Claims_History": claims_hist_relativity, "Coverage_level": coverage_level_relativity, "Deductible": deductible_relativity,
             "Vehicle": vehicle_safety_relativity}
    return relativity_dict

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
    # print(fm_dataframe.head())
    calculate_premium(fm_dataframe)


def cal_relativity(data):
    """
    Finds final relativity of each customer and the total premium of all the customers
    :param data: list of dictionaries with randomized values of relativity for each variable
    :return: list with aggregate relativity for each customer
    """
    relativities = []
    premium_per_customer = []
    base_premium = 1600  # assumption
    total_premium = 0

    for customer in data:
        relativity_per_customer = 1
        for columns, relativity in customer.items():
            relativity_per_customer = relativity_per_customer * relativity
        relativities.append(relativity_per_customer)
        premium_per_customer.append(base_premium * relativity_per_customer)
        total_premium = total_premium + (base_premium * relativity_per_customer)

    return relativities, total_premium


def calculate_premium(df):
    """
    This function returns the total insurance premium of n customers based on their relativity of each variable that
    we have considered
    :param df:
    :param dataframe: dataframe with relativity of all the factors affecting insurance premium
    :param n: No. of customers
    :return: total insurance premium
    """
    baseline_premium = 1600
    df['Relativity'] = df['Age'] * df['Driving_History_DUI'] * df['Driving_History_reckless'] * \
                       df['Driving_History_speeding'] * df['Credit_Score'] * df['Years_of_Driving'] * df['Location'] * \
                       df['Insurance_History'] * df['Annual_Mileage'] * df['Marital_Status'] * df['Claims_History'] * \
                       df['Coverage_level'] * df['Deductible'] * df['Vehicle']
    df['Calculated_premium'] = baseline_premium * df['Relativity']
    print(df['Relativity'].head(20))
    df.to_csv('initial_df.csv')


if __name__ == '__main__':
    create_df(10)
