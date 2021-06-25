def win(letter_list, word):
    word_win = ''
    for win_loop in range(len(letter_list)):
        word_win = word_win + letter_list[win_loop]
    if word==word_win:
        print('\n Word: ', word_win)
        print ('\nYou win!')
        continue_game = input('Play again y/n: ')
        if continue_game== 'y' or 'Y':
            forca()
        
        elif continue_game== 'n' or 'N':
            input('Press any key to leave')
            exit()
        
        else:
            print('y/n')

    else:
        return(word_win)

        
def forca():  
    word = ''
    letter = ''
    life = 5
    wrong_letter = []
    word_ingame = []
    word_win = ''
    dead_letter = ''

    word=(input('Select your word: '))

    for loop in range(len(word)):
        word_ingame.append('_')
        
    while life>0 or word==word_win:
        letter=(input('Select your try (letter): '))    
        if (len(letter)) < 2:
            if not letter in dead_letter:
                dead_letter = dead_letter+letter
            if letter in word:
                for replacer in range(len(word)):
                    if word_ingame[replacer] != letter:    
                        if word[replacer] == letter:
                            word_ingame[replacer] = letter
                word_win = win(word_ingame, word)
                letter = ''
                forca = []
                        
                print ('\nWrongs letters:', wrong_letter)
                print ('\nDead letters: ', dead_letter)
                print('\n\nWord: ', word_win)
                print('\n\nLife:', life)
            else:
                if letter in dead_letter:
                    print('You alredy try this letter')
                    letter = ''
                    forca = []
                else:
                    wrong_letter.append(letter)
                    
                    word_win = win(word_ingame, word)
                    life=life-1
                    letter = ''
                    forca = []
                    
                    print ('\nWrongs letters:', wrong_letter)
                    print ('\nDead letters: ', dead_letter)
                    print('\nWord: ', word_win)
                    print('\nLife:', life)             
        else:
            print ('\nOnly one letter!\n\n')
        word_win = win(word_ingame, word)
    print('\nThis was the word: ', word)
    print('\nYou lose, NOOB!')
    input('Press any key to leave')
forca()
