def sockMerchant(n, ar):
    pairs = 0
    for element in set(ar):
        pairs += ar.count(element) // 2
    return pairs


def sockMerchant(n, ar):
    return sum([ar.count(i) // 2 for i in set(ar)])


n = 9
ar = [10, 20, 20, 10, 10, 30, 50, 10, 20]
print(sockMerchant(n, ar))
