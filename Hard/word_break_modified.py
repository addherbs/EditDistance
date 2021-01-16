def decode(input_string, word_dict):
    if input_string in word_dict: return [input_string]

    answer = []
    for each_word in word_dict:
        if input_string.startswith(each_word):
            if input_string is each_word:
                return [each_word]

            next_string = input_string[len(each_word):]
            next_values = decode(next_string, wordDict)
            if next_values:
                for each_string in next_values:
                    answer.append(each_word + " " + each_string)

    return answer


s = "catsanddog"
wordDict = ["cat", "cats", "and", "sand", "dog"]

print(decode(s, set(wordDict)))
