# 1 -----------------------------------------------------------------------

hello <- function(name){
  print(paste('Hello', name))
}
hello('Manthan')

# 2 -----------------------------------------------------------------------

pro <- function(a,b){
  result <- a*b
  print(result)
}
pro(5,10)

# 3 -----------------------------------------------------------------------

numw <- function(num,v){
  for (i in v){
    if (i == num){
      return(T)
    }
  }
  return(F)
}

numw(2,c(1,2,3))

# 4 -----------------------------------------------------------------------
nume <- function(num, v){
  count <- 0
  for (i in v){
    if (i == num){
      count <- count + 1
    }
  }
  print(count)
}
nume(2, c(1,2,4,2,2,2,4,5,6,2,2))

# 5 -----------------------------------------------------------------------

summer <- function(a,b,c){
  out <- c(0)
  if (a%%3 != 0){
    out <- append(a, out)
  }
  
  if (b%%3 != 0){
    out <- append(b, out)
  }
  
  if (c%%3 != 0){
    out <- append(c, out)
  }
  print(sum(out))
}
summer(7,2,3)

# 6 -----------------------------------------------------------------------

prime_check <- function(num){
  if (num == 2){
    return(T)
  }
  for (x in 2:(num-1)){
    if (num%%x == 0){
      return(F)
    }
  }
  return(T)
}

prime_check(45)
