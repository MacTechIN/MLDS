# Factor : 요인형 
# 성격이 비슷한 값의 묶음 
#  - Nominal : 범주의 순서는 알파벳 순서로 정렬 
#  - Ordinal : 범주의 순서는 사용자가 지정한 순서대로 정렬 


gender <-  c('남자','여자',"여자",'남자','남자',"중성")
gender


#Factor Nominal 
# 알파벳 순서로 정렬 

ng <- as.factor(gender)
ng
# [1] 남자 여자 여자 남자 남자
# Levels: 남자 여자

# 빈도수 
table(ng)

#그래프 그리기 
par(family="AppleGothic")
plot(ng)

#  자료형 
mode(ng)
class(ng)
is.factor(ng) # T
as.integer(ng) 

#####################
# Factor Ordinal 
# 범주의 순서는 사용자가 지정한 순서대로 정렬 
# factor() 함수 
# 
args(factor)
on <- factor(gender, levels = c("여자","중성","남자"), ordered = T)
on

table(on)
plot(on)

# 남자 여자 여자 남자 남자 중성 
as.integer(on) #3 1 1 3 3 2

#
par(mfrow= c(1,2))
plot(on) # 여자, 중성, 남자 
plot(ng) # 남자, 여자, 중성 

