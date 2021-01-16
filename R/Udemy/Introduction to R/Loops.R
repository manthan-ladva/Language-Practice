for (i in 1:10) {
  print(i)
}

i <-1
while(i>=1){
  print(i)
  i<- i+1
}

for (i in 1:10) {
  if(i%%2 !=0){
    next
  }
  else{
    print(i/2)
  }
}


x<- c(1,5,10,100)
ifelse(x>=1, x**2)