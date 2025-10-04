
#Task 1
#This function will check each grade and assign the minimum value based on next grade in the list
def min(gradeList):
    min_val = gradeList[0]
    for grade in gradeList:
        if grade < min_val:
            min_val =grade
    return min_val

#This function will check each grade and assign the maximum value based on next grade in the list
def max(gradeList):
    max_val =  gradeList[0]
    for grade in gradeList:
        if grade > max_val:
            max_val = grade
    return max_val

#This function will check size of the grade list and calls the another function where we get the return values of sum
# of grades  in the list
def mean(gradeList):
    count_gradelist = len(gradeList)
    total_val = total_sum_grades(gradeList)
    return total_val // count_gradelist

#Calculate sum of each grade which is in the list
def total_sum_grades(gradeList):
    total_grade = 0
    for grade in gradeList:
        total_grade +=grade
    return total_grade

#This function will calculates the variance of each grade and mean of the whole grade list

def calculate_variance(gradeList,mean_grade_value):
    variance_gradeslist = []
    i=0
    for grade in gradeList:
        variance_gradeslist.insert(i,mean_grade_value - grade)
        #print((mean_grade_value - grade)," mean_grade_value ",mean_grade_value, " Grade" ,grade ," Far from mean ", variance_gradeslist ,  " i value ",i)
        i=i+1
    return variance_gradeslist

def standard_deviation(variance_gradeList):
    sum_varianceList = total_sum_grades(variance_gradeList)
    return sum_varianceList**0.5



def median_abosolute_deviation(gradeList,median_grade_value):
    absolute_grade_list= calculate_variance(gradeList,median_grade_value)
    median_absolute_value = median_grade(absolute_grade_list)
    return median_absolute_value


def median_grade(gradeList):
    gradeList.sort()
    return gradeList[(len(gradeList)//2)]



#Task 2
grades  = [8,6,1,7,22,27,9,10,1,-1,0]
#The below function call returns the minimum grade values from the grades list
lower_grade_value = min(grades)
print(lower_grade_value," Lower grade")
#The below function call returns the maximum grade values from the grades list
higher_grade_value = max(grades)
print(higher_grade_value," Higher grade")
#The below function call returns the mean values for the grades list
mean_grade_value = mean(grades)
print(mean_grade_value," Mean grade")
#The below function call returns the list how must variance of mean for each grade
variance_grade_value = calculate_variance(grades,mean_grade_value)
print(grades ," Variance for these grades are : ",variance_grade_value)
#The below function provides the Standard deviation variance from the grade list.
standard_deviation_value = standard_deviation(variance_grade_value)
print("Standard_Deviation Value for these grades are : ",standard_deviation_value)
#The below function provides the median  from the grade list.
median_grade_value = median_grade(grades)
print("Median Value for these grades are : ",median_grade_value)
#The below function provides the Absolute_Median  from the grade list
absolute_median_grade_value = median_abosolute_deviation(grades,median_grade(grades))
print("Absolute Median Value for these grades are : ",absolute_median_grade_value)

