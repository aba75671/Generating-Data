import matplotlib.pyplot as plt

""" x_values = [1, 2, 3, 4, 5]
y_values = [1, 4, 9, 16, 25]

plt.style.use('seaborn')
fig, ax = plt.subplots()
# s is the size of the dots
ax.scatter(x_values, y_values, s=10)

# set chart title and label axes
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# set size of tick labels
ax.tick_params(axis='both', which='major', labelsize=14)

plt.show() """

# Code for 1000 points with loop for y_values
x_values = range(1, 1001)
y_values = [x**2 for x in x_values]

plt.style.use('seaborn')
fig, ax = plt.subplots()
# larger data set so smaller dot size
# can use color as string or RGB value as c=(0, 0, 0)
# ax.scatter(x_values, y_values, c='red', s=10)

# colormap for gradient to emphasis pattern in data
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10)

# set chart title and label axes
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# specifying the range of each axis
ax.axis([0, 1100, 0, 1100000])

# plt.savefig('square_plot.png', bbox_inches='tight') to save
plt.show()