# 06장 자유자재로 데이터 가공하기 

# 06-1 데이터 전처리 - 원하는 형태로 데이터 가공

library(dplyr)

exam <-  read.csv("../00.Data/csv_exam.csv")
exam


# exam에서 classrk 1인 경우만 추출하여 출력 
# 파이프 라인 : %>% 
# exam 을 filter() 함수에 연결 

exam %>% filter(class ==1)
# 동일 : filter(exam, class ==1)

exam %>% filter(class==2)

#filter(exam, class!=1)
exam %>% filter(class==1 & class==2)

exam %>% filter(class!=3)

exam %>% filter(english>70 & math>70 & science > 70)

exam %>% filter(math < 60 | english < 60 | science < 60)



s = exam %>% filter(class ==1 | class==3 | class==5) 

s = exam %>% filter(class %in% c(1,3,5))

# class (1,3,5) 학생의수 
nrow(s) # row : 12
length(s) # column : 5
s_dim <- dim(s)
s_dim[1]
s_dim[2]


