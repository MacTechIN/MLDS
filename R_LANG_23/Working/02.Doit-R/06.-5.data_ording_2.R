# 06장 자유자재로 데이터 가공하기 

# 06-4 순서대로 정렬하기 
# arrange() 함수 

library(dplyr)

exam <- read.csv("../data/csv_exam.csv")
exam

#종합 변수 추가 
exam %>% mutate(total = math + english + science)

# 종합, 평균 추가 
exam %>% 
  mutate(total = math+english+science, mean = (math+english+science)/3)
exam_test <- exam %>% 
  mutate(mean= (math+english+science)/3) %>% 
  mutate(test = ifelse(mean >=60, '합격','불합격'))
table(exam_test$test)

exam %>% 
  mutate(mean= (math+english+science)/3) %>% 
  mutate(test = ifelse(mean >=60, '합격','불합격')) %>% 
  select(test) %>% 
  table()

