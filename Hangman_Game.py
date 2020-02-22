import random as rd


if __name__ == '__main__':
    # database of words
    database = []
    file = open('Hangman_wordbank.txt','r')
    for line in file:
        database.extend(line.rstrip().split(', '))

    # randomly select one and take off some characters
    word = list(database[rd.randint(0,len(database))])
    word_copy = word.copy()
    answer = ''.join(word)

    for i in range(len(word_copy)):
        word_copy[i] = '_'


    print(' '.join(word_copy))

    # Game part
    limit = 0
    while limit <= 6 and '_' in word_copy:
        print("\nPlease enter your guess: ")
        input_char = input()
        if input_char.isalpha():
            if input_char in word:
                print("\nCorrect!")

                index_to_change = []
                for i in range(len(word)):
                    if word[i] == input_char:
                        index_to_change.append(i)

                for ind in index_to_change:
                    word_copy[ind] = input_char

                print(' '.join(word_copy))
            else:
                limit += 1
                print(f"Wrong guess! Remaining {6 - limit + 1} attempts !")
        else:
            limit += 1
            print(f"Not a valid input! Remaining {6 - limit + 1} attempts !")

    if '_' not in word_copy:
        print("\nSuccess!")
    else:
        print("\nYou failed! Hahaha, Im gonna laugh at you!")
        print(f"\nCorrect answer is \n \n{answer}\n")
