from operator import index, indexOf
from selectors import SelectSelector
import matplotlib.pyplot as plt
import matplotlib.pyplot as pltd
import pandas as pd
import numpy as np
from scipy.stats import false_discovery_control


#we can also use with keyword instead of open and closing file statements below if we use built-in functions.
def readingfile(filename,mode_of_file,regional_file):
    file = open(filename, mode_of_file)
    cleaned_data = []
    final_data = []
    i = 0
    for line in file:
        if(regional_file == False):
            inc_subset_data = line.replace('\n', '').split(",")
            final_data.append(inc_subset_data)
            del inc_subset_data[0]
            print(i,"  ",inc_subset_data.__getitem__(0),"  ",inc_subset_data.__getitem__(1))
        else :
            inc_subset_data = line.replace('\n', '').split(",")
            print(inc_subset_data.__getitem__(0),"  ",inc_subset_data.__getitem__(1),"  ",inc_subset_data.__getitem__(2))
            inc_subset_data[2] = inc_subset_data[2].replace(' years', '').replace('100+','100')
            cleaned_data.append(inc_subset_data)
        i+=1
    if(regional_file == False):
        return final_data
    else:
        return cleaned_data

def mean_square_error(a, b, data_points):  # a is the y-intercept of the line when x=0, and b is the slope of the line
    total_error = 0
    for i in range(len(data_points)):
        x = float(data_points[i].__getitem__(0))
        y = float(data_points[i].__getitem__(1))

        total_error += (y-((b*x)+a))**2 #here we are subtracting the actual value and predicted value before squaring
    return total_error / float(len(data_points))


def gradient_descent(a_now, b_now, data_points, L):
    a_gradient = 0  # this is to initialise the y-intercept value
    b_gradient = 0  # this is to initialise the slope value
    for i in range(len(data_points)):
        x= float(data_points[i].__getitem__(0))# this line fetches data from age column in the data set and assigns to variable x
        y= round(float(data_points[i].__getitem__(1)),6)# this line fetches data from salary column in the data set and assigns to variable y

        # the below two formulas are calculated using the partial derivative of MSE equation with respect to a, and respectviely
        a_gradient += -(2 / len(data_points)) * (y - ((b_now * x) + a_now))
        b_gradient += -(2 / len(data_points)) * x * (y - ((b_now * x) + a_now))
    a = a_now - a_gradient * L
    b = b_now - b_gradient * L
    return a, b


print("---------Task 1-----------")
file_data_task1 = readingfile("inc_subset.csv","r",False)
file_data_task1.pop(0)

validation_percentage = 0.8
index_till = int(validation_percentage * len(file_data_task1))
train_data = file_data_task1[:index_till]
test_data = file_data_task1[index_till:]


print("---------Task 2-----------")
a = 0 #initial value of the y-intercept
b = 0 #initial value of the slope
L = 0.0004 #learning curve can be varied to fit the line accordingly
n_iterations = 300 #this iteration value can be varied depending on how a, and b fits the model
for i in range(n_iterations):
    a, b = gradient_descent(a, b, train_data, L)
a, b = gradient_descent(a, b, train_data, L)
print("Value of y-intercept a is {intercept} and value of slope b is {slope}".format(intercept=a,slope=b))

age_List =[]
salary_List=[]
for data in train_data:
    age_List.append(float(data[0]))
    salary_List.append(float(data[1]))

plt.scatter(age_List, salary_List, color='orange')
i=0
for x in range(20,30):
    print(((b*x) +a),salary_List[i])
    i+=1



plt.plot(list(range(20,50)), [((b*x) +a) for x in range(20, 50)], color="green")
plt.show()

age_List_test_Data =[]
salary_List_test_Data=[]
for data in test_data:
    age_List_test_Data.append(float(data[0]))
    salary_List_test_Data.append(float(data[1]))


plt.scatter(age_List_test_Data, salary_List_test_Data, color='orange')
plt.plot(list(range(20,50)), [((b*x) +a) for x in range(20, 50)], color="green")
plt.show()






mse_value = mean_square_error(a,b,file_data_task1)
print("MSE value for only age  & 2020 data file", mse_value)

#Task 3
print("--------- Task3 --------")
file_data_val = readingfile("inc_utf.csv","r",True)
age_data =[]
salary_data=[]
del file_data_val[0]
for data in file_data_val:
    age_data.append(float(data[2]))
    salary_data.append(float(data[3]))


linear_regression_data = pd.DataFrame({'Age': age_data,'2020': salary_data})
mean_data = linear_regression_data.groupby(['Age']).mean().reset_index()
print(mean_data)

regional_data =[]
i=0
age_List_data =[]
salary_List_data=[]
for get_regional_data in range(len(mean_data)) :
    age_List_data.append(round(mean_data['Age'][i],6))
    salary_List_data.append(round(mean_data['2020'][i],6))
    regional_data.append([mean_data['Age'][i],mean_data['2020'][i]])
    i = i+1



def calc_a_b(data_points):
    sum_xy = 0
    sum_x = 0
    sum_y = 0
    sum_x2 = 0
    sum_y2 = 0

    for i in range(len(data_points)):
        sum_xy += (float(data_points[i][0]) * float(data_points[i][1]))
        sum_x += float(data_points[i][0])
        sum_y += float(data_points[i][1])
        sum_x2 += float(data_points[i][0]) ** 2
        sum_y2 += float(data_points[i][1]) ** 2

    b = ((len(data_points) * sum_xy) - (sum_x * sum_y)) / ((len(data_points) * sum_x2) - (sum_x) ** 2)
    a = (sum_y - (b * sum_x)) / len(data_points)

    return a, b


c = 0 #initial value of the y-intercept
d = 0 #initial value of the slope
Li = 0.0002 #learning curve can be varied to fit the line accordingly
n_iterations = 300 #this iteration value can be varied depending on how a, and b fits the model
#for i in range(n_iterations):
#    c, d = gradient_descent(c, d, regional_data, Li)


c, d  = calc_a_b(regional_data)
#c, d = gradient_descent(c, d, regional_data, Li)
print("Regional Value of y-intercept a is {intercept} and value of slope b is {slope}".format(intercept=c,slope=d))
#pltd.scatter(age_List_data, salary_List_data, color='blue')
#pltd.plot(list(range(20,100)), [((c*dt) +d) for dt in range(20,100)], color="red")
#pltd.show()


def plot_data(data_points, b, a, min_v, max_v):
  x = []
  y = []
  for i in range(len(data_points)):
    x.append(float(data_points[i][0]))
    y.append(float(data_points[i][1]))

  plt.scatter(x,y, color='black')
  plt.plot(list(range(min_v, max_v)), [((b*j) +a) for j in range(min_v, max_v)], color="red")
  plt.show()


plot_data(regional_data, d, c, min_v=10, max_v=100)
mse_value = mean_square_error(c,d,regional_data)
print("MSE value for regional data file", mse_value)


print("---------Task5------")


poly_model = np.poly1d(np.polyfit(age_List_data, salary_List_data, 3)) #this line creates the equation of the line that best fits our datapoints

list_of_values = list(range(0, 100))

plt.scatter(age_List_data, salary_List_data)
plt.plot(list_of_values, poly_model(list_of_values))
plt.show()