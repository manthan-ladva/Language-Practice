library(ggplot2)
library(ggplot2movies)

# Bin2d -------------------------------------------------------------------


pl <- ggplot(movies, aes(x = year, y = rating)) +
  geom_bin2d() + scale_fill_gradient(high = 'yellow', low = 'blue')
pl


# Hex ---------------------------------------------------------------------


pl <- ggplot(movies, aes(x = year, y = rating)) +
  geom_hex() + scale_fill_gradient(high = 'yellow', low = 'blue')
pl

# Density 2d --------------------------------------------------------------


pl <- ggplot(movies, aes(x = year, y = rating)) +
  geom_density_2d() + scale_fill_gradient(high = 'yellow', low = 'blue')
pl
