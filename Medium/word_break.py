def decode(input_string, word_dict):
    print(input_string)
    for key, value in word_dict.items():
        if input_string is value: return [key]

    answer = []
    for key, value in word_dict.items():
        if input_string.startswith(value):
            if input_string is value:
                return [key]

            next_string = input_string[len(value):]
            next_values = decode(next_string, word_dict)
            if next_values:
                for each_string in next_values:
                    answer.append(key + " " + each_string)
    print(input_string, ": ", answer)
    return answer


s = "catsanddog"
wordDict = ["cat", "cats", "and", "sand", "dog"]

test = {chr(num + 97): str(num + 1) for num in range(26)}
word = "111"

print(word, test)
# print(decode(s, set(wordDict)))
print(decode(word, test))
