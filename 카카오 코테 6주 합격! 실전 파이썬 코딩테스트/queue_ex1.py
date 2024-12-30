
# 콘서트 입장 줄
queue = ["사람1", "사람2", "사람3", "사람4"]
print('큐: ', list(queue))

# 새로운 사람이 줄을 섬
queue.append("사람5")
print('사람5가 줄 선 후의 큐: ', list(queue))

# 첫 번째 사람이 줄을 떠남
queue.pop(0)
print('사람1이 떠난 다음의 큐: ', list(queue))


 