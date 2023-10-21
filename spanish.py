 
word = input("Give me a word in English: ")

#  I Translate the word to Spanish using conditional statements
if word == "cat" or word == "Cat":
    translation = "gato"
elif word == "dog" or word == "Dog":
    translation = "perro"
elif word == "horse" or word == "Horse":
    translation = "caballo"
else:
    translation = "no entiendo"

# Here is the translation 
print(f"The translation in Spanish is: {translation}")