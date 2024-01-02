def is_palindrome(text):
    word = text[::-1]
    if text.lower() == word.lower():
        return True
    else:
        return False
