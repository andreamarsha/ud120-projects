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

