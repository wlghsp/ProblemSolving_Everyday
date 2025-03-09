def solution(cacheSize, cities):
    answer = 0
    cache = []
    for city in cities:
        city = city.lower()
        if city in cache: # 캐시 히트
            cache.remove(city)
            cache.append(city)
            answer += 1
        else:
            if cache and len(cache) >= cacheSize:
                cache.pop(0)
                cache.append(city)
            elif cacheSize > len(cache):
                cache.append(city)
            answer += 5

    return answer

print(solution(3, 	["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"])) # 50
print(solution(3, 	["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"])) # 21
print(solution(2, 	["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"])) # 60
print(solution(5, 		["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"])) # 52
print(solution(2, 	["Jeju", "Pangyo", "NewYork", "newyork"])) # 16
print(solution(0, 	["Jeju", "Pangyo", "Seoul", "NewYork", "LA"])) # 25