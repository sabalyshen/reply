reply = []
with open('reviews.txt', 'r') as f1:#f == file
    for line in f1:
    	reply.append(line)
print(len(reply))
