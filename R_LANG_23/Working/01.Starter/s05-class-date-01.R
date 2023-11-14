# 날짜형 

now <- "23/11/08"
now
mode(now) #"character"
class(now) # "character"

dt <- as.Date(now, '%y/%m/%d')
dt
mode(dt)
class(dt)

today <- "2023/11/08" 
dt2 <- as.Date(today,"%Y/%m/%d") # 년도4자리: %Y 
dt2
mode(dt2)
class(dt2)

#년/월/일/시/분/초 표기 하기 
time <- "2023/11/08 12:30:49"

tm1 <- as.Date(time, "%Y/%m/%d %H:%M:%S")
tm1

tm2 <- strptime(time, format = "%Y/%m/%d %H:%M:%S" )
tm2
mode(tm2)
class(tm2)

#오늘 , 현재 시간 

tmx  <- Sys.time()
class(now)
tmx <- as.character(now)
tmx
# tmxx <- strptime(tmx, format ="%Y/%m/%d %H:%M:%S")
tmxx <- as.POSIXlt(tmx, format="%Y/%m/%d %H:%M:%S")  
tmxxx <- as.str
tmx
tmxx 
mode(tmx)
mode (tmxx)
class(tmx)
class(tmxx)

# 로케일 확인 
Sys.localeconv()
Sys.getlocale()
Sys.getpid()

