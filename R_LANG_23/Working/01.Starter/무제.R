# R Studio 주석 은 sharp 로 사용 한다. Python 동일 
# 현재 라인 실행 Shortcut : Ctrl + Enter (Mac : Cmd + Enter)
available.packages()
dim(available.packages())
sessionInfo()

# 패키지 설치 
install.packages('stringr')

# 패키지 로드 : 사용 
library(stringr)
# 현재 로드된 패키지 확인 
search()

# 패키지 제거 
remove.packages('stringr')

#데이터 셋 보기 
data()

# 히스토 그램 : 빈도수 
hist(Nile) 

# 히스토 그램 : 밀도 
hist(Nile, freq = F) # frequency : F : False , 

# 분포곡선 (line) 추가 
lines(density(Nile))

# 난수에 대한 히스토 그램 그맂기 
hist(rnorm(20))
# 난수 발생 
rnorm(20)

# 히스토 그램 파일로 저장 
# plot 영역 에 1개 그래프 표시 

par(mfrow=c(1,1)) 
pdf('./Working/s01-hello-hist-1.pdf')
hist(Nile, freq = F)
lines(density(Nile))
dev.off() 

ls()
objects()
rm(objects)
#Vector  
name <- c("Mike","Lucy","Sam")
age <- c(20,25,30)

#2. Array
x <- matrix(c(1,2,3,4), nrow=2, ncol=2)
x
#3.List 리스트 


