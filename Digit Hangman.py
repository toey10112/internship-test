def answer(text):
    for i in text:
        print(i, end="")
    print()


problem = list(input().split(' '))
length = len(problem)
text = ['_'] * length
check = []
score = 0
answer(text)
for i in range(5):
    n = input()
    temp = False
    for j in range(length):
        if n == problem[j]:
            temp = True
            score += 1
            text[j] = n
    if temp:
        check.append(n)
    elif n not in check:
        check.append(n)
        text += n + ' '
    answer(text)
print(score)
