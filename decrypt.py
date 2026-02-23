def decrypt(ot,sa):
    new_list = ''
    alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    str = ''
    for j in ot:
        x = 0
        #print(j)
        
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
    #str = str + alphabets[x] 
        else: 
            str = str + alphabets[x]
    print(f'New text is {str}')
            
        
original_text = input("Enter Text: \n").lower()
shift_amount = int(input("Enter shift amount: \n"))
decrypt(original_text,shift_amount)
