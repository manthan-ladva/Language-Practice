
# Lecture 1 ---------------------------------------------------------------

library(ggplot2)
library(ggthemes)
library(dplyr)
library(corrgram)
library(corrplot)

library(caTools)

df <- read.csv('student-mat.csv', sep = ';')
head(df)

num.cols <- sapply(df, is.numeric)
cor.data <- cor(df[,num.cols])
cor.data

corrplot(cor.data, method = 'color')
corrgram(cor.data)#, method = 'color')

corrgram(df,order=TRUE, lower.panel=panel.shade,
         upper.panel=panel.ellipse, text.panel=panel.txt)

ggplot(df,aes(x=G3)) +
  geom_histogram(bins = 20, fill = 'Blue', alpha = 0.5)

# Lecture 2 ---------------------------------------------------------------

set.seed(101)

sample <- sample.split(df$G3, SplitRatio = 0.7)
train <- subset(df, sample == TRUE)                  #-------- This means Train data will go for 70% of total data
test <- subset(df, sample == FALSE)                  #-------- This means Test data will go for 30% of total data

#formula for Linear Model
# model <- lm(y ~ x1+x2, data)
# or
# model <- lm(y ~., data)

model <- lm(G3 ~., data=train)
summary(model)

res <- residuals(model)
res <- as.data.frame(res)
ggplot(res, aes(res)) + geom_histogram(fill = 'pink', alpha=1, bins=30)

# Lecture 3 ---------------------------------------------------------------

plot(model)

G3.predictions <- predict(model, test)
result <- cbind(G3.predictions, test$G3)
colnames(result) <- c('Predicted', 'Actual')
result <- as.data.frame(result)
head(result)

to_zero <- function(x){
  if(x<0){
    return(0)
  }
  else{
    return(x)
  }
}

result$Predicted <- sapply(result$Predicted, to_zero)

#MSE
mse <- mean( (result$Actual - result$Predicted)^2 )
mse

#RMSE
rmse <- mse^0.5
rmse

#SSE & SST
sse <- sum( (result$Predicted - result$Actual)^2 )
sst <- sum( (mean(df$G3) - result$Actual)^2 )
r2 <- 1 - (sse/sst)
r2
