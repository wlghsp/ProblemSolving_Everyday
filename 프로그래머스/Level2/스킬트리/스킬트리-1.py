def solution(skill, skill_trees):
    answer = 0

    def appropriate_skill_tree(skill_tree):
        res = ''.join([c for c in skill_tree if c in skill])
        return skill.startswith(res)

    for skill_tree in skill_trees:
        if appropriate_skill_tree(skill_tree):
            answer += 1

    return answer

print(solution("CBD", ["BACDE", "CBADF", "AECB", "BDA"])) # 2