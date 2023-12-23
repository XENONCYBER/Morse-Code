def get_value_from_key(dictionary,value):
    for key,val in dictionary.items():
        if val==value:
            return key

#Dictionary which contains all the characters as keys and morse equivalents as values.
dictionary={
    #Alphabets
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    #Numbers
    '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----',
    #Special Characters
    '.': '.-.-.-', ',': '--..--', '?': '..--..', "'": '.----.', '!': '-.-.--',
    '/': '-..-.', '(': '-.--.', ')': '-.--.-', '&': '.-...', ':': '---...',
    ';': '-.-.-.', '=': '-...-', '+': '.-.-.', '-': '-....-', '_': '..--.-',
    '"': '.-..-.', '$': '...-..-', '@': '.--.-.', ' ': '/'}
while True:
    note=int(input("What operation to perform: \n 1) English to morse. \n 2)Morse to english. \n"))
    if note==1:
        #This list contains all the keys of the dictionary.
        valid_chars=list(dictionary.keys())

        #Take the text to be translated.
        text=str(input("Enter the text to be translated:"))

        #Converts all the characters in the string to uppercase as the keys are also uppercase in the dictionary.
        text=text.upper()

        #Creates a list of all the inputted text, Divides them into single characters
        text_list=[]
        for i in range(0, len(text)):
            text_list.append(text[i])

        #Creates a list of all the inputted text which can be translated 
        #into morse code by checking if the translation is present in the dictionary
        final_text=[]
        omitted_text=[]
        for i in range(0, len(text_list)):
            if text_list[i] in valid_chars:
                final_text.append(text_list[i])
            else:
                omitted_text.append(text_list[i])

        #Actual Translation
        translated_list=[]
        for i in range(0,len(final_text)):
            translated_list.append(dictionary.get(final_text[i]))
        translated_text=' '.join(translated_list)
        print(translated_text)
        if len(omitted_text) > 0:
            print(f"These characters were not printed because their translation was not available: {omitted_text}")
        break    
    elif note==2:
        morse_input=str(input("Enter a valid morse code: ")).split()
        translated_to_english_list=[]
        # omitted_morse=[]
        for i in range(0, len(morse_input)):
            if not get_value_from_key(dictionary, morse_input[i])==None:
                translated_to_english_list.append(get_value_from_key(dictionary,morse_input[i]))
            # else:
            #     omitted_morse.append(get_value_from_key(dictionary, morse_input[i]))
        translated_to_english=''.join(translated_to_english_list)
        print("The text translated to English is:",translated_to_english)
        # if len(omitted_morse)>0:
        #     print("These set of codes were not valid and thus were omitted: ",omitted_morse)
        break