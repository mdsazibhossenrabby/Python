

def isPalindrome(word):
    if word==word[::-1]:
        return True
    return False

word=input("Enter any word : ")
print(f"is the word '{word}' palindrome : {isPalindrome(word)}")