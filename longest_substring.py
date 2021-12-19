#takes an inputted word and returns the longest possible sub string withotu repeating characters

def longest_substring(text):
    if len(text) == 1:
        return 1
    max_length = 0
    for index in range(len(text)-1):
        max_string = ''
        for next_character in text[index+1:]:
            if next_character in max_string:
                break
            else:
                max_string += next_character
        if len(max_string) > max_length:
            max_length = len(max_string)
    return max_length

#tests:
# x =longest_substring('abcabcbb')
# print(x)
# #3
# y = longest_substring('bbbbbb')
# print(y)
# #1
# z = longest_substring('pwwkew')
# print(z)
# #3
