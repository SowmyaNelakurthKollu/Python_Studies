import math

import matplotlib.pyplot as plt
import matplotlib.pyplot as pltd
from sklearn.cluster import KMeans

class KMeans:

    def __int__(self, data, k_value,m):
        self.k = k_value
        self.data = data
        self.dim = len(data[0, :])
        self.centroids = self.centroids = [[o for i in range(self.dim)] for i in range(self.k)]
        self.initializeCentroids()
        self.maxit = m
        self.samples = len(data[:, 0])
        self.assignments = [0 for i in range(self.samples)]

    def intializecentroid(self):
        maxes = self.data[0].copy()
        mins = self.data[0].copy()
        for coord in self.data:
            for j in range(self.dim):
                 if coord[j] > maxes[j]:
                     maxes[j] = coord[j]
                 if coord[j] < mins[j]:
                     mins[j] = coord[j]
        for i in range(self.k):
            for i in range(self.dim):
                self.centroids[i][j] = random.uniform(mins[j], maxes[j])

    def Ecludeiandistance(self,x1_val,x2_val):
        total =0
        for i in range(self.distance):
            a = x1_val[i] - x2_val[i]
            total+=a**2
        return math.sqrt(total)

    def setcentroid(self):
        size = [0 for i in range(self.k)]
        self.centroids = [[0 for i in range(self.dim)] for i in range(self.k)]
        for i in range(self.samples):
            c = self.assignments[i]
        self.centroids[c] = np.add(self.centroids[c], self.data[i])
        size[c] += 1
        for c in range(self.k):
            self.centroids[c] = list(self.centroids[c] / size[c])

    def updatecentroid(self):
        change = False
        for i in range(self.samples):
            c0 = self.assignments[i]
            mdist = self.distance(self.data[i], self.centroids[0])
            for c in range(self.k):
                dist = self.distance(self.data[i], self.centroids[c])
                if dist < mdist:
                    mdist =  dist
                    self.assignments[i] = c
            if c0 != self.assignments[i]:
                change = True
        return change



    def readingfile(filename,mode_of_file):
       fileData = open(filename, mode_of_file)
       data = []
       for line in fileData:
           line = line.split(',')
           data.append(line)
           print(line.__getitem__(0) , " ",line.__getitem__(1)," ",line.__getitem__(2),"\t  \t",line.__getitem__(3)," ",line.__getitem__(4))
       return data


print("--------Task1------")


fileData = KMeans.readingfile("inc_vs_rent.csv","r")

annual_rent_Data =[]
average_SEK_Data=[]
fileData.pop(0)
for data in fileData:
    annual_rent_Data.append(float(data[3]))
    average_SEK_Data.append(float(data[4]))


plt.scatter(annual_rent_Data, average_SEK_Data, color='orange')
plt.show()



