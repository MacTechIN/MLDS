# 기본함수 

# 함수 도움말 
# help(함수명)
# ? 함수명 


help(sum)
?sum 



# 함수 파라미터 보기 
# args(함수명)

args(sum)
sum(1,2,3,4,5,NA) #NA
sum(1,2,3,4,5,NA, na.rm = TRUE) #25 

#함수 사용예
example(sum) # sum> sum(1:5, NA, na.rm = TRUE)

#슬라이싱 숫자 다 포함 (파이썬과 다름)
sum(1:5) #15
sum (1:2 , 3:5) #15
sum(1,2,3,4,5) #15 

#현재 작업공간 
getwd() #  "/Users/sl/Workspace/MLDS/R_LANG_23"

#현재 작업 공간 이동 현재 작업위치 이동  
setwd("c:/Temp") 
