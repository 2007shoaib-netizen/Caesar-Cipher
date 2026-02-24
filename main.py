logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""

def caesar(ch,direc,ot,sa):
    new_list = ''
    alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    new_list = ''
    str = ''
    #ch = 'y'
    
    if direc == 'encode':
        for i in ot:
            x = 0
            #print(i)
            if i not in alphabets:
                new_list = new_list + i
            else:
                
                ind = alphabets.index(i)
                
                x = ind
                x = x + sa
                if x > 25:
                    remain = 25 - ind
                    #print(f'remain is {remain}')
                    x = sa - remain - 1
                    #print(f'x is {x}')
                    #print(x)
                    #new_list = new_list + alphabets[x]
                    #print(alphabets[x])
                new_list = new_list + alphabets[x]
                ch = 'n'
                    
        print(f'Original text is {ot}')
        print(f'Encoded list is {new_list}')
        ch = input('Do you want to continue(y/n)? \n')
        return ch
    elif direc == 'decode':
        for j in ot:
            x = 0
            #print(j)
            if j not in alphabets:
                str = str + j
            else:
                ind= alphabets.index(j)
                x = ind
                #print(f'index is {ind}')
                x = x - sa
                if x < 0:
                    #print(x)
                    #remain = ind - 0
                    #print(f'remain is {x}')
                    str = str + alphabets[x]
                    #print(alphabets[-2])
                    #remain = ind % 25
                   #print(f'remainder is {remain}')
                else: 
                    str = str + alphabets[x]
        print(f'Original text is {ot}')
        print(f'Encoded list is {str}')
        ch = 'n'
        ch = input('Do you want to continue(y/n)? \n')
        return ch
    else:
        print('Incorrect choice')
        ch = 'n'
        return ch
            

print(logo)
direction = input("Do you want to Encrypt(Encode) or Decrypt(Decode)? \n").lower()
if direction != 'encode' and direction != 'decode':
    print('Incorrect Choice. Good Bye!!!')
    quit()
original_text = input("Enter Text: \n").lower()
shift_amount = int(input("Enter shift amount: \n"))
ch = 'y'
ch = caesar(ch,direction,original_text,shift_amount)
#ch = input('Do you want to continue(y/n)? ')
#print(f'ch value outside definition is {ch}')
while ch == 'y':
    direction = input("Do you want to Encrypt(Encode) or Decrypt(Decode)? \n").lower()
    if direction != 'encode' and direction != 'decode':
        print('Incorrect Choice. Good Bye!!!')
        quit()
    original_text = input("Enter Text: \n").lower()
    shift_amount = int(input("Enter shift amount: \n"))
    ch = caesar(ch,direction,original_text,shift_amount)
    
else:
    print('Good Bye!!!')
