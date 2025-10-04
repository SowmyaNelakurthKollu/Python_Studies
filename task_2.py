from task_1 import *
import matplotlib.pyplot as plt

data = load_data('inc_subset.csv')

def mean_square_error(a, b, data_points): #a is the y-intercept of the line when x=0, and b is the slope of the line
    total_error = 0
    for i in range(len(data_points)):
        x = float(data_points[i][1])
        y = float(data_points[i][2])
        total_error += (y-((b*x)+a))**2 #here we are subtracting the actual value and predicted value before squaring
    
    return total_error/float(len(data_points)) 

def gradient_descent(a_now, b_now, data_points, L):
    a_gradient= 0 #this is to initialise the y-intercept value 
    b_gradient= 0 #this is to initialise the slope value 

    for i in range(len(data_points)):
        x = float(data_points[i][1]) #this line fetches data from age column in the data set and assigns to variable x 
        y = float(data_points[i][2]) #this line fetches data from salary column in the data set and assigns to variable y

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
print("Mean square error is: ", mean_square_error(a, b, data))


def plot_data(data_points, b, a, min_v, max_v):
  x = []
  y = []
  for i in range(len(data_points)):
    x.append(float(data_points[i][1]))
    y.append(float(data_points[i][2]))

  print(x)
  print(y)
  plt.scatter(x,y, color='black')
  plt.plot(list(range(min_v, max_v)), [((b*j) +a) for j in range(min_v, max_v)], color="red")
  plt.show()


plot_data(data, b, a, min_v=10, max_v=60)

#plt.scatter(data[i][1], data[i][2], color='black')
plt.plot(list(range(20,100)), [((b*x) +a) for x in range(20, 100)], color="red")
plt.show()
