# Naming Style
v1 <- 1:5
v2 <- c(1,2,3)          #-------- c() is a function which combine/concate vectors
v8<- c(1, TRUE)
v7<-c(1, FALSE)

str(v1)          #--------It is a structure function which gives structure of given object

v3 <- seq(9)          #-------- seq() name as sequence function. This function give the sequence from 1 to the no which is passed in it
seq(from=5, to=100,by=5)
seq(from=1, to=100,length.out = 5)

rep(9, timees=5)          #-------- rep() function is used to repeate the value given to it
rep(c(1,2,3), times=5, each=3)

v9 <- rnorm(10, mean=0, sd=1)          #-------- It will give 10 observation

v1<- 1:100
sample1 <- sample(v1, size = 10, replace = FALSE)          #-------- Sample() is a function which will give rnadom number from the given value
sample1

a1<-1:5
a2<-1:6
a3 = a1+a2
a3

a1<-1:5
a2<-c(1,2,3)
a3<-a1+a2

a1<-c(1,2,3,4,NA)
sum(a1, na.rm = TRUE)

v1<- c(TRUE, TRUE, FALSE)          #-------- True = 1, False = 0
sum(v1)

v1<-1:10
v1[c(1,3,5)]
v1[2:5]
v1[-1]
v1[-8]

b1<- rep(TRUE, 5)
b2<-rep(FALSE, 5)
b3<- c(b1,b2)
b3

v1[b3]

grades<- c(70,75,80,85,90,95)
grades[grades > 75]
grades[grades > 75 | grades<75]
grades[grades > 75 & grades<90]

student <- c('Jinal', 'Manthan', 'Shweta', 'Ojaswini')
top <- c('Jinal', 'Manthan')
is.element(student, top)
union(student, top)
intersect(student, top)
setequal(student, top)
setdiff(student, top)
all(grades > 69)

m3 <- matrix(nrow = 2, ncol = 2)
v1<- c(1,2)
v2<- c(3,4)
m3[1,]<-v1 
m3[2,]<- v2

m4 <- matrix(nrow = 2, ncol = 2)
v1<- c(1,2)
v2<- c(3,5)
m4[1,]<-v1 
m4[2,]<- v2

v1<- 1:10
v2<- 2:11
rbind(v1,v2)
cbind(v1,v2)

dim(m4)
dim(cbind(v1,v2))
