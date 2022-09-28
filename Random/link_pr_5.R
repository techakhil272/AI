data = read.csv("C:/Users/steph/OneDrive/Documents/kmeans.csv")
data

data = data[,-1]

?dist
distance = dist(data,method = "manhattan")

?hclust
model = hclust(distance, method = "average")
model$merge

plot(model,hang = -1)

?sparcl
model2 = cutree(model,3)
model2
ColorDendrogram(model,model2,branchlength = 10)

