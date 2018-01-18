from collections import Counter

cnt = Counter()

mycnt = dict()

for word in ['red', 'blue', 'red', 'green', 'blue', 'blue']:
    cnt[word] += 1
    mycnt[word] = mycnt.get(word, 0) + 1

print(cnt)
print(cnt.most_common(2))

print(mycnt)

dict2 = dict()
dict2['good'] = 2
dict2['bad'] = 5
print(dict2)

dict2.update({
    'a': 2,
    'b': 3
})

print(dict2)


