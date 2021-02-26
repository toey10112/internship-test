n = int(input())
answer = []
for i in range(n):
    text = str(input())
    text = text.split(' ')
    tmp = ''
    for i in text:
        if i[0] != i[0].lower():
            tmp += i[0]
    answer.append(tmp)
answer.sort(key=len, reverse=True)
for i in answer:
    print(i)
