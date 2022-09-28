data =iris
data

normalise = function(x){
  return(x-min(x))/(max(x)-min(x))
}

data$Sepal.Length = normalise(data$Sepal.Length)
data$Sepal.Width = normalise(data$Sepal.Width)
data$Petal.Length = normalise(data$Petal.Length)
data$Petal.Width = normalise(data$Petal.Width)

?sample
m=sample(1:nrow(data),size=(0.9*nrow(data)),replace = FALSE)

train_data = data[m,]
train_data

test_data = data[-m,] #remains of 90% i.e 10%
test_data

train_label = train_data[,5]
train_data = train_data[,-5]

test_label = test_data[,5]
test_data = test_data[,-5]

library(class)
?knn
model = knn(train_data, test_data, train_label, k=11, 6)

library(gmodels)
?CrossTable
CrossTable(model,test_label)
