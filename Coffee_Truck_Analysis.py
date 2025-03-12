#Import Modules
import pandas as pd
import os

# Change the file path to where the data is located on your device
os.chdir(r"C:\Users\kutlw\.spyder-py3\CoffeeTruckAnalysis")

#Read the dataset
coffee = pd.read_csv("CoffeeTruck.csv")

#How many rows and columns does the dataset have
# Obtain the number of observations
coffee.shape[0]

# Obtain the number of columns
coffee.shape[1]

#List all the variables in the data set.
list(coffee)

#Find the unique values in the 'Location' variable. How many unique locations are present in the dataset?
location_types = coffee["Location"].unique()

#Subset the data to include only the observations of sales at the Zoo
coffee_sales_at_zoo = coffee.loc[coffee["Location"] == "Zoo", :]

#How many duplicated rows are there in the data? Remove all the duplicated rows from the data set.How many rows are left in the data set
# Print all the duplicated rows
duplicates = coffee.duplicated(keep = False)
dups = coffee[duplicates]

# Remove the duplicated rows (but one of the rows should be kept in the 
# data frame)

no_dups = coffee.drop_duplicates(keep = "first")

#Sort the data set first by profit made (from smallest to largest) and then by music played (from Z to A).(Make use of the data set where the duplicates are removed)
coffee_Profit = coffee.sort_values(by=['Profit'])
coffee_Profit2 = no_dups.sort_values(by=['Profit'])
# Sort the dataset by "TopSpeedReached" in ascending order and then by 
# "FinishTime" in descending order.
racing_sorted2 = racing.sort_values(by=['TopSpeedReached', 'FinishTime'],
                                    ascending=[True, False])
