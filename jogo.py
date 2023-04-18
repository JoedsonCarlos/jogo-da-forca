palavra_secreta='papai'
letras_corretas=''
tentativas=0

while True:

    
    letra= input('digite uma letra: ')
    tentativas+=1
    
    
    if len(letra ) > 1:
        print('digite só uma letra')
        continue

    if letra in palavra_secreta:
        letras_corretas+=letra
        

    palavra_formada= ''
        
    for palavra in palavra_secreta:
       
        if palavra in letras_corretas:
            palavra_formada+=palavra
           
        else:
            palavra_formada += '*'
            
    

    if tentativas>8:
        print('você passou do numero de tenta tivas permitido')
        break
    
    print(palavra_formada, tentativas )

    if palavra_formada==palavra_secreta:
        break

# jogo
# jogo
# jogo
# jogo-da-forca
