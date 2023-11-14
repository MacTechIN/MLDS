# 05장
# 데이터 분석 기초 !
# - 데이터 파악하기, 다루기 쉽게 수정하기 
# 05-3 파생 변수 
library(ggplot2)
df <- data.frame(var1=c(4,3,8), var2=c(2,6,1))

df

df$var_sum <- df$var1 + df$var2

df

df$var_mean <- (df$var1 + df$var2)/2

df

#########################################
# mpg 통합 연비 

mpg <-  as.data.frame(ggplot2::mpg)

mpg$total <-  (mpg$cty + mpg$hwy) / 2

head(mpg,10)

summary (mpg$total)

hist(mpg$total)

mpg$test <- ifelse(mpg$total >= 20,"pass","fail")
head(mpg,10)
table(mpg$test)
qplot(mpg$test)

mpg$grade <-ifelse(mpg$total >=30, "A", ifelse(mpg$total>=20,'B' , 'C'))

head(mpg,10)
qplot(mpg$grade)
table(mpg$grade)

mpg$grade2 <- ifelse(mpg$total>=30, "A", ifelse(mpg$total >=25, "B", ifelse(mpg$total >=20,"C","D")))
table (mpg$grade2)
qplot(mpg$grade2)
