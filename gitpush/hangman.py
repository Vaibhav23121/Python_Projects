import random
# from hangman_words import words
words=["apple","car","men","aeroplane","banana","cherry","date","elderberry","fig","grape","honeydew","kiwi","lemon","mango","nectarine","orange","peach","quince","raspberry","strawberry","tangerine","watermelon","zucchini","bike","bus","honda","yellow","blue","red","green","white","black","orange","yellow","blue","red","green","white","black"]
print('''

██╗░░██╗░█████╗░███╗░░██╗░██████╗░███╗░░░███╗░█████╗░███╗░░██╗
██║░░██║██╔══██╗████╗░██║██╔════╝░████╗░████║██╔══██╗████╗░██║
███████║███████║██╔██╗██║██║░░██╗░██╔████╔██║███████║██╔██╗██║
██╔══██║██╔══██║██║╚████║██║░░╚██╗██║╚██╔╝██║██╔══██║██║╚████║
██║░░██║██║░░██║██║░╚███║╚██████╔╝██║░╚═╝░██║██║░░██║██║░╚███║
╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝░╚═════╝░╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝
''')

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

# lst=["apple","banana","cherry","date","elderberry","fig","grape","honeydew","kiwi","lemon","mango","nectarine","orange","peach","quince","raspberry","strawberry","tangerine","watermelon","zucchini"]
word=random.choice(words)
print(word)
print(" The length of word is",len(word))
print("_"*(len(word)))

n=len(word)

correct="_"*(len(word)+1)
gameover=False
correctletter=[]
lives=6
print(word)
while not gameover:
    print(f"********************************************************************{lives} LIVES LEFT********************************************************************")
    guess=input("enter the letter : ")
    if guess in correctletter:
        print(f"you already guessed this letter {guess}")
    display=""
    for letter in word:
        if letter==guess:
            display+=letter
            correctletter.append(letter)
        elif letter in correctletter:
            display+=letter
        else:
                display+='_'
                
    print("Words to guess" + display)
    if guess not in word:
        lives-=1
        if lives==0:
            gameover=True
            print('''██    ██  ██████  ██    ██     ██       ██████  ███████ ████████ 
 ██  ██  ██    ██ ██    ██     ██      ██    ██ ██         ██    
  ████   ██    ██ ██    ██     ██      ██    ██ ███████    ██    
   ██    ██    ██ ██    ██     ██      ██    ██      ██    ██    
   ██     ██████   ██████      ███████  ██████  ███████    ██    
                                                                 
                                                                 ''')
    print(stages[lives])
    if"_" not in display:
        gameover=True
        print('''██    ██  ██████  ██    ██     ██     ██ ██ ███    ██ 
 ██  ██  ██    ██ ██    ██     ██     ██ ██ ████   ██ 
  ████   ██    ██ ██    ██     ██  █  ██ ██ ██ ██  ██ 
   ██    ██    ██ ██    ██     ██ ███ ██ ██ ██  ██ ██ 
   ██     ██████   ██████       ███ ███  ██ ██   ████ 
                                                      
                                                      ''')
# print(''.join([guess if letter==guess else "_" for letter in word]))
# n-=1
    
