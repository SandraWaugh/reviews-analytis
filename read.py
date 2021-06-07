data = []
count = 0
with open ("reviews.txt","r") as f:
	for line in f :
		data.append(line)
		count += 1
		if count % 1000 == 0:
			print(len(data))
print("檔案讀取完了，總共有",len(data),"個資料")

print(data[0])

wc = {} #words_count
for d in data:   #d是字串，data是清單
	words = d.split()
	for word in words:
		if word in wc:
			wc[word] +=1
		else:
			wc[word] = 1  #新增key進字典

for word in wc:
	if wc[word] > 1000000:
		print(word,wc[word])	

print(len(wc))

while True:
 	word = input("請問你想查什麽字：")
 	if word == "q":
 		break
 	if word in wc:
 		print(word,"出現過的次數為",wc[word])
 	else:
 		print("這個字沒有出現過")
print("感謝使用本查詢功能")

























"""
sum_len = 0
for d in data:
	sum_len += len(d)

print("コメントの平均長さは", sum_len/len(data))

new = []
for d in data:
	if len(d) < 100:
		new.append(d)
print("合計",len(new),"のコメントは100文字未満です。")
print(new[1])
"""

"""
good =[]
for d in data:
	if "good" in d:
		good.append(d)
print("GOODの字が含められたコメントは",len(d),"回あります。")
print(good[0])
"""

#good = [d for d in data if "good" in d ]
#print(good[0])

#用【】來產生一個list，“for d in data” + “if "good" in d”
#     把d裝進good


"""
bad = ["bad" in d for d in data]
print(bad)
"""

