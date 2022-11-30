"""
FINANCIAL MODELING OF INSURANCE COMPANY (AUTO INSURANCE) USING MONTE CARLO SIMULATION
AUTHORS
ANTARA CHANSARKAR
SAKET NAIK
SPARSH SADAFAL
"""
import copy
import random
from typing import List

import pandas as pd
import numpy as np
from scipy.stats.distributions import poisson
from scipy.stats import truncnorm

import statistics
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
    coverage_level = {"10000-20000": 0.94, "20000-30000": 0.97, "30000-40000": 1, "40000-50000": 1.05,
                      "50000-60000": 1.09, "60000-70000": 1.12, "70000-80000": 1.15, "80000-90000": 1.18,
                      "90000-100000": 1.22, "100000-110000": 1.25, "110000-120000": 1.28, "120000-130000": 1.32,
                      "130000-140000": 1.35, "140000-150000": 1.38}
    deductible = {"No deductible": 1.2, "$250": 1, "$500": 0.9, "$1000": 0.8}
    vehicle_safety = {"0 NCAP": 1.15, "1 NCAP": 1.1, "2 NCAP": 1.05, "3 NCAP": 1,
                      "4 NCAP": 0.95, "5 NCAP": 0.9}
    information_dict = {'age': age, 'driving_hist_dui': driving_hist_dui,
                        'driving_hist_reckless': driving_hist_reckless, 'driving_hist_speeding': driving_hist_speeding,
                        'credit_score': credit_score, 'driving_exp': driving_exp, 'location': location,
                        'insurance_hist': insurance_hist, 'annual_mileage': annual_mileage,
                        'marital_status': marital_status, 'claims_hist': claims_hist, 'coverage_level': coverage_level,
                        'deductible': deductible, 'vehicle_safety': vehicle_safety}

    aggregate_dict = copy.deepcopy(information_dict)
    for key in aggregate_dict:
        for k in aggregate_dict[key]:
            aggregate_dict[key][k] = 0
    # print(information_dict)
    # print(get_relativity(information_dict, aggregate_dict))
    # print(aggregate_dict)
    return information_dict, aggregate_dict


def get_age_relativity(age_dict, agg_age_dict):
    # agg_age_dict = {"18-24 years": 0, "25-45 years": 0, "45-60 years": 0,
    #            "60+ years": 0}
    relativity = 1
    random_age = int(get_truncated_normal(mean=40, sd=20, low=18, upp=80).rvs())
    if 18 <= random_age < 25:
        relativity = age_dict["18-24 years"]
        agg_age_dict["18-24 years"] += 1
    elif 25 <= random_age <= 45:
        relativity = age_dict["25-45 years"]
        agg_age_dict["25-45 years"] += 1
    elif 45 < random_age <= 60:
        relativity = age_dict["45-60 years"]
        agg_age_dict["45-60 years"] += 1
    elif 60 < random_age:
        relativity = age_dict["60+ years"]
    return relativity


def get_credit_relativity(credit_dict, agg_credit_dict):
    # agg_credit_score = {"300-579": 0, "580-669": 0, "670-739": 0,
    #               "740-799": 0, "800-850": 0}
    relativity = 1
    random_credit = int(get_truncated_normal(mean=700, sd=100, low=350, upp=850).rvs())
    if 300 <= random_credit < 580:
        relativity = credit_dict["300-579"]
        agg_credit_dict["300-579"] += 1
    elif 580 <= random_credit < 670:
        relativity = credit_dict["580-669"]
        agg_credit_dict["580-669"] += 1
    elif 670 <= random_credit < 740:
        relativity = credit_dict["670-739"]
        agg_credit_dict["670-739"] += 1
    elif 740 <= random_credit < 800:
        relativity = credit_dict["740-799"]
        agg_credit_dict["740-799"] += 1
    elif 800 <= random_credit:
        relativity = credit_dict["800-850"]
        agg_credit_dict["800-850"] += 1
    return relativity


def get_general_relativity(val_dict, agg_dict, variable):
    """
    Finds random relativity of varibales not associated with any distribution
    :return: relativity
    """
    d = val_dict[variable]
    x = np.random.randint(0, len(d))
    relativity = list(d.values())[x]
    key = list(d.keys())[list(d.values()).index(relativity)]
    agg_dict[variable][key] += 1
    return relativity


def get_relativity(info_dict, agg_dict):
    """

    :param agg_dict:
    :param info_dict:
    :return: dictionary with relativity values
    """
    age_relativity = get_age_relativity(info_dict['age'], agg_dict['age'])
    driving_history_dui_relativity = get_general_relativity(info_dict, agg_dict, 'driving_hist_dui')
    driving_hist_reckless_relativity = get_general_relativity(info_dict, agg_dict, 'driving_hist_reckless')
    driving_hist_speeding_relativity = get_general_relativity(info_dict, agg_dict, 'driving_hist_speeding')
    credit_score_relativity = get_credit_relativity(info_dict['credit_score'], agg_dict['credit_score'])
    driving_exp_relativity = get_general_relativity(info_dict, agg_dict, 'driving_exp')
    location_relativity = get_general_relativity(info_dict, agg_dict, 'location')
    insurance_hist_relativity = get_general_relativity(info_dict, agg_dict, 'insurance_hist')
    annual_mileage_relativity = get_general_relativity(info_dict, agg_dict, 'annual_mileage')
    marital_status_relativity = get_general_relativity(info_dict, agg_dict, 'marital_status')
    claims_hist_relativity = get_general_relativity(info_dict, agg_dict, 'claims_hist')
    coverage_level_relativity = get_general_relativity(info_dict, agg_dict, 'coverage_level')
    deductible_relativity = get_general_relativity(info_dict, agg_dict, 'deductible')
    vehicle_safety_relativity = get_general_relativity(info_dict, agg_dict, 'vehicle_safety')
    relativity_dict = {"Age": age_relativity, "Driving_History_DUI": driving_history_dui_relativity,
                       "Driving_History_reckless": driving_hist_reckless_relativity,
                       "Driving_History_speeding": driving_hist_speeding_relativity,
                       "Credit_Score": credit_score_relativity,
                       "Years_of_Driving": driving_exp_relativity, "Location": location_relativity,
                       "Insurance_History": insurance_hist_relativity,
                       "Annual_Mileage": annual_mileage_relativity, "Marital_Status": marital_status_relativity,
                       "Claims_History": claims_hist_relativity, "Coverage_level": coverage_level_relativity,
                       "Deductible": deductible_relativity,
                       "Vehicle": vehicle_safety_relativity}
    return relativity_dict


def cal_relativity(number_of_customers):
    """
    Finds final relativity of each customer and the total premium of all the customers
    :param number_of_customers:
    :return: list with aggregate relativity for each customer
    """
    relativities = []
    coverage_levels = []
    base_premium = 1600  # assumption
    total_premium = 0
    info_dict, agg_list = dict_generator()

    for i in range(0, number_of_customers):
        relativity_per_customer = 1
        data_dict = get_relativity(info_dict, agg_list)
        for column, relativity in data_dict.items():
            relativity_per_customer = relativity_per_customer * relativity
            if column == 'Coverage_level':
                coverage_levels.append(relativity)
        relativities.append(relativity_per_customer)
        total_premium = total_premium + (base_premium * relativity_per_customer)
    # print(relativities)
    # print("Total premium: {}".format(total_premium))
    return relativities, round(total_premium, 3), coverage_levels


def find_total_claim_amt(no_cust):
    """
    This function finds probability of claim via poisson dist and severity of claim via
    :return: probability of claim for each customer
    """
    rel, total_premium, coverages_rel = cal_relativity(no_cust)
    # bin the relativity scores as poisson pmf function cannot directly fit floating point values of relativity
    relativity_int = bin_relativity(rel)
    freq_prob = poisson.pmf(relativity_int, statistics.mean(rel))
    claim_sev = []
    for coverage_rel in coverages_rel:
        coverage_val = find_claim_severity(coverage_rel)
        claim_sev.append(coverage_val)
    print("Frequency Probabilities: {}".format(freq_prob))
    print("Claim severity: {}".format(claim_sev))
    total_claim_amount = sum([x * y for x, y in zip(freq_prob, claim_sev)])
    return round(total_claim_amount, 3)


def find_claim_severity(coverage_relativity):
    """
    This function finds the claim severity by fitting the relativity into a normal distribution
    :return: Returns a number which is the claim severity
    """
    coverage_bucket_dict = dict_generator()[0]['coverage_level']
    for claim_severity_level, coverage_bucket in coverage_bucket_dict.items():
        if coverage_relativity == coverage_bucket:
            claim_level = claim_severity_level.split("-")
            claim_level = [int(i) for i in claim_level]
            claim_val = np.random.normal(statistics.mean(claim_level), statistics.stdev(claim_level))
    return round(claim_val, 2)


def bin_relativity(rel_list):
    """
    This function bins the relativity values at different integer levels to be used for fitting to various distributions
    :return: List of binned relativity values
    """
    rel_int: list[int] = []
    for value in rel_list:
        if value > 5:
            rel_int.append(10)
        elif value > 4:
            rel_int.append(9)
        elif value > 3.5:
            rel_int.append(8)
        elif value > 3:
            rel_int.append(7)
        elif value > 2.5:
            rel_int.append(6)
        elif value > 2:
            rel_int.append(5)
        elif value > 1.5:
            rel_int.append(4)
        elif value > 1.35:
            rel_int.append(3)
        elif value > 1.2:
            rel_int.append(2)
        else:
            rel_int.append(1)
    return rel_int


def find_SD():
    """
    calculated standard deviation of each bucket
    :return: a list with standard deviations of each bucket
    """
    info_dict, agg_list = dict_generator()
    sd_dict = {}
    for key, value in info_dict.items():
        sd_dict[key] = statistics.stdev(list(value.values()))
    return sd_dict


def optimize_profit(no_of_cust):
    """

    :return:
    """
    n = 1
    info_dict, agg_dict = dict_generator()
    rel_dict = get_relativity(info_dict, agg_dict)
    sd = find_SD()
    # for v in range(len(rel_dict)):"""

    total_revenue_from_premium = cal_relativity(no_of_cust)[1]
    print("Total revenue earned from insurance premium: {}".format(total_revenue_from_premium))
    total_claim_val = find_total_claim_amt(no_of_cust)
    print("Total value of claims: {}".format(total_claim_val))
    pl_from_premium = round(total_revenue_from_premium - total_claim_val, 3)
    print("Company PL: {}".format(pl_from_premium))


# UNUSED FUNCTIONS BLOCK
def calculate_premium(df):

    baseline_premium = 1600
    df['Relativity'] = df['Age'] * df['Driving_History_DUI'] * df['Driving_History_reckless'] * \
                       df['Driving_History_speeding'] * df['Credit_Score'] * df['Years_of_Driving'] * df['Location'] * \
                       df['Insurance_History'] * df['Annual_Mileage'] * df['Marital_Status'] * df['Claims_History'] * \
                       df['Coverage_level'] * df['Deductible'] * df['Vehicle']
    df['Calculated_premium'] = baseline_premium * df['Relativity']
    print(df['Relativity'].head(20))


def create_df(number_of_customers):

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


if __name__ == '__main__':
    # cal_relativity(5000)
    optimize_profit(500)
    # find_claim_severity(1)



