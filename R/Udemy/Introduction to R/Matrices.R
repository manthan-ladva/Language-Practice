m <- matrix(nrow = 2, ncol = 2)
m[1,1]<- 1
m[1,2]<- 2
v <- c(3,4)
m[2,]<- v

v1<- c(5,6)
m[1,]<- v1

v1<- 1:5
v2<- 6:10
m1<- rbind(v1,v2)
m1
dim(m1)
m2<- cbind(v1,v2)
m2
dim(m2) #_-_________________ dim() gives the details of row and column in given value
