#Vector 자료 구조 
# 합집합, 교집합 , 차집합 

# 합집합 : union() 
n <- c(1,3,5,7)
m <- c(3,5,9)

uni =union(n,m)
uni # 1 3 5 7 9


#교집합 : intersect()
#n - m  (양쪽에 존재하는 데이터만 선택
is = intersect(n,m)
is

#차집합 : setdiff(n,m)
# n에는 있고, m에는 없는 데이터 
# n-m 
setdiff(n,m) # 1 7

# m에는 있고 n에는 없는 데이터 
setdiff(m,n) # 9 

# 단순결합 : 중복허용 
z = c(n,m)
z

