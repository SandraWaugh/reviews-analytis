data = []
count = 0
with open ("reviews.txt","r") as f:
	for line in f :
		data.append(line)
		count += 1
		if count % 1000 == 0:
			print(len(data))

print("檔案讀取完了，總共有",len(data),"個資料")

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
