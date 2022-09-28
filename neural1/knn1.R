data = iris
normalise = function(x){
  return((x-min(x))/(max(x)-min(x)))
}

data$Sepal.Length = normalise(data$Sepal.Length)
data$Sepal.Width = normalise(data$Sepal.Width)
data$Petal.Length = normalise(data$Petal.Length)
data$Petal.Width = normalise(data$Petal.Width)

data = data[sample(1:nrow(data)),]
ind=sample(1:nrow(data),size=(0.9*nrow(data)),replace = FALSE)
train_data=data[ind,]
train_label = train_data[,5]
train_data = train_data[,-5]
test_data=data[-ind,]

test_label =test_data[,5]
test_data = test_data[,-5]

model=knn(train_data,test_data,train_label,k=11,6)

predict(model,test_data)

library(gmodels)
CrossTable(model,test)
