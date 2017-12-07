class Game:
    def __init__(self):
        self.board = ['-' for i in range(0, 9)]
        self.lastmoves = []
        self.winner = None

    def print_board(self):
        """
        Print the current game board
        :return:
        """
        print("\nCurrent board:")
        for j in range(0, 9, 3):
            for i in range(3):
                if self.board[j + i] == '-':
                    print("%d |" % (j + i),end="")
                else:
                    print("%s |" % self.board[j + i],end="")

            print("")

    def get_free_positions(self):
        """
        Get the list of available positions
        :return:
        """
        moves = []
        for i, v in enumerate(self.board):
            if v == '-':
                moves.append(i)
        return moves

    def mark(self, marker, pos):
        """
        Mark a position with marker X or O
        :param marker:
        :param pos:
        :return:
        """
        self.board[pos] = marker
        self.lastmoves.append(pos)


    def revert_last_move(self):
        """
        Reset the last move
        :return:
        """
        self.board[self.lastmoves.pop()] = '-'
        self.winner = None

    def is_gameover(self):
        """
        Test whether game has ended
        :return:
        """

        win_positions = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]

        for i, j, k in win_positions:
            if self.board[i] == self.board[j] == self.board[k] and self.board[i] != '-':
                self.winner = self.board[i]
                return True

        if '-' not in self.board:
            self.winner = '-'
            return True

        return False

    def play(self, player1, player2):
        """
        Execute the game play with players
        :param player1:
        :param player2:
        :return:
        """

        self.p1 = player1
        self.p2 = player2

        for i in range(9):

            self.print_board()

            if i % 2 == 0:
                if self.p1.type == 'H':
                    print("[Human's Move]",end="")
                else:
                    print("[Computer's Move]",end="")

                self.p1.move(self)
            else:
                if self.p2.type == 'H':
                    print("[Human's Move]",end="")
                else:
                    print("[Computer's Move]",end="")

                self.p2.move(self)

            if self.is_gameover():
                self.print_board()
                if self.winner == '-':
                    print("Game over with Draw")
                else:
                    print("Winner : %s" % self.winner)
                return

class Human:
    def __init__(self, marker):
        self.marker = marker
        self.type = 'H'

    def move(self, gameinstance):

        while True:

            m = input("Input position:")

            try:
                m = int(m)
            except:
                m = -1

            if m not in gameinstance.get_free_positions():
                print("Invalid move. Retry")
            else:
                break

        gameinstance.mark(self.marker, m)


class AI:
    """
    Class for Computer Player
    """

    def __init__(self, marker):
        self.marker = marker
        self.type = 'C'

        if self.marker == 'X':
            self.opponentmarker = 'O'
        else:
            self.opponentmarker = 'X'

    def move(self, gameinstance):
        move_position, score = self.maximized_move(gameinstance)
        gameinstance.mark(self.marker, move_position)

    def maximized_move(self, gameinstance):
        #  Find maximized move'''
        bestscore = None
        bestmove = None

        for m in gameinstance.get_free_positions():
            gameinstance.mark(self.marker, m)

            if gameinstance.is_gameover():
                score = self.get_score(gameinstance)
            else:
                move_position, score = self.minimized_move(gameinstance)

            gameinstance.revert_last_move()

            if bestscore == None or score > bestscore:
                bestscore = score
                bestmove = m

        return bestmove, bestscore

    def minimized_move(self, gameinstance):
        """
        Find the minimized move
        :param gameinstance:
        :return:
        """

        bestscore = None
        bestmove = None

        for m in gameinstance.get_free_positions():
            gameinstance.mark(self.opponentmarker, m)

            if gameinstance.is_gameover():
                score = self.get_score(gameinstance)
            else:
                move_position, score = self.maximized_move(gameinstance)

            gameinstance.revert_last_move()

            if bestscore == None or score < bestscore:
                bestscore = score
                bestmove = m

        return bestmove, bestscore

    def get_score(self, gameinstance):
        if gameinstance.is_gameover():
            if gameinstance.winner == self.marker:
                return 1  # Won

            elif gameinstance.winner == self.opponentmarker:
                return -1  # Opponent won

        return 0  # Draw

if __name__ == '__main__':
    game = Game()
    player1 = Human("X")
    player2 = AI("O")
    game.play(player1, player2)