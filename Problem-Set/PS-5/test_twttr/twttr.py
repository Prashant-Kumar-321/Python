def main(): 
    twiit = input("Enter your twiit ? ")
    short_twiit = shorten(twiit)
    print("Shorten Twiit = ", short_twiit)

def shorten(word): 
    short_text = ""

    for char in word: 
        if not is_vowel(char): 
            short_text += char       

    return short_text

def is_vowel(c): 
    return c in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'] 

if __name__ == "__main__": 
    main()