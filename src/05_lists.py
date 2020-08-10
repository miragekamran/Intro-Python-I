# For the exercise, look up the methods and functions that are available for use
# with Python lists.

x = [1, 2, 3]
y = [8, 9, 10]

# For the following, DO NOT USE AN ASSIGNMENT (=).

# Change x so that it is [1, 2, 3, 4]
# YOUR CODE HERE
print(x)

# Using y, change x so that it is [1, 2, 3, 4, 8, 9, 10]
# YOUR CODE HERE
print(x)

# Change x so that it is [1, 2, 3, 4, 9, 10]
# YOUR CODE HERE
print(x)

# Change x so that it is [1, 2, 3, 4, 9, 99, 10]
# YOUR CODE HERE
print(x)

# Print the length of list x
# YOUR CODE HERE

# Print all the values in x multiplied by 1000
# YOUR CODE HERE

# Solution 1:
x_1000 = []
for i in x:
    x_1000.append(i * 1000)
print(x_1000)

# Solution 2:
for i in x:
    print(i * 1000)

# Solution 3:
print([num * 1000 for num in x])