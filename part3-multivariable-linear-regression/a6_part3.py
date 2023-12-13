import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

#imports and formats the data
data = pd.read_csv("part3-multivariable-linear-regression/car_data.csv")
x = data[["miles(000)","age"]].values
x_1=data["miles(000)"]
x_2=data["age"]
y = data["Price"].values

#split the data into training and testing data
xtrain, xtest, ytrain, ytest= train_test_split(x,y, test_size=.2)

#create linear regression model
model=LinearRegression().fit(xtrain,ytrain)

#Find and print the coefficients, intercept, and r squared values. 
#Each should be rounded to two decimal places. 
coef=np.around(model.coef_,2)
intercept=round(float(model.intercept_),2)
r_squared=round(model.score(x,y),2)

#Loop through the data and print out the predicted prices and the 
#actual prices
print("***************")
print("Testing Results")


# get the predicted y values for the xtest values - returns an array of the results
predict = model.predict(xtest)
# round the value in the np array to 2 decimal places
predict = np.around(predict, 2)
print(predict)

# compare the actual and predicted values
print("\nTesting Multivariable Model with Testing Data:")
for index in range(len(xtest)):
    actual = round(ytest[index]) # gets the actual y value from the ytest dataset
    predicted_y = predict[index] # gets the predicted y value from the predict variable
    x_coord = xtest[index] # gets the x value from the xtest dataset
    x_coord=np.around(x_coord,2)
    # print(f"miles(000): {x_coord[0]} age: {x_coord[1]}  Actual: {actual} Predicted: {predicted_y}")
    # print(f"miles(000): {89} age: 10 Actual:{actual} Predicted: {predicted_y})
    print(f"miles(000): {150} age: {20}  Actual: {actual} Predicted: {predicted_y}")
    print("R Squared value:", r_squared)