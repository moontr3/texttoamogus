'''
Made by moontr3, 2022
github.com/moontr3/texttoamogus/
'''

def amoguser(text, encoding = 'utf-8'):
    '''
    ╔╡FUNCTION DESCRIPTION╞══════════════════════╗
    ║                                            ║
    ║   This function is used to convert text    ║
    ║   into Amogus text characters.             ║
    ║   unamoguser() function should be used to  ║
    ║   decode amogused text back to normal.     ║
    ║                                            ║
    ╚════════════════════════════════════════════╝

    ╔╡ARGUMENTS DESCRIPTION╞═════════════════════╗
    ║                                            ║
    ║   ╔════════════╦═══════════════════════╗   ║
    ║   ║  Argument  ║      Description      ║   ║
    ║   ╚════════════╩═══════════════════════╝   ║
    ║   ┌────────────┬───────────────────────┐   ║
    ║   │ text: any  │  Text that should be  │   ║
    ║   │            │    converted into     │   ║
    ║   │            │   amogus characters   │   ║
    ║   │            │ (note that text will  │   ║
    ║   │            │  be converted to str  │   ║
    ║   │            │     in any case)      │   ║
    ║   ├────────────┼───────────────────────┤   ║
    ║   │ encoding:  │ Encoding that should  │   ║
    ║   │ str        │      be used for      │   ║
    ║   │ (default:  │  converting the text  │   ║
    ║   │ 'utf-8')   │                       │   ║
    ║   └────────────┴───────────────────────┘   ║
    ║                                            ║
    ╚════════════════════════════════════════════╝
    '''
    text = str(text) # Converting text to str in case if it is not
    encoded = 'ඕ'.join(format(x, 'b') for x in bytearray(text, encoding)) # Converting text to binary 
                                                                          # string with ඕ as a separator
    encoded = encoded.replace('0','ඞ').replace('1','𐐘') # Replacing zeroes and ones with different amogus characters

    return encoded

def unamoguser(text, encoding = 'utf-8', raise_on_incorrect_text = False):
    '''
    ╔╡FUNCTION DESCRIPTION╞══════════════════════╗
    ║                                            ║
    ║   This function is used to convert         ║
    ║   amogused text back to normal text.       ║
    ║   amoguser() function should be used to    ║
    ║   get amogused text for this function.     ║
    ║                                            ║
    ╚════════════════════════════════════════════╝

    ╔╡ARGUMENTS DESCRIPTION╞═════════════════════╗
    ║                                            ║
    ║   ╔════════════╦═══════════════════════╗   ║
    ║   ║  Argument  ║      Description      ║   ║
    ║   ╚════════════╩═══════════════════════╝   ║
    ║   ┌────────────┬───────────────────────┐   ║
    ║   │ text: any  │  Amogused text that   │   ║
    ║   │            │  should be converted  │   ║
    ║   │            │   into normal text    │   ║
    ║   │            │ (note that text will  │   ║
    ║   │            │  be converted to str  │   ║
    ║   │            │     in any case)      │   ║
    ║   ├────────────┼───────────────────────┤   ║
    ║   │ encoding:  │ Encoding that should  │   ║
    ║   │ str        │      be used for      │   ║
    ║   │ (default:  │  converting the text  │   ║
    ║   │ 'utf-8')   │    (it is heavily     │   ║
    ║   │            │  recommended to use   │   ║
    ║   │            │ the same encoding as  │   ║
    ║   │            │      you used in      │   ║
    ║   │            │ amoguser() function!) │   ║
    ║   ├────────────┼───────────────────────┤   ║
    ║   │ raise_on_  │  Used to raising an   │   ║
    ║   │ incorrect_ │ exception if program  │   ║
    ║   │ text: bool │  detects any symbols  │   ║
    ║   │ (default:  │   other than amogus   │   ║
    ║   │ False)     │  characters in text.  │   ║
    ║   │            │    Set to False to    │   ║
    ║   │            │ automatically remove  │   ║
    ║   │            │      unnecessary      │   ║
    ║   │            │      characters       │   ║
    ║   └────────────┴───────────────────────┘   ║
    ║                                            ║
    ╚════════════════════════════════════════════╝
    '''
    temp_text = '' # Creating variable for temporarily storing necessary text
    text = str(text) # Converting text to str in case if it is not

    for i in range(len(text)):

        if text[i] != '𐐘' and text[i] != 'ඞ' and text[i] != 'ඕ': # If text contains symbols other than amogus characters
            if raise_on_incorrect_text: # If user asked to raise the exception
                raise Exception('Text contains characters that are not allowed by the program.') # Raising the exception

        else: # If selected symbol is an amogus character
            temp_text += text[i] # Adding this character to temporary variable

    text = temp_text # Replacing text variable with one 
                     # with only amogus characters in case 
                     # there was characters that aren't allowed

    text = text.replace('ඞ','0').replace('𐐘','1') # Replacing amogus characters with zeroes 
                                                  # and ones so the text will become an actual binary string

    values = text.split('ඕ') # Splitting the text in different binary
                             # strings each representing one symbol
    encoded = bytes([int(x, 2) for x in values]).decode(encoding) # Converting binary strings to symbols
                                                                  # and decoding the text with selected encoding
    
    return encoded
