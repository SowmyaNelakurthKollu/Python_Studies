import csv
import matplotlib.pyplot as plt

def load_data(file_name):
    clean_list = []

    with open(file_name) as data:
        csv_data = csv.reader(data, delimiter=',')
        next(csv_data) #this will remove the header from the csv file

        for row in csv_data:
            clean_list.append(row)
                    
        return clean_list


provided_data = load_data('inc_subset.csv')
for r in provided_data:
    print(r)

