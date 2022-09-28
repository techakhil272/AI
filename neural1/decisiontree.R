data=iris
ind = sample(1:nrow(data),0.9*nrow(data),replace=FALSE)
train_data = data[ind,]
test_data = data[-ind,]
test_label = test_data[,5]
test_data = test_data[,-5]

install.packages("party")
model = ctree(Species~.,train_data)
plot(model)
install.packages("rpart")
model1=rpart(Species~.,train_data,minsplit=2,cp=0.0001)
install.packages("rattle")

fancyRpartPlot(model1)