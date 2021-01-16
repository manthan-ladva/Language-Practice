# Lecture 1 ----------------------------------------------------------------

days <- c('Mon', 'Tue', 'Wed', 'Thurs', 'Fri')
temp <- c(21,22,45,29,25)
rain <- c(T,F,T,T,F)
df <- data.frame(days,temp,rain)

subset(df, subset = temp>=24)


# Lecture 2 ---------------------------------------------------------------

c1 <- 1:10
c2 <- letters[1:10]
df2 <- data.frame(col.names.1 = c1,col.names.2 = c2 )

nrow(df2)
ncol(df2)

colnames(df2)
rownames(df2)

df2[5,2]
df2[5, 'col.names.2']

df2[2,'col.names.2'] <- 'b'
df2

df2[2, 'col.names.1'] <- 999

df3 <- data.frame(col.names.1 = 11, col.names.2 = 'new')
df3

dfnew <- rbind(df2, df3)
dfnew

df2
df2$col.names.3 <- df2$col.names.1 * 2
df2
