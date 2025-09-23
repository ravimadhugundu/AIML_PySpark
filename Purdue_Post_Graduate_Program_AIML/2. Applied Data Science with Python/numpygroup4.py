# %% [markdown]
# Generate a matrix that shows daily temperature highs for two cities (City A & City B) over a week. You need to generate a 2D NumPy array named temperatures with shape (7, 2). (temperatures between -10 and 30. 2. Print the average temperature of each city

# %%

import numpy as np
temperatures = np.random.randint(-10, 31, size=(7,2))
cit1average = np.mean(temperatures[0], axis=0)

temperatures
# cit2average =  np.mean(arr1[0:,1])


# %%
average_temperatures = np.mean(temperatures, axis=0)
average_temperatures

cityAAverage = average_temperatures[0]
cityBAverage = average_temperatures[1]
print(f"city a : {cityAAverage} city b : {cityBAverage}")
average_temperatures

# %% [markdown]
# Plot Load num_data.csv file into an array 
# 2. Get the shape 
# 3. Reshape the matrix to a compatible (row,col) 2D matrix. 
# 4. Define a new array that has values from the first array where number <10

# %%
array = np.loadtxt('num_data.csv')
array

# %%
array.shape

# %%
reshapedarray = array.reshape(8,9)
reshapedarray

# %%
filteresarray = array[array<10]
filteresarray

# %% [markdown]
# Define the following array: sales_data = np.array([ [50, 60, 55, 52, 60, 62, 65, 70, 75, 80, 85, 90], # Year 1 
# [95, 100, 110, 105, 115, 120, 125, 130, 140, 150, 160, 170] # Year 2 ]) 
# 2. Calculate total sales of each year 
# 3. Compute the difference in sales between Year 2 and Year 1 for each month.

# %%
sales_data = sales_data = np.array([ [50, 60, 55, 52, 60, 62, 65, 70, 75, 80, 85, 90], # Year 1 
[95, 100, 110, 105, 115, 120, 125, 130, 140, 150, 160, 170]])
# Year 2 ]) 
total_sales_per_year = np.sum(sales_data, axis=1)
total_sales_per_year
                       

# %%


# %%
salesdiff = sales_data[1] - sales_data[0];
salesdiff


