library(ggplot2)

df <- mtcars

pl <- ggplot(df, aes(x = wt, y = mpg))

pl+ geom_point(aes(shape = factor(cyl), color = factor(cyl)), size = 5, alpha = 0.4)


pl+ geom_point(aes(color = hp), size = 5) + scale_color_gradient(low = 'red', high = 'yellow')
