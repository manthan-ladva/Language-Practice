library(ggplot2)
library(ggplot2movies)

p1 <- ggplot(movies, aes(x = rating))

p2 <- p1 + geom_histogram(binwidth = 0.1, aes(fill = ..count..))

p3 <- p2 + xlab('Movies Ratings') + ylab('Count') + ggtitle('Movie Ratings By Manthan')
print(p3)

# 2 -----------------------------------------------------------------------


pl <- ggplot(movies, aes(x = rating)) +
  geom_histogram(binwidth = 0.1, color = 'pink', aes(fill = ..count..)) +
  xlab('Votes') + ylab('Count') + ggtitle('Votings')
pl
