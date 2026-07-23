def Palindrome():
    text = input("Enter Text = ")
    if text == text[::-1]:
        print("Text Is Palindrome")
    else:
        print("Text is not Palindrome")

Palindrome()
