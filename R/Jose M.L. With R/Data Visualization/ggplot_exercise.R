# 1 -----------------------------------------------------------------------
library(ggplot2)
library(ggthemes)

head(mpg)

pl1 <- ggplot(mpg, aes(x = hwy)) +
  geom_histogram(fill = 'red', alpha = 0.5, bins = 20) +
  theme_wsj()
pl1

# 2 -----------------------------------------------------------------------

pl2 <- ggplot(mpg, aes(x = manufacturer)) + geom_bar(aes(fill= factor(cyl)))
pl2

# 3 -----------------------------------------------------------------------

pl3 <- ggplot(txhousing, aes(x = sales, y = volume)) +
  geom_point(alpha=0.4, fill = 'blue', color = 'blue') +
  geom_smooth(color = 'red')
pl3
