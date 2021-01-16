library(ggplot2)
library(dplyr)

batting <- read.csv("Batting.csv")
sal <- read.csv("Salaries.csv")

batting$BA <- batting$H / batting$AB
batting$OBP <- (batting$H + batting$BB + batting$HBP) / (batting$BB + batting$HBP + batting$SF + batting$AB)
batting$X1B <- batting$H - batting$X2B - batting$X3B - batting$HR
batting$SLG <- ((batting$X1B) + (2 * batting$X2B) + (3 * batting$X3B) + (4 * batting$HR)) / (batting$AB)

batting <- subset(batting, yearID >=1985)

combo <- merge(batting, sal, by=c('playerID', 'yearID'))

lost_players <- subset(combo, playerID %in% c('giambja01', 'damonjo01', 'saenzol01'))
lost_players <- subset(lost_players, yearID == 2001)
lost_players <- lost_players[, c('playerID','H','X2B','X3B','HR','OBP','SLG','BA','AB', 'salary')]

combo <- subset(combo, yearID == 2001)

ggplot(combo, aes(OBP, salary)) +
  geom_point(size = 2)

combo <- subset(combo, salary < 8000000 & OBP > 0)
combo <- subset(combo, AB >= 450)

option <- head(arrange(combo, desc(OBP)))
option[, c('playerID', 'OBP', 'AB', 'salary')]
