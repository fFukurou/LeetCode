# A pangram is a sentence where every letter of the English alphabet appears at least once.

# Given a string sentence containing only lowercase English letters, return true if sentence is a pangram, or false otherwise.


def checkIfPangram(sentence: str) -> bool:
    letter_set = set()
    for letter in sentence:
        if letter not in letter_set:
            letter_set.add(letter)
            
    
    return len(letter_set) == 26







def main():
    # sentence = "I like to eat people with bunny masks."
    sentence = "thequickbrownfoxjumpsoverthelazydog"
    print(checkIfPangram(sentence))


if __name__ == "__main__":
    main()