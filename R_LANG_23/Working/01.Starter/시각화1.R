#  데이터 시각화..
# 

# 막대 차트 

chart <-c(300,450,500,320,460,220,480,510) 
names(chart) <- c("2022 1분기","2022 2분기 ", "2022 3분기","2022 4분기 ","2023 1분기","2023 2분기","2023 3분기","2023 4분기")

chart
str(chart)

par(family='AppleGothic')


#  세로막대 : barplot 
#  칼럼수 : 1개 
#  칼럼 특성 : 숫자형 

barplot(chart, ylim = c(0,600), col = rainbow(8), main = "2022년 vs 2023년 비교")


########################################################

# 가로막대 

barplot(chart, xlim = c(0,600), col = rainbow(8), horiz = T, xlab = "매출액", ylab = '년도별 분기 현황', main = "2022년도 vs 2023년도")




