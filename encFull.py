import tkinter

window = tkinter.Tk()
window.title("Program de encriptie anti KGB Bulgar")
window.geometry("600x600")
window.wm_iconbitmap('enc0.ico')

toEncriptLabel = tkinter.Label(window,text="Fisierul de encriptat")
toEncriptEntry = tkinter.Entry(window,width=70)
toEncriptLabel.pack()
toEncriptEntry.pack()

window.mainloop()

additionalMappsings = { 'a' : '@' , 'c' : '<' , 'e' : '3' , 'i' : '|' , 'o' : '(' , 'q' : ')' , 't' : '7' , 'B' : '8' , 'G' : '6' , 'M' : '^' , 'O' : '0' , 'R' : '&' }
pathToFile = "test.txt"

def generateAlphabet ():

    normalAlphabetBig = []
    normalAlphabetSmall = []
    normalAlphabet = []
    
    for letter in range(65,91):
        normalAlphabetBig.append(chr(letter))

    for letter in range(97,123):
        normalAlphabetSmall.append(chr(letter))

    normalAlphabet = normalAlphabetSmall + normalAlphabetBig

    return normalAlphabet

def generateEncodedAlphabet ( alphabet ):
    offsetBig = 65
    offsetSmall = 97
    shift = 5
    encodedAlphabet = {}
    
    for letter in range(0,26):
        newMap = (letter + shift)%26 + offsetSmall
        encodedAlphabet[alphabet[letter]] = chr(newMap)

    for letter in range(0,26):
        newMap = (letter + shift)%26 + offsetBig
        encodedAlphabet[alphabet[letter+26]] = chr(newMap)
        
    return encodedAlphabet

def mapper ( toMap ):
    try:
        return additionalMappsings[toMap];
    except:
        return toMap

def encode ():
    normalAlphabet = generateAlphabet()
    encodedAlphabet = generateEncodedAlphabet( normalAlphabet )
    for letter in encodedAlphabet.keys():
        encodedAlphabet[letter] = mapper(encodedAlphabet[letter])

    encodedText = ''
    
    with open(pathToFile) as f:
        for content in f:
            content = content.strip()
            encodedText = encodedText + change(content , encodedAlphabet)

    return encodedText

def change(toChange , encodedAlphabet):
    toReturn = ''
    for i in range(0, len(toChange)):
        try:
            toReturn = toReturn + encodedAlphabet[toChange[i]]
        except:
            toReturn = toReturn + toChange[i]
    return toReturn

def revert(toChange , decodeAlphabet):
    toReturn = ''
    for i in range(0, len(toChange)):
        try:
            toReturn = toReturn + decodeAlphabet[toChange[i]]
        except:
            if toChange[i] == '>':
                toReturn = toReturn + '\n'
            else:
                toReturn = toReturn + toChange[i]
    return toReturn

def decode ( toDecode ):
    normalAlphabet = generateAlphabet()
    encodedAlphabet = generateEncodedAlphabet( normalAlphabet )
    for letter in encodedAlphabet.keys():
        encodedAlphabet[letter] = mapper(encodedAlphabet[letter])
    
    decodeAlphabet = {v: k for k, v in encodedAlphabet.items()}
    return revert(toDecode , decodeAlphabet)

def main():
    encodedText = encode()
    decodedText = decode(encodedText)
    print(encodedText)
    print(decodedText)
    
if __name__ == "__main__":
    main()
