
  
# To represent a data point corresponding to x and y = f(x) 
import matplotlib.pyplot as plt
import numpy as np
class Data: 
    def __init__(self, x, y): 
        self.x = x 
        self.y = y 
  
# function to interpolate the given data points 
# using Lagrange's formula 
# xi -> corresponds to the new data point 
# whose value is to be obtained 
# n -> represents the number of known data points 

def interpolate(f: list, xi: int, n: int) -> float: 
  
    # Initialize result 
    result = 0.0
    for i in range(n): 
  
        # Compute individual terms of above formula 
        term = f[i].y 
        for j in range(n): 
            if j != i: 
                term = term * (xi - f[j].x) / (f[i].x - f[j].x) 
  
        # Add current term to result 
        result += term 
  
    return result 
  
# Driver Code 
if __name__ == "__main__": 
  
    # creating an array of 12 known data points 
    

    f = [Data( 3 , 1 ),Data( 7 , 47 ),Data( 11 , 670 ),Data( 14 , 1529 ),
         Data( 17 , 3629 ),Data( 20 , 9217 ),Data( 25 , 20921 ),
         Data( 30 , 38226 ),Data( 35 , 61049 ),Data( 40 , 82329 ),
         Data( 42 , 90980 ),Data( 43 , 95591 )] 
    
    
    # Using the interpolate function to obtain a data point 
    # corresponding to x=50 
    print("Value of f(37)+ is :", interpolate(f, 37, 12)) 

plt.plot([3,7,11,14,17,20,25,30,35,40,42,43],[1,47,670,1529,3629,9217,20921,38226,61049,82329,90980,95591],color="blue",label="All cases")
plt.plot(37, interpolate(f, 37, 12), color='blue', marker=6, markerfacecolor='red', label="37th day")
plt.legend()

plt.title("Daily Case Numbers")
plt.xlabel("Day")
plt.ylabel("Cases")
plt.show()
