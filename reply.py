reply = []
count = 0
with open('reviews.txt', 'r') as f1:#f == file
    for line in f1:
    	reply.append(line)
    	count += 1
    	if count % 100000 == 0: 
    	#'%'是用來求餘數的，1001/1000 餘數=1
    	    print(len(reply))

print('檔案讀取完畢，共有', len(reply), '筆資料')
print(reply[0])
print('---------------')
print(reply[1])
#資料加總平均，我的答案
total = 0
count2 = 0
with open('reviews.txt', 'r') as f2:#f == file
    for line2 in f2:
        count2 += 1
        total = total + len(line2)
        if count2 % 1000000 == 0:
            a = total / len(reply)
            print(total)
            print(a)
#老師答案
sum_len = 0
for d in reply:
	sum_len += len(d) # sum_len = sum_len + len(d)
print('平均留言長度', sum_len / len(reply))

#清單篩選
new = []
for d in reply:#把reply 的每一個東西一個一個叫出來(forloop)
    if len(d) < 100:
    	new.append(d) #if你的長度<100我把你裝入new清單
print('共有', len(new), '筆留言小於100個字母')
print(new[0])

word = []
for d in reply:
    if 'good' in d:#if 後面會變是非題
        word.append(d)
print(len(word))
print(word[0])

#應用:list comprehension清單快寫法
""" 整段註解起始
bad = []
for b in bad:
    if 'bad' in b:
        bad.append(b)
print('共有', len(b), '筆資料')
整段註解結束 """ 
bad = [b for b in reply if 'bad' in b]
#output = [(number-1運算) for number變數 in reference清單 if number % 2 == 0 篩選條件 ]