import pandas as pd
from matplotlib import pyplot as plt

def get_distinct_ocean_proximity():
    ocean_proximity_values = data["ocean_proximity"].tolist()
    ocean_proximity_data = []
    for ocean_proximity in ocean_proximity_values:
        if ocean_proximity not in ocean_proximity_data:
           ocean_proximity_data.append(ocean_proximity)
    return ocean_proximity_data

#Mean value of the list
def mean_data(gradeList):
    count_gradelist = len(gradeList)
    total_val = total_sum_grades(gradeList)
    return total_val // count_gradelist

def total_sum_grades(gradeList):
    total_grade = 0.0
    for grade in gradeList:
        total_grade +=grade
    return total_grade

grades  = [8,6,1,7,22,27,9,10,1,-1,0]
plt.hist(grades)
plt.title("Histogram regarding grades")
plt.show()
data = pd.read_csv('/Users/SowmyaN/PycharmProjects/Assignments/housing.csv')
print(data)

print("")
print("4.1 Exercise")
print("Number of districts loaded", len(data)-1)
print("")
print("")


print("")
print("4.3 Exercise")
print("Please check the plots")

amount_of_households=data["households"].tolist()
plt.hist(amount_of_households,50)
plt.title("Amount of households")
plt.show()

median_income =data["median_income"].tolist()
plt.hist(median_income)
plt.title("Median Income")
plt.show()

housing_median_age=data["housing_median_age"].tolist()
plt.hist(housing_median_age,50)
plt.title("Housing median age")
plt.show()

median_house_value=data["median_house_value"].tolist()
plt.hist(median_house_value,50)
plt.title("Median house value")
plt.show()


print("")
print("4.2 Exercise")


median_house_value_data = mean_data(median_house_value)
print("Median_House_Value ",median_house_value_data)


print("")
print("4.4 Exercise")
print("The Magnitude values are different as it took the graph according to the data that we have.")
print("")
print("4.5 Exercise")
print("The Magnitude values are different as it took the graph according to the data that we have.")





value_proximity = get_distinct_ocean_proximity()

def calculate_proximity(value_proximity):
    housingdata = pd.DataFrame(data)
    print("")
    print("4.1 Exercise")
    for ocean_proxi in value_proximity:
      list_median_house_value = housingdata[housingdata['ocean_proximity']==ocean_proxi].groupby('ocean_proximity')['median_house_value'].apply(list)
      #print(list_median_house_value.values.tolist())
      for ocean_each_proxi in list_median_house_value.values.tolist():
         mean_of_ocean_proxi  = mean_data(ocean_each_proxi)
         print("Oceanproximity mean for ", ocean_proxi, "is ", mean_of_ocean_proxi)

calculate_proximity(value_proximity)

