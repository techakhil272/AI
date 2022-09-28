data = read.csv("C:/Users/steph/OneDrive/Documents/kmeans.csv")
data
data = data[,-1]
data
?kmeans

model = kmeans(data,2)
model
plot(data,col=model$cluster)
ind = which(model$cluster==1)
ind
cl = data[ind,]
cl
