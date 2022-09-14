mood = 'hungry'

match mood:
    case 'hungry':
        print('get some food')
    case 'thirsty':
        print('get some water')
    case 'tired':
        print('get some rest')
    case _:
        print('any other mood')
