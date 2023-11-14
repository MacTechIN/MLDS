# 문자열 처리 

install.packages('stringr') # 패키지 설치 
library(stringr) # 사용하기  

# 문자열 고체 
tel <-  "010-1234-5678"


#처음 찾은 문자열을 교체 
tel = str_replace(tel, "-", ".")
str_replace(tel,"-",".")

#문자열 교체 2
rid <-"123456-1234567"

#처음 찾은 문자를 교체 
str_replace(rid,'-', '.')

# 문자열 결합 
helloword  <- str_c("hello", " ", "world")
helloword

# 문자 분활 
str_split(helloword, " ")
# [문제]
# 전화번호("010-1234-5678)의 '-' 를 "."로 변경하라 
# 결과 : "010.1234.5678"

tel <- "010-1234-5678"
tel

tel1 <-  str_replace(tel,"-",".")
tel1

tel2 <- str_replace_all(tel,"-",".")
tel2

sl = str_locate_all(tel,'-')
class(sl)

f1 = sl[[1]][1,1]
f2 = sl[[1]][2,1]


first = str_sub(tel,1,f1-1)
first

middle = str_sub(tel, f1+1,f2-1)
middle

end = str_sub(tel,f2+1,str_length(tel))
end
############################

tel <- "010-1234-5678"

stel <- str_split(tel,'') 
stel
ptel = pastel(stel,collapse='.') 
rtel
###

vtel <- unlist(strsplit(tel,''))
vtel

vlen <- str_length(tel)
vlen
for (n in seq(vlen)) {
  if (stel[n] == "-") {
    stel[n]='.'
  }
}

vtel

###############################

tlen <-  length(stel)
###########################################################

# [문제1] 벡터 n개를 만들고 홀수의 합과 짝수의 합을 각각 구하여 출력 

pro1 <- function(n) {
 vtemp <- seq(1,n,1)
 odd <- 0
 even <- 0

 for (i in c(1:n)) {
   if (vtemp[i]%%2 == 1) {
     odd = odd + vtemp[i] 
   }
   else {
     even = even +vtemp[i] 
   }
 }
 cat("odd :", odd,'\n')
 cat("even :", even)
}

pro1(4)
########################

###########################

# [문제2] 1부터 16까지 벡터 값을 Matrix 4행 4열 생성하고 아래의 제시된 문제를 작성
# 1. 행 단위로 각 행의 최대값
# 2. 열 단위로 각 열의 최대값
# 3. 행 단위 합계
# 4. 열 단위 합계
# 5. 행 단위 평균
# 6. 열 단위 평균
# 

vn <-  seq(1,16,1)
vm <- matrix(vn, nrow=4,byrow = T)
vm
nc <- ncol(vm) 
nr <- nrow(vm)

# 1. 행 단위로 각 행의 최대값
apply(vm,1,max)

mr1 =max(vm[1,])
mr1

mr2 =max(vm[2,])
mr2

mr3 =max(vm[3,])
mr3

mr4 =max(vm[4,])
mr4

#행렬의 원소중 최대값의 위치 알아내기 
max_v <- which(vm == max(vm) , arr.ind = TRUE)
max_v[1,2]
max_v
max_value <-vm[max_v[1,1],max_v[1,2]] 
max_value

# 2. 열 단위로 각 열의 최대값
apply(vm,2,max)

mc1 = max(vm[,1])
mc1
mc2 = max(vm[,2])
mc2
mc3 = max(vm[,3])
mc3 
mc4 = max(vm[,4])
mc4

# 1. 행 단위 최댓값
addr = apply(vm,1,max)
addr #10 26 42 58
# 2. 열 단위 최댓값
addc = apply(vm,2,max) 
addc # 28 32 36 40

# 3. 행 단위 합계
addr = apply(vm,1,sum)
addr #10 26 42 58
# 4. 열 단위 합계
addc = apply(vm,2,sum) 
addc # 28 32 36 40

# 5. 행 단위 평균
meanr = apply(vm,1, mean)
meanr # 2.5  6.5 10.5 14.5
# 6. 열 단위 평균
meanc = apply(vm, 2, mean)
meanc

# [문제3] 1부터 12까지 12개 요소로 구성된 벡터를 생성하고 3행 * 2열 * 2면의
# array 만들고 아래의 계산
c12 <-  c(1:12)
ax <- array(c12, c(3,2,2))
ax

#면참조 
ax[,,1]

ax[,,2]

#열 단위 참조 
a1 
a1[,1,1]

# 1. 각 면의 행의 합계



# 2. 각 면의 열의 합계
ax[,1,1]

