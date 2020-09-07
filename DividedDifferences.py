import matplotlib.pyplot as plt

def proterm(i, value, x): 
  pro = 1; 
  for j in range(i): 
    pro = pro * (value - x[j]); 
  return pro; 

# Function for calculating 
# divided difference table 
def dividedDiffTable(x, y, n): 

  for i in range(1, n): 
    for j in range(n - i): 
      y[j][i] = ((y[j][i - 1] - y[j + 1][i - 1]) /
                  (x[j] - x[i + j])); 
  return y; 

# Function for applying Newton's 
# divided difference formula 
def applyFormula(value, x, y, n): 

  sum = y[0][0]; 

  for i in range(1, n): 
    sum = sum + (proterm(i, value, x) * y[0][i]); 
  
  return sum; 

# Function for displaying divided 
# difference table 
def printDiffTable(y, n): 

  for i in range(n): 
    for j in range(n - i): 
      print(round(y[i][j], 4), "\t", 
              end = " "); 

    print(""); 

# Driver Code 

# number of inputs given 
n = 12; 
y = [[0 for i in range(12)] 
    for j in range(12)]; 
x = [3,7,11,14,17,20,25,30,35,40,42,43]; 

# y[][] is used for divided difference 
# table where y[][0] is used for input
dumb = [1,47,670,1529,3629,9217,20921,38226,61049,82329,90980,95591]
for i in range (len(x)):
   y[i][0] = dumb[i]


# calculating divided difference table 
y=dividedDiffTable(x, y, n); 

# displaying divided difference table 
printDiffTable(y, n); 

# value to be interpolated 
value = 37; 

# printing the value 
print("\nValue at", value, "is", 
    round(applyFormula(value, x, y, n), 2)) 

plt.plot([3,7,11,14,17,20,25,30,35,40,42,43],[1,47,670,1529,3629,9217,20921,38226,61049,82329,90980,95591],color="blue",label="All cases")
plt.plot(37, round(applyFormula(value, x, y, n), 2) , color='blue', marker=6,markerfacecolor='red', label="37th day")
plt.legend()

plt.title("Daily Case Numbers")
plt.xlabel("Day")
plt.ylabel("Cases")
plt.show()
