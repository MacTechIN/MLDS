


# P81
# 피클링(Pickling) , 언피클링(unpickling)
# 피클링 : 파이썬 객체를 바로  파일에 저장
# 언피클링 : 파일에 저장된 파이썬 객체를 읽음

import pickle

#파일 오픈
file = open("./pickling.txt","rb")


group_name = pickle.load(file)
member = pickle.load(file)
company = pickle.load(file)
songs = pickle.load(file)

file.close()

print("group_name : ", group_name)
print("member : ", member)
print("company : ", company)
print("songs : ", songs)





