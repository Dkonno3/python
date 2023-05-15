alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
            'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def ceasar(crypt,intxt,inshift):
    cipher_txt = ''
    inshift = inshift % 26
    if crypt== 'encode':
        for letter in intxt:
            if letter in alphabet:
                position=alphabet.index(letter)
                new_position = position + inshift
                if new_position>26:
                    new_position=new_position-26
                    new_letter=alphabet[new_position]
                else:
                    new_letter=alphabet[new_position]
                cipher_txt+=new_letter
            else: cipher_txt+=letter
    elif crypt== 'decode':
        for letter in intxt:
            if letter in alphabet:
                position = alphabet.index(letter)
                new_position = position - inshift
                if new_position < 0:
                    new_position = 26 + new_position
                    new_letter = alphabet[new_position]
                else:
                    new_letter = alphabet[new_position]
                cipher_txt += new_letter
            else: cipher_txt += letter
    print(f"The result for {intxt} is: {cipher_txt}")

run=True
direction=''
while direction=='encode' or direction=='decode' or run==True:
    direction = input("Type 'encode' to encrypt or 'decode' to decrypt \n").lower()
    text = input("Type the message: \n").lower()
    shift = int(input("Type the shift number: \n"))
    ceasar(crypt=direction,intxt=text,inshift=shift)
    direction=''
    rerun=input("run again? y,n ")
    if rerun=='n':
        run=False
