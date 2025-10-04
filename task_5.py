import numpy as np
from task_1 import load_data
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score


data_points = load_data("clean_data.csv")

#create a separate list of age and salary to feed into the "poly1d" function used in poly_model variable 
age = []
salary = []
for i in range(len(data_points)):
    age.append(float(data_points[i][0]))
    salary.append(float(data_points[i][1]))

poly_model = np.poly1d(np.polyfit(age, salary, 2)) #this line creates the equation of the line that best fits our datapoints 

list_of_values = list(range(1, 100))


plt.scatter(age, salary)
plt.plot(list_of_values, poly_model(list_of_values))
plt.show()


    



