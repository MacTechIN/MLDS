


# P81
# 피클링(Pickling) , 언피클링(unpickling)
# 피클링 : 파이썬 객체를 바로  파일에 저장
# 언피클링 : 파일에 저장된 파이썬 객체를 읽음

import pickle

group_name = "BlackPink"
member = 13
company = 'YSIT미래교육원'
songs ={'마지막처럼':2023, 'Kill this love':2019}

#바이너리(이진)파일
file = open("./pickling.txt","wb")

pickle.dump(group_name, file)
pickle.dump(member, file)
pickle.dump(company, file)
pickle.dump(songs, file)

file.close()



