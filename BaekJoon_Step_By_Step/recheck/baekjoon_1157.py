words = input().upper()
words_list = list(set(words))
word_count = list()

for i in words_list:
    count = words.count(i)
    word_count.append(count)

if (word_count.count(max(word_count)) >= 2):
    print('?')
else:
    print(words_list[(word_count.index(max(word_count)))])


# from collections import Counter

# word = input().upper()
# c = Counter(word)

# many = []

# for k, v in c.items():
#     if v == max(c.values()):
#         many.append(k)

#         if len(many) > 1:
#             break
# if len(many) == 1:
#     print(many[0])
# else:
#     print('?')
