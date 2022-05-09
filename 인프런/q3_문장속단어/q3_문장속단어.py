

sen = list(input().split())
sen_list = list(map(len, sen))


max = max(sen_list)


for s in sen:
    if len(s) == max:
        print(s)







