
# Project On Linear Regression  -------------------------------------------
# Editor:- @Manthan Ladva

library(ggplot2)
library(dplyr)

df <- read.csv('bikeshare.csv')
head(df)

#Temp vs Count Graph
ggplot(df, aes(x=temp, y=count)) + 
  geom_point(alpha=0.3, aes(color=temp)) +
  theme_bw()

#Datetime vs Count Graph
df$datetime <- as.POSIXct(df$datetime)

ggplot(df, aes(datetime, count)) +
  geom_point(alpha=0.3, aes(color=temp))

#Correlation between Temperature and Count
cor(df[,c('temp', 'count')])

#BoxGraph of Season vs Count
ggplot(df, aes(factor(season), count)) +
  geom_boxplot(aes(color=factor(season)))

#Feature Enginnering

#Making Hour Column
df$hour <- sapply(df$datetime, function(x){format(x, "%H")})




#Graph of Count vs Hour && Color == Temp                            ####------------1st Way------------####
wd <- subset(df, df$workingday==1)              #---------- For working days
ggplot(wd, aes(hour, count)) +
  geom_point(aes(color = temp), alpha=0.4, position = position_jitter(w=1, h=0)) +
  theme_bw() +
  scale_color_gradientn(colors=c('pink', 'red', 'yellow'))

wd <- subset(df, df$workingday==0)              #---------- For non-working days
ggplot(wd, aes(hour, count)) +
  geom_point(aes(color = temp), alpha=0.4, position = position_jitter(w=1, h=0)) +
  theme_bw() +
  scale_color_gradientn(colors=c('pink', 'red', 'yellow'))




#Graph of Count vs Hour && Color == Temp                            ####------------2nd Way------------####

#---------- For working days
ggplot(filter(df, workingday==1), aes(hour, count)) +
  geom_point(aes(color = temp), alpha=0.4, position = position_jitter(w=1, h=0)) +
  theme_bw() +
  scale_color_gradientn(colors=c('pink', 'red', 'yellow'))


#---------- For non-working days
ggplot(filter(df, workingday==0), aes(hour, count)) +
  geom_point(aes(color = temp), alpha=0.4, position = position_jitter(w=1, h=0)) +
  theme_bw() +
  scale_color_gradientn(colors=c('pink', 'red', 'yellow'))


#-----------------------------------------------------------Linear Model

model <- lm(count ~ temp, df)
summary(model)

#test <- data.frame(temp=c(25))
predict(model, data.frame(temp=c(25)) )

df$hour <- sapply(df$hour, as.numeric)

model2 <- lm(count ~ . -casual -registered -datetime -atemp, df)
summary(model2)
