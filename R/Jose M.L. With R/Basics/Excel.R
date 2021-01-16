a <- c(9,8,7)

if (a[1] > a[2]){
  fir <- a[1]
  sec <- a[2]
}else{
  fir <- a[2]
  sec <- a[1]
}

if (a[3] > fir & a[3] > sec){
  thi <- sec
  sec <- fir
  fir <- a[3]
}else if (a[3] < fir & a[3] < sec){
  thi <- a[3]
}else{
  thi <- sec
  sec <- a[3]
}



cat(fir, sec, thi)


#a>c, b>c
#a<c, b<c
#a>c, b<c
#a<c, b>c
