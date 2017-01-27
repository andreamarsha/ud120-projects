#!/usr/bin/python

import numpy as np

def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where
        each tuple is of the form (age, net_worth, error).
    """

    cleaned_data = []


    ### your code goes here
    error = predictions - net_worths
    abs_error = abs(error)
    print abs_error

    total_removal = len(predictions)/10
    print total_removal
    i = 0

    # Remove data points with max absolute residual errors
    for i in range(0, total_removal):
        max_index = abs_error.argmax()
        predictions = np.delete(predictions, [max_index])
        ages = np.delete(ages, [max_index])
        net_worths = np.delete(net_worths, [max_index])
        abs_error = np.delete(abs_error, [max_index])

    cleaned_data = zip(ages, net_worths, predictions)

    return cleaned_data

