import numpy as np

a = np.array([1,2,3])
print(a*2)

print("Hello Git")


import numpy as np

# Take input from user
numbers = input("Enter numbers separated by space: ")

# Convert to numpy array
a = np.array(list(map(int, numbers.split())))

# Operations
double = a * 2
total = np.sum(a)
average = np.mean(a)

# Output
print("Original Array:", a)
print("After Multiplying by 2:", double)
print("Sum:", total)
print("Average:", average)

print("Hello GitHub ")
