v1 <- c(1,2,3)
v2 <- 1:100
m1 <- matrix(nrow = 2, ncol = 2)

l <- list(B_no = v1, S_no = v2, Empty = m1)

df1 <- data.frame(x = c(TRUE, FALSE, TRUE))
l$data <-df1
df1
l
l[[5]] <- df1
