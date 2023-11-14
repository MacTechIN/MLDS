# Vector 자료구조
# 참조 
# R의 내장 문자형 벡터 : letters

args(print)
letters
print(letters)
print(x = letters)

letters[1] # a 
letters[length(letters)] # z (26)

a <-  letters

a [c(1,3,5)] #"a" "c" "e"
a [c(T,F)]

a <- letters[1:5]
a
a[10] <- 'x'
a
#벡터의 원소를 삭제 
# a <- a[-c(6:9)]
a <-  a[-seq(6,9)] # 동일한 효과 

a

# replace 수정 
a[6] <- 'Z'
a
