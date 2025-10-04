import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('inc_subset copy.csv')

def mean_square_error(a, b, data_points): #a is the y-intercept of the line when x=0, and b is the slope of the line
    total_error = 0
    for i in range(len(data_points)):
        x = data_points.iloc[i].age
        y = data_points.iloc[i].salary
        total_error += (y-((b*x)+a))**2 #here we are subtracting the actual value and predicted value before squaring
    
    return total_error/float(len(data_points)) 

def gradient_descent(a_now, b_now, data_points, L):
    a_gradient= 0 #this is to initialise the y-intercept value 
    b_gradient= 0 #this is to initialise the slope value 

    for i in range(len(data_points)):
        x = data_points.iloc[i].age #this line fetches data from age column in the data set and assigns to variable x 
        y = data_points.iloc[i].salary #this line fetches data from salary column in the data set and assigns to variable y
        print(x)
        print(y)
        sub_formula = (int(b_now) * int(x)) + int(a_now)
        print(sub_formula)
        #the below two formulas are calculated using the partial derivative of MSE equation with respect to a, and respectviely 
        a_gradient += -(2/len(data_points))*(y-((b_now*x)+a_now)) 
        b_gradient += -(2/len(data_points))*x*(y-((b_now*x)+a_now))

    a = a_now - a_gradient * L 
    b = b_now - b_gradient * L

    return a, b 

a = 0 #initial value of the y-intercept 
b = 0 #initial value of the slope 
L = 0.0004 #learning curve can be varied to fit the line accordingly 
n_iterations = 300 #this iteration value can be varied depending on how a, and b fits the model 

for i in range(n_iterations):
    a, b = gradient_descent(a, b, data, L)

a, b = gradient_descent(a, b, data, L)
print("Value of y-intercept a is {intercept} and value of slope b is {slope}".format(intercept=a,slope=b))
plt.scatter(data.age, data.salary, color='black')
plt.plot(list(range(20,50)), [((b*x) +a) for x in range(20, 50)], color="red")

plt.show()
