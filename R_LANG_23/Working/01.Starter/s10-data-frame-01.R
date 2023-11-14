# DataFrame
#  - 데이터 베이스의 테이블 구조 
# - 칼럼 단위로 처리 
# - 리스트와 벡터의 혼합 
# - 칼럼은 리스트 
# - 칼럼 내의 데이터는 벡터 자료구조


# 벡터를 이용한 데이터프레임 생성 

no <- c(1,2,3)
name <- c('kim','lee','jang')
pay <- c(150,300,400)
emp <- data.frame(No=no, Name=name, Pay=pay)

# 데이터프레임$칼럼 (참조하기)
emp$No
emp$Name
emp$Pay

str(emp)

ncol(emp) # 3
nrow(emp) # 3 

#칼럼명 
names(emp)

