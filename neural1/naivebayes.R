data = iris
set.seed(125)
?set.seed
data
ind = sample(1:nrow(data),size = 0.9*nrow(data),replace=FALSE)
train_data = data[ind,]
test_data = data[-ind,]
test_label = test_data[,5]
test_data = test_data[,-5]

model=naiveBayes(Species~.,train_data)

predict(model,test_data)
library(gmodels)
table(predict(model,test_data),test_label)
