#takes an inputted word and returns the longest possible palindrome within

def longest_palindromic_substring(text):
    if len(text) == 1:
        return 'a'
    palindrome = ''
    for index in range(len(text)-1):
        max_string = ''
        for next_character in text[index+1:]:
            max_string += next_character
            if max_string == max_string[::-1]:
                if len(max_string) > len(palindrome):
                    palindrome = max_string
    return palindrome

#tests:
# x = longest_palindromic_substring('babad')
# print('')
# 
# y = longest_palindromic_substring('cbbd')
# print('')
# 
# z = longest_palindromic_substring('a')
# print('')
# a = longest_palindromic_substring('ac')

