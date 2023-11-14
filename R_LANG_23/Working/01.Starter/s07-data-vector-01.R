# 데이터 유형과 구조 
# 1.Vector : 1차원 배열 
# 2.Matrix  : 2차원 배월


# [Vector]
# - 1차원 배열 
# - 첨자(index) 는 1 부터 시작 

# combine value 

c1 <- c(1,2,3,4,5)
# 슬라이싱 
c2 <- c(1:5)
c1
c2


# sequence value 
# seq(시작값, 종료값, 증가값 )
# 함수에 파라미터 
help(seq)
s1 <- seq(10)
s2 <- seq(1,10,1) #과 동일 


#1 부터 10까지 홀수 데이터 
ox = seq(1,10,2)
ox

#2부터 10까지 짝수 데이터 
ex = seq(2,10,2)
ex

################################
# 반복 
# replicate value 
# rep(값, 반복횟수)

r1 <- rep(3,5)
r1 

r2 <- rep(2:6,2)
r2

r3 <- rep(c('a', 'c'), 3)
r3

r4 <- rep(1:3, 3)
r5 <- rep(c(1:3),3)
r6 <- rep(c(1,2,3),3
          )
r4 #int
r5 #int
r6 #num 


