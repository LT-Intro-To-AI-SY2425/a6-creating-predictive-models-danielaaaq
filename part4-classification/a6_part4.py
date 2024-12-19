import pandas as pd
from sklearn import linear_model
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

data = pd.read_csv("part4-classification/suv_data.csv")
data['Gender'].replace(['Male','Female'],[0,1],inplace=True)

x = data[["Age", "EstimatedSalary", "Gender"]].values
y = data["Purchased"].values


scaler=StandardScaler().fit(x)
x=scaler.transform(x)
x_train,x_test,y_train,y_test=train_test_split(x,y)

model = linear_model.LogisticRegression().fit(x_train, y_train)

print("score:",model.score(x_test,y_test))


for index in range(len(x_test)):
    x=x_test[index]
    x=x.reshape(-1,3)
    print(x)
    y_pred=int(model.predict(x))

    if y_pred==0:
        y_pred="Male"
    else:
        y_pred="Female"
    
    actual=y_test[index]
    if actual==0:
        actual="Male"
    else:
        actual="Female"
    print("prediction:"+y_pred+" actual:"+actual)
    print("")