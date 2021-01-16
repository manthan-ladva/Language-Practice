v1 <- c(9,8,7)
v2 <- c(4,5,6)
v3 <- c(v1, v2)
v3

v4 = c(c(45,46,47), c(78,77,79))
v4

v5 = c(1, 'M')
v5

v6 <- c(1, TRUE, 'M')
v6

v7 <- seq(9)
seq(from=5, to=100, by=5)
seq(from=1, to=100, length.out =3)

rep(9, times= 5)
rep('Manthan', times = 9)
rep(c(1,2,3), times = 3, each = 3)

v45 <- rnorm(10, mean = 0, sd = 1)
v45

v98 <- 1:100
sample1 <- sample(v98, size = 10, replace = FALSE)
sample1


a1 <- 1:5
a2 <- 1:5
a3 <- a1+a2
a3


a1<- 1:5
a2<- c(1,2,3)
a3<-a1+a2


a1<- c(1,2,3,4,NA)
sum(a1)
a1 <- sum(a1, na.rm = TRUE)


a2 <- c(TRUE, TRUE, FALSE)
sum(a2) / length(a2)

grades<- c(75,80,85,90,60)
filter<-grades>75
grades[filter]
grades[grades > 80 | grades < 75]
grades[grades > 75 & grades < 90]

student <- c('Jinal', 'Manthan', 'Shweta', 'Ojaswini')
top <- c('Jinal', 'Manthan')
is.element(student, top)
union(student, top)
intersect(student, top)
setequal(student, top)
setdiff(student, top)
all(grades>90)
