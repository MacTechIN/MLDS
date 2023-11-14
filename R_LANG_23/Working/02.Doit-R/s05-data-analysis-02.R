# 05장


exam  <- read.csv("../00.Data/csv_exam.csv") 

head(exam,10)
tail(exam,10)
View(exam) #전체 보여줌, Sorting 가능 
edit(exam) #extra windows

dim(exam) # 20  5 (Row, Columns)
str(exam)
summary(exam)


##########02.###################################################
## Fuel economy data from 1999 to 2008 for 38 popular models of cars 
install.packages("ggplot2")

mpg <-  as.data.frame(ggplot2::mpg)
View(mpg)
help(mpg) #?mpg 동일 
dim(mpg)
str(mpg)
summary(mpg)


##
round(mean(mpg$cty),2) # 16.86 (Summary 수치와 동일)
round(mean(mpg$hwy),2) # 23.44 (Summary 수치와 동일)


