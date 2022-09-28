#Method 1: party package
data=iris
set.seed(125) #fixed output every time
ind=sample(1:nrow(data),size=0.95*nrow(data),replace=FALSE) #random output everytime
train_data=data[ind,]
test_data=data[-ind,]
test_label=test_data[5,]
test_data=test_data[-5,]
library(party) #library of package party
?ctree #document
model=ctree(Species~.,train_data) #ctree decision tree algo
plot(model)
ans=predict(model,test_data)

?rpart
model1 = rpart(Species~.,train_data)
model2=rpart(Species~.,train_data,minsplit=20,cp=0.001)
library(rattle)
fancyRpartPlot(model2)
