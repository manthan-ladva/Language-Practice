# 1 -----------------------------------------------------------------------

library(dplyr)
library(nycflights13)
head(flights)

#Filter
filter(flights, month == 3, day == 11, carrier == 'AA')

#Slice
slice(flights, 1:10)

#Arrange
arrange(flights, month, year, day, arr_time)
head(arrange(flights, month, year, day, desc(arr_time)))

#Select
head(select(flights, carrier))

#rename
head(rename(flights, mnt=month))

#Distinct it will give unique value
head(distinct(select(flights, arr_time)))

#mutate
head(mutate(flights, new_col = arr_delay - dep_delay))

#transmute
head(transmute(flights, new_col = arr_delay - dep_delay))

#summarise
summarise(flights, avg = mean(air_time, na.rm = T))
summarise(flights, total = sum(air_time, na.rm = T))

#sample_n   it will gives 10 rows randomly
sample_n(flights, 10)

# 2 -----------------------------------------------------------------------


#pipe operator
df <- mtcars
arrange(sample_n(filter(df, mpg>20), size = 5), desc(mpg))

df %>% filter(mpg>20) %>% sample_n(size=5) %>% arrange(desc(mpg))
