
string = string.lower()
print(message.lower())

my_stop_words = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
    'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were',
    'will', 'with'
]
def remove_my_stop_words(sentence):
    tokens = sentence.split(" ")
    tokens_filtered= [word for word in text_tokens if not word in my_stopwords]
    return (" ").join(tokens_filtered)
    print(filtered_text)


def print_word_freq(file):
    """Read in `file` and print out the frequency of words in that file."""
    # list = ['a','b','a','c','d','c','c']
frequency = {}
for item in list:
   if (item in frequency):
      frequency[item] += 1
   else:
      frequency[item] = 1
for key, value in frequency.items():
        print("% s -> % d" % (key, value))
   #Your code will go here. #You can write additional functions if you want, and call them inside this function.
    # first open the file
    file_object = open('real_love.txt')
data = file_object.read()
        print(data)
file_object.close()
    
    
    
    with open(file) as f:
        lyrics = f.readlines()
        word_list = [line.split() for line in lyrics]
        print(word_list)

# This is an "incantation." You will not see it very often, and it needs to be here to be able to pass file names as arguments.
if __name__ == "__main__":
    import argparse
    from pathlib import Path

    parser = argparse.ArgumentParser(
        description='Get the word frequency in a text file.')
    parser.add_argument('file', help='file to read')
    args = parser.parse_args()

    file = Path(args.file)
    if file.is_file():
        print_word_freq(file)
    else:
        print(f"{file} does not exist!")
        exit(1)
# define punctuation
punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

my_str = "You see I'm searching for a real love.."

# To take input from the user
# my_str = input("Enter a string: ")

# remove punctuation from the string
def remove_punctuation(text):
    result = []
    for char in text:
        if char not in string.punctuation:
            result.append(char)
    return "".join(result)


# display the unpunctuated string
print(no_punct)

from collections import Counter
def word_count(fname):
        with open(fname) as f:
                return Counter(f.read().split())

print("Number of words in the file :",word_count("real_love.txt"))

