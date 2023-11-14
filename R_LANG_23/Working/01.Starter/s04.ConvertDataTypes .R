# Convert data types 
# as.numeric(v) 
# as.logical(v) 
# as.character(v)


ns <- 30
is.numeric(ns)
as.character(ns)

nn <- as.numeric(ns)

is.numeric(nn) # TRUE

s = '홍길동'
s1 = as.numeric(s) # NA 
s2 = is.numeric(s1) # TRUE
s1
s2 
nn = is.nan(s1)
nn # FALSE

sn = is.na(s2)
sn # FALSE

# 정수형을 쓰기 위해서는 명시적으로 형변환(integer)을 해야한다. 
# 초깃값을 정수형으로 쓰기 위해서는 술자 뒤에 L을 붙임 
x <- 99
is.numeric(x) #TRUE
is.integer(x) #FASLE
is.double(x) #TRUE

y <- as.integer(99)
y
is.numeric(y) #TRUE
is.integer(y) # TRUE
is.double(y) #FALSE


z <- 1L
is.integer(z)
is.numeric(z)
