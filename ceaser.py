def encryption(text,step):
    result=""
    for i in range(len(text)):
        char=text[i]

        if(char.isupper()):
              result+=chr((ord(char) +step-65)%26+65)  
        else:
              result+=chr((ord(char) +step-97)%26+97)

    return result 
