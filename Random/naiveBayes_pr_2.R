data =iris
data

?sample
ind =sample(1:nrow(data),size=(0.9*nrow(data)),replace = FALSE)

train_data = data[ind,]
test_data = data[-ind,]
model = naiveBayes(Species~.,train_data)

test_label = test_data[,5]
test_data = test_data[,-5]
library(e1071)
?naiveBayes

predict(model,test_data)
table(predict(model,test_data))

library(gmodels)
#calculating efficiency of the model
CrossTable(predict(model,test_data),test_label)
