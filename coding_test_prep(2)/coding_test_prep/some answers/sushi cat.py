sushi_dict = {'meow': 'I am hungry!', 
    'meeoow': 'I am bored!', 'mmmeow': 'Nap time.', 
    'meoooow': 'Pet me!', 'meooooww': 'Enough!', 
    'meoooooooww': 'How dare you human!'}

def translator_word(dictionary,word):
    if word in dictionary:
        print(dictionary[word])
    else:
        print(word)


def translator(dictionary, sentence):
    words=sentence.split()
    translation=[]
    for word in words:
        if word in dictionary:
            translation.append(dictionary[word])
        else:
            tranlation.append(word)