import random

import numpy as np
import pandas as pd


def create_df():
    """
    Creates a dataframe with values of all the variables being considered for the auto insurance financial model
    :return: dataframe with relativity of all the variables
    """
    data = []
    for i in dict_generator():
        x = np.random.randint(0, len(i))
        key = list(i)[x]
        data.append(i[key])

    column_names = ['Age', 'Driving_History', 'Credit_Score', 'Years_of_Driving', 'Location', 'Insurance_History',
                    'Annual_Mileage', 'Marital_Status', 'Claims_History', 'Coverage_level', 'Deductible', 'Vehicle']
    fm_dataframe = pd.DataFrame(data, columns=column_names)
    return fm_dataframe


def calculate_premium(dataframe, n):
    """
    This function returns the total insurance premium of n customers based on their relativity of each variable that
    we have considered
    :param dataframe: dataframe with relativities of all the factors affecting insurance premium
    :param n: No. of customers
    :return: total insurance premium
    """
