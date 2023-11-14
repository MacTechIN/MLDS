# Local file


url <- "https://vincentarelbundock.github.io/Rdatasets/csv/COUNT/titanic.csv"
#url <- "https://github.com/vincentarelbundock/Rdatasets/blob/master/csv/COUNT/titanic.csv"
titanic <- read.csv(url,header= T)
titanic

#######################
# Read Excel 
# table

tab <-table(titanic$survived, titanic$sex)
tab

barplot(tab, col=rainbow(2), main="Survival ratio against gender type")

install.packages('readxl')
library(readxl)

xl <- read_excel(path = './students.xlsx')
xl

str(xl)
class(xl)
summary(xl)
