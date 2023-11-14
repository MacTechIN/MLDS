# [Data type] 
# 3 Main Data types with 결측 
# Numeric  : 0, 123, -1234 
# String : 'a' , 'test'
# Logical : TRUE, FALSE, T,F
# 결측 (Missing Value) :  NA(Not a available) , Nan(Not a Number)
# Infinitive : INf, -Inf 
# None excist Value : NULL


n <- 20 
n
s <- '이시웅'
s
s1 <- "전현진"
s1 
s1 <- 2 
s1

# Logical data type 
t = T
f = F
bt = TRUE
bf = FALSE
# 단축형 shrink 
t
f

# Sumerize function
sum(1,3,5,7,9)
sum(2,4,6,8,NA) # included missing Data , result is NA (Can not calculate it) 
sum(2,4,6,8,NA,na.rm=T) # 결측값을 제외 시켜라 : 20 
sum(2,4,6,8,F) # 20 , T:1 , F:0
sum(-T)
sum(-F)

# Show current using variables 
#list 
ls()

# Type of Data type 
# Result : TRUE, FALSE 
# 변수의 자료 형이 문자인지 검사 , Checking data type for VAR 
is.character(n) # FALSE
is.character(s) # TRUE  

is.numeric(n)
n
is.numeric(s)
s
# 변수의 자료형이 논리형인지 검사 
is.logical(f) # TRUE
is.logical(n) # FALSE 
is.logical(T)

class(n)

