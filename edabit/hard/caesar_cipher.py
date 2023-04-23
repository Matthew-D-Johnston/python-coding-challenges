def caesar_cipher(text, key):
    key %= 26
    encoded_text = ''

    for char in text:
        char_code = ord(char)
        encoded_char_code = char_code + key

        if char_code >= 65 and char_code <= 90:
            if encoded_char_code > 90:
                encoded_char_code -= 26
            
            encoded_text += chr(encoded_char_code)
        elif char_code >= 97 and char_code <= 122:
            if encoded_char_code > 122:
                encoded_char_code -= 26
            
            encoded_text += chr(encoded_char_code)
        else:
            encoded_text += ' '
        
    return encoded_text

print(caesar_cipher("hello", 5))
print(caesar_cipher("hello world", 1))
print(caesar_cipher("a", 2))