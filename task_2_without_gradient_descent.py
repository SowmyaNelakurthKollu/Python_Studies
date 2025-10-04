from task_1 import *
import matplotlib.pyplot as plt

data = load_data('inc_subset.csv')

def calc_a_b(data_points):
    sum_xy = 0
    sum_x = 0
    sum_y = 0
    sum_x2 = 0
    sum_y2 = 0

    for i in range(len(data_points)):
       sum_xy += (float(data_points[i][1])*float(data_points[i][2]))
       sum_x +=  float(data_points[i][1])
       sum_y += float(data_points[i][2])
       sum_x2 += float(data_points[i][1])**2
       sum_y2 += float(data_points[i][2])**2
    
    b = ((len(data_points)*sum_xy)-(sum_x*sum_y))/((len(data_points)*sum_x2)-(sum_x)**2)
    a = (sum_y-(b*sum_x))/len(data_points)

    return a, b 


a, b = calc_a_b(data)
print("Value of y-intercept a is {intercept} and value of slope b is {slope}".format(intercept=a,slope=b))


def mean_square_error(a, b, data_points): #a is the y-intercept of the line when x=0, and b is the slope of the line
    total_error = 0
    for i in range(len(data_points)):
        x = float(data_points[i][1])
        y = float(data_points[i][2])
        total_error += (y-((b*x)+a))**2 #here we are subtracting the actual value and predicted value before squaring
    
    return total_error/float(len(data_points)) 


print("Mean square error is: ", mean_square_error(a, b, data))


def plot_data(data_points, b, a, min_v, max_v):
  x = []
  y = []
  for i in range(len(data_points)):
    x.append(float(data_points[i][1]))
    y.append(float(data_points[i][2]))

  plt.scatter(x,y, color='black')
  plt.plot(list(range(min_v, max_v)), [((b*j) +a) for j in range(min_v, max_v)], color="red")
  plt.show()


plot_data(data, b, a, min_v=20, max_v=50)


