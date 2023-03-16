#Programa usando Match-case para reconocer las empciones de una persona e imprimir emoji..
Emocion='Enojado'

match Emocion:
    case 'Feliz':
        print('\U0001F600')
    case 'Triste':
        print('\U0001F62D')
    case 'Enojado':
        print('\U0001F621')
    case 'Enamorado':
        print('\U0001F60D')
