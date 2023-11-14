# 문자열 처리 

install.packages('stringr') # 패키지 설치 

library(stringr) # 사용하기  


s1 <-  "문자열입니다."
s1

#논리적인 문자의 길이 
sl <-  str_length(s1)
sl #7 

# 문자열 내에서 문자열의 특정 위치 

sp1 <- str_locate(s1,'열')
sp1

sp2 <- str_locate(s1,"입니다")
sp2 #start : 4, end : 6 
sp2[]

sp2[1,1]  #시작위치 : 4 
sp2[1,2]  #종료위치 : 6  
# 부분 문자열 만들기 

s2 <- str_sub(s1,3,str_length(s1))
s2
# [문제]
# 이메일(abc@syit.ac.kr) 에서 아이디와 주소를 분리 추출 하라 

addr <- c('abc@syit.ac.kr')
addr2 <- c('hotnewton@korea.ac.kr')


addr

il <- str_locate(addr,"@")
il
il[1]
len <- str_length(addr)
len

emailChecker <- function (addr) {
  atlocation <- str_locate(addr,"@")
  
  header <- str_sub(addr,1,atlocation[1,1]-1) 
  domain <- str_sub(addr,atlocation[1,1]+1,str_length(addr)) 
  cat("Email Header : ", header,"\n")
  cat("Domain Name : ", domain )
}

id <- str_sub(addr,1,il[1,1]-1) 
id
domain <-  str_sub(addr,il[1]+1,str_length(addr))
domain

#함수 사용 
checkByEmail(addr2)

#선생님 풀이 

email <-  'abc@ysit.ac.kr'
eloc <-  str_locate(email, '@')
eloc 
estr <- eloc[1,1]
estr
eend <-  eloc[1,2]
eend

elen <- str_length(email)

eid <-  str_sub(email,1,estr-1)
eid

edm <-  str_sub(email,eend+1 , elen)
edm

#소문자를 대문자로 변환 
captial <- str_to_upper(email)
captial

#