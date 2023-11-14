#  [Matrix]
# 2차원 배열 구 
# 행렬 자료 구의 특징
# 행, 열 의  2차원 배열구조의 객체
# 동일한타ㅂ 의  데이터만 저장 
#  function for createing : matrix(), rbind() , cbind() 
#  function for processing : apply() 

# 3행 4열 


mx <-  matrix(1:12, nrow=3,ncol=4, byrow = T) # 행 우선  
mx <-  matrix(1:12, nrow=3,ncol=4, byrow = F) # 열 우선 
mx

#행렬의 전체 원소 갯수 
length(mx) # 12

# 열의 갯수 
ncol(mx) #4 

# 행의 갯수 
nrow(mx) #3





