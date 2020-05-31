game = [[0,0,0],
        [0,0,0],
        [0,0,0]]


user_input = int(input('Which value: '))
user_row = int(input('Which row: '))
user_column = int(input('Which column: '))

def game_board(game_map,player=0 ,row=0 ,column=0, just_display=False):
        try:
                print('   a  b  c')
                if not just_display:
                        game[row][column] = player
                for count, row in enumerate(game_map):
                        print(count, row)
                return game_map
        except IndexError as ie:
                print("ERROR: Make sure you input row/column as 0,1 or 2?", ie)

        except Exception as ve:
                print("ERROR: Something went very wrong!", ve)

game = game_board(game, just_display=True)
game = game_board(game,player=user_input, row=user_row, column=user_column)









