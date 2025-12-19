import random

class TicTacToe:
    def __init__(self):
        """ Initialize the game board and randomly select the first player (X or O).
        """
        self.board = [' '] * 10   # list(map(str, range(10)))
        self.player_turn = self.get_random_first_player()
        
    def show_board(self):
        print('\n')
        print(self.board[1] +  '|' + self.board[2] + '|' + self.board[3])
        print('-----')
        print(self.board[4] +  '|' + self.board[5] + '|' + self.board[6])
        print('-----')
        print(self.board[7] +  '|' + self.board[8] + '|' + self.board[9])
        print('\n')
    
    def get_random_first_player(self) -> str:
        """ Randomly select the first player (X or O) to start the game.

        :return: A string representing the first player ('X' or 'O').
        """
        return random.choice(['X', 'O'])
    
    def swap_player_turn(self) -> str:
        """ Swap the current player's turn between 'X' and 'O'.

        :return: The new player ('X' or 'O').
        """
        self.player_turn = 'X' if self.player_turn == 'O' else 'O'
        return self.player_turn
    
    def is_board_filled(self) -> bool:
        """ Check if the board is completely filled.

        :return: True if the board is filled, False otherwise.
        """
        return ' ' not in self.board[1:]
    
    def fix_spot(self, cell: int, player: str):
        """ Place the player's mark on the specified cell of the board.

        :param cell: The cell number (1-9) where the player wants to place their mark.
        :param player: The player's mark ('X' or 'O').
        """
        self.board[cell] = player
        
    def has_player_won(self,player: str) -> bool:
        """ Check if the specified player has won the game by having three of their marks 
        in a row, column, or diagonal.

        :param player: The player's mark ('X' or 'O').
        :return: True if the player has won, False otherwise.
        """
        win_combinations = [
            [1, 2, 3], [4, 5, 6], [7, 8, 9], #row
            [1, 4, 7], [2, 5, 8], [3, 6, 9], #col
            [1, 5, 9], [3, 5, 7] # diagonal
        ]
        for combination in win_combinations:
            if all (self.board[cell] == player for cell in combination):
                return True
        
        return False
    
    def start_game(self):
        """ Start the main game loop, allowing players to take turns until there is a winner or a draw.
        """
        while True:
            self.show_board()
            print(f'Player {self.player_turn} turn:')
            cell = int(input('Enter a cell from 1 to 9: '))
            
            if (cell in range(1, 10) and self.board[cell] == ' '):
                self.fix_spot(cell, self.player_turn)
                
                if self.has_player_won(self.player_turn):
                    self.show_board()
                    print(f'Player {self.player_turn} has won!')
                    break
                
                if self.is_board_filled():
                    self.show_board()
                    print('Draw!')
                    break
                
                self.swap_player_turn()
            else:
                print('Invalid cell number!')

if __name__ == '__main__':
    game = TicTacToe()
    game.start_game()