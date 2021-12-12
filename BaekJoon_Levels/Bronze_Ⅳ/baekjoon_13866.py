import sys

input = sys.stdin.readline

skill_levels = list(map(int, input().split())).sort()

skill_levels.sort()

difference = (skill_levels[-1] + skill_levels[0]) - (skill_levels[1] + skill_levels[2])

print(abs(difference))
