def modify_word(word):
    chars = list(word)
    n = len(chars)

    # Find the rightmost character that is smaller than the character to its right
    for i in range(n-2, -1, -1):
        if chars[i] < chars[i+1]:
            break
    else:
        # If no such character is found, return the original word
        return word

    # Find the smallest character to the right of the above character, and swap them
    for j in range(n-1, i, -1):
        if chars[j] > chars[i]:
            chars[i], chars[j] = chars[j], chars[i]
            break

    # Reverse the suffix starting at i+1
    chars[i+1:] = reversed(chars[i+1:])

    return ''.join(chars)

# Example usage:
word = input("Enter a word consisting of only lowercase letters: ")
modified_word = modify_word(word)
print(f"The modified word is: {modified_word}")
