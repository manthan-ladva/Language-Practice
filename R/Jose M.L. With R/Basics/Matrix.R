# Lecture 1 ---------------------------------------------------------------

v1 <- c(45,46,47,48,49)
v2 <- c(54,55,56,57,58)

days <- c('Mon','Tue','Wed','Thu','Fri')
vec <- c('v1', 'v2')
stock <- c(v1,v2)

stock.matrix <- matrix(stock, byrow = T, nrow = 2)

colnames(stock.matrix) <- days
rownames(stock.matrix) <- vec

stock.matrix

# Lecture 2 ---------------------------------------------------------------

