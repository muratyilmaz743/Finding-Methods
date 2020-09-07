
import numpy as np
from scipy import linalg
import matplotlib.pyplot as plt

t = np.array([3,7,11,14,17,20,25,30,35,40,42,43])

vt = np.array([1,47,670,1529,3629,9217,20921,38226,61049,82329,90980,95591])

x = np.zeros((len(t),len(t)))
desired = 37

for i in range (len(t)):
    for a in range (len(t)):
        x[i][a]=t[i]**a

y=linalg.solve(x,vt)

exam=0

for i in range (len(y)):
  exam += y[i]*(desired**i)

print(exam,"this is our guess for the 37. days total")

plt.plot([3,7,11,14,17,20,25,30,35,40,42,43],[1,47,670,1529,3629,9217,20921,38226,61049,82329,90980,95591],color="blue",label="All cases")

plt.plot(37, exam, color='blue', marker=6,markerfacecolor='red', markersize=12,label="37th day")
plt.legend()

plt.title("Daily Case Numbers")
plt.xlabel("Day")
plt.ylabel("Cases")
plt.show()
