def encrypt(text,ss): 
        res = "" 
        # chars
        for i in range(len(text)): 
            char = text[i]

        # uppercase
            if (char.isupper()): 
                res += chr((ord(char) + ss-65) % 26 + 65) 

        # lowercase
            else: 
                res += chr((ord(char) + ss - 97) % 26 + 97)
        return res

def decrypt(text,ss): 
        res = "" 

        # chars
        for i in range(len(text)): 
            char = text[i] 

        # uppercase
            if (char.isupper()): 
                res += chr((ord(char) - ss-65) % 26 + 65) 

        # lowercase
            else: 
                res += chr((ord(char) - ss - 97) % 26 + 97) 
        return res 

    # results
text = input('---Write line to encrypt---\n')
s = 4
print("Shift : " + str(s)) 
print("Encrypted: " + encrypt(text,s))
print("Original: " + decrypt(encrypt(text,s),s))
