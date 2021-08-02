data = []
count = 0
with open('reviews.txt', 'r') as f1:
    for line in f1:
        data.append(line)
        count += 1
        if count % 100000 == 0: 
            print(len(data))

print('檔案讀取完畢，共有', len(data), '筆資料')
print(data[0])

wc = {} #word_count
for d in data:
    words = d.split(' ') #split()內建功能就是由空白見切割
    for word in words:
        if word in wc:
            wc[word] += 1
        else:
            wc[word] = 1 #新增

for word in wc:
    if wc[word] > 1000000:
        print(word, wc[word])        
print(len(wc)) #看字典的長度(多少key) 

while True:
    word = input('請問你想查什麼字? ')
    if word == 'q':
        break
    if word in wc:
        print(word, '出現的次數為', wc[word])
    else:
        print('這個字沒出現過喔!')

print('感謝使用')