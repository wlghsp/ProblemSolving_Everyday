def solution(cacheSize, cities):
    answer = 0
    cache = []
    for city in cities:
        city = city.lower()
        if city in cache:
            cache.remove(city)
            cache.append(city)
            answer += 1
        else: # 캐시 미스
            if cache and len(cache) >= cacheSize: # 가득 찬 상태이면
                cache.pop(0)
                cache.append(city)
            elif cacheSize > len(cache):
                cache.append(city)

            answer += 5

    return answer

print(solution(2, ["Jeju", "Pangyo", "NewYork", "newyork"]))
print(solution(0, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))
