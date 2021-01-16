v1<- c(45,75,70,85,90,99)
v2<- c('A','A','C','A','A+', 'B')
v3<- c(TRUE,TRUE,TRUE,TRUE,TRUE, TRUE)

df1<- data.frame(Percent=v1, Grade=v2, Pass_Fail = v3)
df1
df1$Percent

df1$Grade[df1$Percent < 50] <-'F'
df1$Grade[df1$Percent >= 75] <-'B'
df1$Grade[df1$Percent >= 90] <-'A+'

df1$Pass_Fail[df1$Percent < 50] <- FALSE
df1$Pass_Fail[df1$Percent > 50] <- TRUE
df1

df1$Name <- c('Jack', 'Maddy', 'Arora', 'Shweta', 'Jinal', 'Manthan')
df1
