#Caesar Cipher- Encryption
def encrypt(ot,sa):
    new_list = ''
    alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    for i in ot:
        x = 0
        #print(i)
        
        ind= alphabets.index(i)
        x = ind
        x = x + sa
        if x > 25:
            remain = 25 - ind
            #print(f'remain is {remain}')
            x = sa - remain - 1
            #print(f'x is {x}')
        #print(x)
        new_list = new_list + alphabets[x]
        #print(alphabets[x])
    #print(ot)
    #print(sa)
    print(f'Original text is {ot}')
    print(f'Encoded list is {new_list}')
original_text = input("Enter Text: \n").lower()
shift_amount = int(input("Enter shift amount: \n"))
encrypt(original_text,shift_amount)
