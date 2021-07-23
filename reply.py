reply = []
count = 0
with open('reviews.txt', 'r') as f1:#f == file
    for line in f1:
    	reply.append(line)
    	count += 1
    	if count % 10000 == 0: 
    	#'%'是用來求餘數的，1001/1000 餘數=1
    	    print(len(reply))

print(len(reply))
print(reply[0])
print('---------------')
print(reply[1])