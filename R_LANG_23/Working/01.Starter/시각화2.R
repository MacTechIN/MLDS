# 데이터 시각화

# 데이터 셋 
# 미국 버지니아주의 하위계층 사망 비율 
data(VADeaths)

# Rual Male : 시골출신 남자 
# Rual Female : 시골 출신 여자 
# Urban Male : 도시 출신 남자 
# Urban Female : 도시출신 여자 

VADeaths


# 세로 막대 : barplot 
# 컬럼수 : 1개 
# 컬럼 특징 : 숫자형 
# 축이름 추가 
# 레이블 : xlab, ylab 

barplot(VADeaths, beside = F, col = rainbow(5), xlab = '출신지역', ylab = "사망율", main = "VA 하위 계층 사망비율")

# 범례표시 
x = 20 # 출력위치 : x
x =70 # 출력위치 : y
legend(x,y, c("50-54","55-59","60-64","65-59","70-74"), cex = 0.8, fill = rainbow(5))

