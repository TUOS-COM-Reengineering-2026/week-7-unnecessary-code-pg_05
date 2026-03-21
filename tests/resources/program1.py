def is_palindrome(s):
    if len(s) == 0:
        return True
    elif s[0] != s[-1]:
        return False
    elif len(s) <= 1:
        return True
    else:
        return is_palindrome(s[1:-1])