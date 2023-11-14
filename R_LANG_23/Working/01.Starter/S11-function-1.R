# 함수정ㅢ 
# 함수명 <-function(매개변수) {

# }

#함수 : 인자없는 함수 

f1 <- function() {
  print('function : f1()')
  cat("매개변수와 리턴값이 없는 함수'")
}

f1()

#함수정의 인자와 리턴값이 있는 함수 
add <- function(x,y) {
  z <- x+y
  return(z) # () 사용 한다. 
}

#함수호출 
add(10,20)

