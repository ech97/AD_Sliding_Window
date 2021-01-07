
data = "1010101010101010100"

with open("text1.txt", "w", encoding = "utf-8", newline="") as f:
    f.write(data)


'''
with as 구문은 자동으로 close를 해주는 역할
'''