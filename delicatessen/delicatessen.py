## function to add two numbers together.
def sandwich(text, string1, string2):
    '''
    searches text for string1 and string 2, returns the string in between
    '''
    if string1 in text and string2 in text:
        position1=text.find(string1)
        length1=len(string1)
        position2=text.find(string2)
        meat=text[position1+length1:position2]
        return meat
    else:
        return "Error making sandwich"
    
def corndog(word, text, size):
    '''
    Searches text for word, return a string of characters surrounding that word. 
    '''
    if word.lower() in text.lower():
        location=text.find(word)
        dog=text[location-size:location+size]
        return dog
    else:
        return "Corndog failed"
    
