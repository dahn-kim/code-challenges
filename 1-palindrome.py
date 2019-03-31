def is_palindrome(word):
# YOUR CODE GOES HERE
    if word.lower() == word[::-1].lower() :
        return True
    return False

print(is_palindrome('Deleveled'))
