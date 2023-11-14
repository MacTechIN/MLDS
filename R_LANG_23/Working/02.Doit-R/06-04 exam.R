# mpg 데이터 분석 하기 문제 

# audi 에서 생산한 자동차중 hwy 가 1~6위 까지 출력 하시요 

library(ggplot2)

mpq <- as.data.frame(ggplot2::mpg)

mpq

audi_max_hwy <- mpq %>% select(manufacturer,hwy) %>% filter(manufacturer=='audi') %>% arrange(desc(hwy)) %>% head(10) 
audi_max_hwy
