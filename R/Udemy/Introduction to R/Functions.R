simpleFunction <- function(){
  print('Hello World')
}

areaOfCricle <- function(radius){
  area<- pi*radius*radius
  return(area)
}

circle<- function(radius=1){
  area<- pi*radius*radius
  circum<- 2*pi*radius
  result <- list(Area=area, Circumference=circum)
  return(result)
}

out_circle<-circle(10)
out_circle$Area
out_circle$Circumference
