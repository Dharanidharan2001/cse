def palindrome(word):
    # word=input("enter the word")
    rev=word[::-1]
    if word==rev:
        print("It is a palindrome")
    else:
        print("Not a palindrome")
palindrome("car")
