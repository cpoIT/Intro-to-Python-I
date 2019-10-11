# For the exercise, look up the methods and functions that are available for use
# with Python lists.

x = [1, 2, 3]
y = [8, 9, 10]

# For the following, DO NOT USE AN ASSIGNMENT (=).

# Change x so that it is [1, 2, 3, 4]
x.append(4)
print(x)

# Using y, change x so that it is [1, 2, 3, 4, 8, 9, 10]
x.extend(y)
print(x)

# Change x so that it is [1, 2, 3, 4, 9, 10]
x.remove(8) # removes the first matched value             O(n)
# del x[4]  # removes by index                           O(1)
# del (x) # removes the entire array
# del x[0:4] # removes indices 0-4 inclusive

# x.pop(4)  # removes by index and returns the value     O(1)
# x.pop() # removes the last value O(1)
print(x)

# Change x so that it is [1, 2, 3, 4, 9, 99, 10]
x.insert(5, 99)
print(x)

# Print the length of list x
print(len(x)) # 7

# Print all the values in x multiplied by 1000
for e in x:
  print(e * 1000)