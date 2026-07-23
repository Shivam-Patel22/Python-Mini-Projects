def Palindrome():
    text = input("Enter Text to Check Palindrome or Not Palindrome = ")
    if text == text[::-1]:
        print("Text Is Palindrome")
    else:
        print("Text is not Palindrome")

Palindrome()
