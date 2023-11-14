#  [Matrix]
# 2차원 배열 구 
# 행렬 자료 구의 특징
# 행, 열 의  2차원 배열구조의 객체
# 동일한타ㅂ 의  데이터만 저장 
#  function for createing : matrix(), rbind() , cbind() 
#  function for processing : apply() 


# 벡터 행렬 객체 생성 
#  matrix() 함수에서 c()  함수를 인수로 지정하여 생성 
# c() 함수는 기본적으로 열을 기준으로 matrix() 객체를 생성 
# 6행 1열 
m <- matrix(c(1:6))
m
m23 <-  matrix(c(1:6), nrow=4)
m23

m42 <-  matrix(c(1:6), nrow = 6) 
m42

# 4행 3열 
# 경고 메세지 : 데이터의 길이가 [11]가 행의 개수[4]의 배수가 되지 않습니다. 
# 4행 3열의 값은 시작값인 10이 지정 
m43 <- matrix(c(10:20),nrow = 4)
m43


# column이 몇개 만들어지는지 nrow 를 가지고 산출하는 공식 만들기 
mx <-  matrix(c(1:15), nrow = 2)
mx

# 행 우선 으로 행렬 객체를 생성 
# 행의 값이 채워지고 다음 행으로 이동하여 채움 
m25 <-matrix(c(1:10), nrow = 2, byrow =  T)
m25


# 경고 발생 : data length [10] is not a sub-multiple or multiple of the number of rows [3]
m34 <-  matrix(c(1:10), nrow = 3, byrow = T)
m34


# 0부터 시작 2의 배수로 증가하는 배열 
mt <- seq(2,20,2)
m45ra <- matrix(mt,nrow= 2, byrow =T)
m45ra




