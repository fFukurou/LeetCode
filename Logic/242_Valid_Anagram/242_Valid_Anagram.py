


def isAnagram(s: str, t: str) -> bool:
    if len(s) != len(t): return False
    
    # Sorting:
    return sorted(s) == sorted(t)
    
    
    # letters = []
    # for letter in s:
    #     letters.append(letter)
        
    # for letter in t:
    #     if letter in letters:
    #         letters.remove(letter)
            
            
    
    # return True if len(letters) == 0 else False

    



def main():
    print(isAnagram("anagram", "nagaram"))


if __name__ == "__main__":
    main()