
# Lecture 1 ---------------------------------------------------------------

library(Amelia)
library(ggplot2)
library(dplyr)

train <-read.csv('titanic_train.csv')
head(train)
str(train)

missmap(train, main='Missing Map', col = c('Yellow', 'Black'), legend = F)

ggplot(train, aes(Survived)) +
  geom_bar(aes(fill=factor(Survived)))

ggplot(train, aes(Pclass)) +
  geom_bar(aes(fill=factor(Pclass)))

ggplot(train, aes(Sex)) +
  geom_bar(aes(fill=factor(Sex)))

ggplot(train, aes(Age)) +
  geom_histogram(alphs=0.4, fill='orange', bins=20)

ggplot(train, aes(SibSp)) +
  geom_bar()

ggplot(train, aes(Fare)) +
  geom_histogram(fill='green', color='black', alpha=0.3)

ggplot(train, aes(Pclass, Age)) +
  geom_boxplot(aes(group=Pclass, fill=factor(Pclass), alpha=0.4)) +
  scale_y_continuous(breaks = seq(min(0), max(80), by=2)) +
  theme_bw()

impute_age <- function(age,class){                    #--------------------Function
  out <- age
  for (i in 1:length(age)){
    
    if (is.na(age[i])){
      
      if (class[i] == 1){
        out[i] <- 37
        
      }else if (class[i] == 2){
        out[i] <- 29
        
      }else{
        out[i] <- 24
      }
    }else{
      out[i]<-age[i]
    }
  }
  return(out)
}

fixed.ages <- impute_age(train$Age,train$Pclass)
train$Age <- fixed.ages
missmap(train, main='Train data', col=c('yellow', 'black'), legend = F)

train <- select(train, -PassengerId, -Name, -Ticket, -Cabin)
train

train$Survived <- factor(train$Survived)
train$Pclass <- factor(train$Pclass)
train$Parch <- factor(train$Parch)
train$SibSp <- factor(train$SibSp)

log.model <- glm(Survived ~. , family = binomial(link = 'logit'), data=train)
