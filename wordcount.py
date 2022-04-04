"""Count words in file."""


# put your code here.
# open text file
file = open('test.txt')
file = file.read()
file = file.lower()


def get_letter_count(phrase):
    letter_counts = {}
    special_chars = ['.', ',', '?', '!',
                     ')', '(', '/', '_', '@', '%', '&', '$', ']', '[', '\n', '#', '-', ' ']
    for letter in phrase:
        if letter in special_chars:
            continue
        letter_counts[letter] = letter_counts.get(letter, 0) + 1
    return letter_counts


print(get_letter_count(file))
