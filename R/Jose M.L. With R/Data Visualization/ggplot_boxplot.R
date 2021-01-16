library(ggplot2)

df <- mtcars

pl <- ggplot(df, aes(x = factor(cyl), y = mpg)) +
  geom_boxplot() + coord_flip()
pl


pl <- ggplot(df, aes(x = factor(cyl), y = mpg)) +
  geom_boxplot(aes(fill = factor(cyl))) + theme_dark()
pl
