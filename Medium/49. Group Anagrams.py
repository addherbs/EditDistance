# 49. Group Anagrams
# Medium
#
# Given an array of strings, group anagrams together.
#
# Example:
#
# Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
# Output:
# [
#   ["ate","eat","tea"],
#   ["nat","tan"],
#   ["bat"]
# ]

#############################   TLE   #############################
from collections import Counter


class Solution:
    def groupAnagrams(self, strs):
        counters = []
        for each in strs:
            curr_counter = Counter(each)
            if curr_counter not in counters:
                counters.append(curr_counter)

        result = [[] for each in range(len(counters))]
        for each in strs:
            each_counter = Counter(each)
            for index, curr_counter in enumerate(counters):
                if each_counter == curr_counter:
                    result[index].append(each)
                    break
        return result


#
# b = Solution()
# print(b.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))

#############################   TLE   #############################


#############################   working  #############################

from collections import defaultdict


def groupAnagrams(strs):
    d = defaultdict(list)
    for w in strs:
        key = tuple(sorted(w))
        print(w, key)
        d[key].append(w)
    return list(d.values())


print(groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))

#############################   working  #############################


#############################   best  #############################

def groupAnagrams(strs):
    d = defaultdict(list)
    for w in strs:
        key = ''.join(list(sorted(w)))
        d[key].append(w)
    return list(d.values())

print(groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))

#############################   best  #############################