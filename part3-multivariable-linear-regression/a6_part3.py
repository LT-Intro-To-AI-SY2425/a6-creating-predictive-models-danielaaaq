import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

#imports and formats the data
data = pd.read_csv("part3-multivariable-linear-regression/car_data.csv")
x = data[["miles","age"]].values
y = data["Price"].values


#split the data into training and testing data
xtrain, xtest, ytrain, ytest = train_test_split(x, y, test_size = .2)

#create linear regression model

model = LinearRegression().fit(xtrain, ytrain)

#Find and print the coefficients, intercept, and r squared values. 
#Each should be rounded to two decimal places. 

coef=np.round(model.coef , 2)
intercept = round(float(model.intercept_), 2)
r_squared=round(model.score(x,y),2)

#Loop through the data and print out the predicted prices and the 
#actual prices
print("***************")
print("Testing Results")

predict= model.predict(xtest)

predict=np.around(predict,2)
print(predict)

print("\nTesting Multivariable Model with Testing Data:")
for index in range(len(xtest)):
    actual = ytest[index] # gets the actual y value from the ytest dataset
    predicted_y = predict[index] # gets the predicted y value from the predict variable
    x_coord = xtest[index] # gets the x value from the xtest dataset
    print(f"Miles Driven: {x_coord[0]} Age: {x_coord[1]}Price: {x_coord[2]} Actual: {actual} Predicted: {predicted_y}")