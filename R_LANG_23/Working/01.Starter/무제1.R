# Local file 

# read.table() 
# 칼럼: 공백, 탭, 콜론(:), 세미콜론(;), comma(,) 등으로 구분된 자료를 읽음 

#옵션 : header=FALSE, sep=""

student <- read.csv(file='./students.csv')
student
edit(student)

