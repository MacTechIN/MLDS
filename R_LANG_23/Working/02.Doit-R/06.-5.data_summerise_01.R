# 06장 자유자재로 데이터 가공하기 

# 06-6 파생변수, 추가 하기  
# summarise(), group_by() 

library(dplyr)

exam <- read.csv("../data/csv_exam.csv")
exam


#집단별 요약 
mean(exam$math)
exam %>% mutate(mean_math=mean(math))

exam %>% summarise(mean_math=mean(math))

# 그룹단위 집단별 요약 
exam %>% 
  group_by(class) %>% 
  summarise(mean_math = mean(math), sum_math = sum(math), median_math = median(math))
