import string

def file_checker(file_name):
    
    each_words = [] #create an empty list to store all words in the text 

    with open(file_name, 'r') as file:
        for line in file:
            word_list = line.split() #here each words are split and stored into a list

            for word in word_list:
                
                cleaned_word = word.strip(string.punctuation).lower()
                if cleaned_word:
                    each_words.append(cleaned_word)

    return each_words

split_words = file_checker("sample_text.txt")

for word in split_words:
    print(word)
