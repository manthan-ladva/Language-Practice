x <- c(20, 10, 1)

if (x[1] > x[2]){
  if (x[1] > x[3]){
    print(paste(x[1], ' is largest'))
  }else{
    print(paste(x[3], ' is largest'))
  }
}else{
  if (x[2] > x[3]){
    print(paste(x[2], ' is largest'))
  }else{
    print(paste(x[3], ' is lagestr'))
  }
}
