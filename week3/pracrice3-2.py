s = str(input())
t = str(input())
theWordDic = {}
list_s = list(s)
list_t = list(t)
for word in s:
    if word not in theWordDic:
        theWordDic[word] = 1
    else:
        theWordDic[word] += 1
print(len(list_s))
print(len(theWordDic))
print("".join(list_s))
theRepeatedWord = []
in_S_not_In_T = 0
for word in theWordDic:
    if word in list_t:
        theRepeatedWord.append(word)
    else:
        in_S_not_In_T += 1
differentWordCount = len(set(list_s)) + len(set(list_t)) - len(theRepeatedWord)
theRepeatedWord.sort()
print("".join(theRepeatedWord))
print(differentWordCount)
print(in_S_not_In_T)
for word in list_t:
    if word not in theWordDic:
        theWordDic[word] = 1
    else:
        theWordDic[word] += 1
print("{}:{}".format(max(theWordDic, key=theWordDic.get), max(theWordDic.values())))
