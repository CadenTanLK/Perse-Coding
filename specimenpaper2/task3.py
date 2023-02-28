word = input()
word_length = len(word)
if word_length < 31:
    ans = word
    while len(ans) < 31:
        ans = str(ans) + str(word)
print (ans)



~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



word = input()
ans = word
while len(ans) < 31:
    ans = str(ans) + str(word)
print(ans)
