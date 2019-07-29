# 28. Implement strStr()
#
#
# Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
#
# Example 1:
#
# Input: haystack = "hello", needle = "ll"
# Output: 2
# Example 2:
#
# Input: haystack = "aaaaa", needle = "bba"
# Output: -1
# Clarification:
#
# What should we return when needle is an empty string? This is a great question to ask during an interview.
#
# For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf().

def strStr(haystack: str, needle: str) -> int:
    if not needle:
        return 0

    needle_len = len(needle)
    for i in range(len(haystack)):
        if haystack[i:i + needle_len] == needle:
            return i

    return -1

print(strStr("hello", "ll"))
print(strStr("a", "a"))

