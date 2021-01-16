library(ggplot2)

pl <- ggplot(mpg, aes(x = displ, y = hwy)) +
  geom_point() + coord_cartesian(xlim= c(1,4), ylim = c(15,30))
pl


pl <- ggplot(mpg, aes(x = displ, y = hwy)) +
  geom_point() + coord_fixed(ratio = 10/10)
pl


pl <- ggplot(mpg, aes(x = displ, y = hwy)) +
  geom_point() + facet_grid(.~drv)
pl
