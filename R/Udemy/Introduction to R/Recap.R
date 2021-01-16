library(ggplot2)
library(plotly)
library(htmlwidgets)

cars_data <- mtcars

plot(cars_data$mpg, cars_data$hp)

mpg_hp_reg <- lm(data = cars_data, formula = mpg ~ hp)

pdf(file='mpg_hp_reg.pdf')
plot(cars_data$mpg, cars_data$hp)
dev.off()

mpg_hp_reg_gg <- ggplot(data = cars_data, aes(x=mpg, y=hp)) + 
  geom_point()+
  geom_smooth(method = 'lm')+
  ggtitle("Hp vs Mpg ggplot")

mpg_hp_reg_gg

mpg_hp_reg_gg_interactive <- ggplotly(mpg_hp_reg_gg)
mpg_hp_reg_gg_interactive

saveWidget(mpg_hp_reg_gg_interactive, file = 'mpg_hp_reg_gg_interactive.html')
s