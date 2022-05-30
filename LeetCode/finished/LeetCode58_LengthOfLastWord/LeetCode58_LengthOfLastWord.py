




def lengthOfLastWord( s: str):
    return len(s.strip().split()[-1])

s = "   fly me   to   the moon  "
print(lengthOfLastWord(s))