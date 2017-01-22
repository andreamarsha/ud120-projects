#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

# Number of people in the dataset
print "Number of people in the dataset = ", len(enron_data)

# Number of features in the dataset
print "Number of features in the dataset = ", len(enron_data['METTS MARK'])

# Function to count the number of persons of interest
def count_poi(index):
    poi = 0
    for entry in index:
        if index[entry]['poi'] == 1:
            poi+= 1
    return poi

print "Number of POI = ", count_poi(enron_data)

# Query Exercises
print "Stock belonging to James Prentice = ", enron_data['PRENTICE JAMES']['total_stock_value']
print "Emails from Wesley Colwell to POIs = ", enron_data['COLWELL WESLEY']['from_this_person_to_poi']
print "Stock options exercised by Jeffrey K Skilling = ", enron_data['SKILLING JEFFREY K']['exercised_stock_options']

# Compare payments for Enron executives
print "Lay : ", enron_data['LAY KENNETH L']['total_payments']
print "Skilling : ", enron_data['SKILLING JEFFREY K']['total_payments']
print "Fastow: ", enron_data['FASTOW ANDREW S']['total_payments']

# Function to count non-NaN input
def count_non_NaN(index, feature):
    non_NaN = 0
    for name in index:
        if index[name][feature] != 'NaN':
            non_NaN += 1
    return non_NaN

print "Quantified salary: ", count_non_NaN(enron_data, 'salary')
print "Known email address: ", count_non_NaN(enron_data, 'email_address')

# Count NaN total payments
nan_total_payments = len(enron_data) - count_non_NaN(enron_data, 'total_payments')
print "Non-quantified total payments: ", nan_total_payments
print "% of non-quantified total payments: ", nan_total_payments*1.0/len(enron_data)

# Count POI with NaN total payments
def count_NaN_POI(index, feature):
    count = 0
    for name in index:
        if index[name]['poi'] == 1 and index[name][feature] == 'NaN':
            count += 1
    return count

print "POIs with NaN total payments: ", count_NaN_POI(enron_data, 'total_payments')
