# 06장 자유자재로 데이터 가공하기 

# 06-6 파생변수, 추가 하기  
# summarise(), group_by() 

library(dplyr)
library(ggplot2)

exam <- read.csv("../data/csv_exam.csv")
exam

mpg <- as.data.frame(ggplot2::mpg)
head(mpg)

mpg %>% 
  group_by(manufacturer) %>%  #회사별분리 
  filter(class=='suv') %>% #sub 추출  
  mutate(tot=(cty+hwy)/2) %>% # 통합연비평균 변수생성 
  summarise(mean_tot = mean(tot)) %>% #통합연비 평균 산출 
  arrange(desc(mean_tot)) %>% #내림차순 정렬 
  head(5) # 1~5위 출력 

#회사별 , 모델별 그룹 
mpg %>% 
  group_by(manufacturer,model) %>%  #회사별분리 
  filter(class=='suv') %>% #sub 추출  
  mutate(tot=(cty+hwy)/2) %>% # 통합연비평균 변수생성 
  summarise(mean_tot = mean(tot)) %>% #통합연비 평균 산출 
  arrange(desc(mean_tot)) %>% #내림차순 정렬 
  head(20) # 1~5위 출력 

# 회사별 구동방식별 도시 평균 연비 
# drv : 4,f,r 
mpg %>% 
  group_by(manufacturer, drv) %>%  #회사별분리 
  summarise(mean_cty = mean(cty)) %>% #통합연비 평균 산출 
  arrange(desc(mean_cty)) %>% #내림차순 정렬 
  head(5) # 1~5위 출력 
