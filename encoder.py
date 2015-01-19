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

def mapper ( toMap , encodedAlphabet , additionalMappsings ):
    try:
        return additionalMappsings[encodedAlphabet[toMap]];
    except:
        return encodedAlphabet[toMap]

def encode ():
    normalAlphabet = generateAlphabet()
    
    encodedAlphabet = generateEncodedAlphabet( normalAlphabet )

    for letter in encodedAlphabet.keys():
        encodedAlphabet[letter] = mapper(encodedAlphabet[letter],encodedAlphabet,additionalMappsings)
    
    with open(pathToFile) as f:
        content = f.readlines()

    print(encodedAlphabet)

def main():
    encode()
    
if __name__ == "__main__":
    main()
