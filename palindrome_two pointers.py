word = input("Enter a word:")
left = 0
right = len(word)-1
while left < right:
    if word[left] != word[right]:
        print("not a palindrome")
        break
    left += 1
    right -= 1
else:
    print("palindrome")