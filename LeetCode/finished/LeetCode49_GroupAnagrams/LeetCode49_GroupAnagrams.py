from typing import List
from collections import defaultdict



def groupAnagrams(strs: List[str]) -> List[List[str]]:
    anagrams = defaultdict(list)

    for word in strs:
        anagrams[''.join(sorted(word))].append(word)

    return list(anagrams.values())



strs = ["eat","tea","tan","ate","nat","bat"]
print(groupAnagrams(strs))