'''
This is the function that can process a given string and returns a dictionary with keys as unique words and their occurances as values. 

Input: String
Output: Dictionary containing unique words (keys) and their count of occurances (values) in the Input String

Assumptions:
- Words are considered case-sensitive ("Hello" and "hello" would result in 2 key entries in the output)
- Input string is assumed to be formatted properly, with whitespace between words
- Any numericals, special characters separated by whitespace in the input is also considered as a word
'''
def count(sentence: str) -> dict:
    sentence = sentence.strip()
    words = sentence.split()
    dict = {}
    
    for word in words:
        if word in dict:
            word_dict[word] += 1
        else:
            word_dict[word] = 1
    
    return word_dict
