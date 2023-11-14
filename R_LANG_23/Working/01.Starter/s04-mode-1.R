# 자료형의 성격(Mode)과 구조(class)를 확인 
# mode : 숫자형, 문자형, 논리형 으로 구분 
# class : 배열, 리스트, 테이블 으로 구분 

# 벡터 Vector 변수 : 1차원 배열 

n1 <- 10 
is.numeric(n1)

#Vector 에서 문자형이 섞여 있으면 모든 요소가 문자형으로 변환 된다. 
ns <- c(1,3,5,7,'9')
ns # [1] "1" "3" "5" "7" "9"

is.numeric(ns) #FALSE
is.character(ns) #TRUE


nd <- as.numeric(ns)
nd
is.numeric(nd) #TRUE
is.character(nd) #FALSE

#자료형의 성격(Type)
# mode : 자료의 성격을 알려줌 : 숫자형, 문자형, 논리형, 
mode(ns) #"character"
mode(nd) #"numeric"

class(nd) # "numeric"

# [mode]
# mode : 자료형의 성격을 알려줌 
# 숫자형, 문자형, 논리형 
mode(NA)
mode()
class(NA) 


# [CLASS] 자료구조, 메모리 구조 
# 배열, 리스트, 데이블 
# 

class(n1)
class(ns)
class(nd)
