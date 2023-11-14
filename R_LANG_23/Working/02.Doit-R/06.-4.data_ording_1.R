# 06장 자유자재로 데이터 가공하기 

# 06-4 순서대로 정렬하기 
# arrange() 함수 

library(dplyr)

exam <- read.csv("../data/csv_exam.csv")
exam

#오름차순 정렬(sort)
exam %>% arrange(math)

# 내림 차순 정렬(sort) :desc(column)
exam %>% arrange(desc(math))
exam %>% arrange(math,class)


#수학점수 상위10명  높은점수 순 
exam %>% arrange(desc(math)) %>% head(10)
