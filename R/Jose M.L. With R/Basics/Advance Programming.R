
# 1 -----------------------------------------------------------------------

seq(0, 100, by = 10)

v <- c(4,5,1,2,8,7,12,454)
sort(v)

rev(1:10)

str(1:10)

a <- append(v, 1:10)
a

is.vector(a)

as.list(a)

# 2 -----------------------------------------------------------------------

#Sample
sample(1:100,5)

#Lapply-Sapply
v = 1:5
addrand <- function(x){
  ran <- sample(1:100, 1)
  return(x+ran)
}

result <- lapply(v, addrand)                ##############   will give list in returning
print(result)

result <- sapply(v, addrand)                ##############   will give normal vector in returning
print(result)

#Anonymous Function
v <- 1:5
sapply(v,function(x){x*2})

#Multiple Input
v = 1:5
and <- function(x, ran){
  return(x+ran)
}

result <- sapply(v, and, ran = 10)
print(result)

# 3 -----------------------------------------------------------------------

v <- 'Hey its Manthan, The man who do not know introduction'
v
grepl('not', v)
v <- c('a', 'b', 'c', 'a')
grep('a', v)

# 4 -----------------------------------------------------------------------

Sys.Date()

my.date <- as.Date("Nov-03-73", format = "%b-%d-%y")
my.date

as.POSIXct("04:15:20", format = "%H:%M:%S")

