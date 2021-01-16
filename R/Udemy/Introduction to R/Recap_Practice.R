library(ggplot2)
library(plotly)
library(htmlwidgets)

cars_data <- mtcars
str(cars_data)

plot(cars_data$disp, cars_data$wt)

disp_gg_reg <- lm(data = cars_data, formula = disp~wt)
disp_gg_reg

pdf(file = 'disp.pdf')
plot(cars_data$disp, cars_data$wt)
dev.off()

disp_gg <- ggplot(data = cars_data, aes(x=cars_data$disp, y=cars_data$wt))+
  geom_point()+
  geom_smooth(method = 'lm')+
  ggtitle('Disp_GG')
disp_gg

disp_gg_interactive <- ggplotly(disp_gg)
disp_gg_interactive

saveWidget(disp_gg_interactive, file = 'disp_gg_interactive.html')
