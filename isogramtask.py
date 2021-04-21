# Determine if a word or phrase is an Isogram.
#
# An isogram (also known as a "non-pattern word") is a word or phrase without a repeating letter,
# however spaces and hyphens are allowed to appear multiple times.
#
# Examples of isograms:
#
# lumberjacks
# background
# downstream
# six-year-old
#
# The word isograms, however, is not an isogram, because the s repeats.
#
# Hint use methods .strip() and .replace() also maybe set keyword

def iso(string):
    test_string = string.lower().replace("-", "").replace(" ", "")

    for character in test_string:
        if test_string.count(character) > 1:
            return False
    return True


word = iso("lumberjacks")
word2 = iso("isograms")
word3 = iso("six-year-old")
print(word, word2, word3)
