import json

def load_dictionary():
    f = open("dictionary.json", "r")
    text=f.read()
    f.close()
    dictionary=json.loads(text)
    return dictionary

def save_dictionary(dictionary):
    text = json.dumps(dictionary)
    f = open("dictionary.json", "w")
    f.write(text)
    f.close()

dictionary=load_dictionary()

print("Are you a translator user(1) or a translator developer(2):")
selection = int(input("Enter 1 or 2: "))

if selection==1:
    word=""
    while word!="exit":
        word=input("Enter a word to translate or 'exit': ")
        if word!="exit":
            if word in dictionary:
                print(word,dictionary[word],sep=' -> ')
            else:
                print('Not Found')
elif selection==2:
    word=""
    while word!="exit":
        word=input("Enter an English word to save or 'exit': ")
        if word!="exit":
            ar_word=input("Enter the Arabic word of '{0}': ".format(word))
            dictionary[word]=ar_word
            save_dictionary(dictionary)
else:
    print("invalid selection")
