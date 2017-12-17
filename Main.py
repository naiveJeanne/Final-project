import random
import matplotlib.pyplot as plt

class Game:
    def __init__(self):
        self.board = ['-' for i in range(0, 9)]
        self.lastmoves = []
        self.winner = None

    def print_board(self):
        """
        Print the current game board
        :return:none
        """
        print("\n--Current board--")
        for j in range(0, 9, 3):
            for i in range(3):
                if self.board[j + i] == '-':
                    print("%d |" % (j + i), end="")
                else:
                    print("%s |" % self.board[j + i], end="")

            print("")

    def get_avail_positions(self):
        """
        Get the list of available positions
        :return: moves that still available
        """
        moves = []
        for i, v in enumerate(self.board):  # start from 1
            if v == '-':
                moves.append(i)
        return moves

    def mark(self, marker, pos):
        """
        Mark a position with marker X or O
        :param marker: the marker
        :param pos: the position
        :return: none
        """
        self.board[pos] = marker
        self.lastmoves.append(pos)

    def revert_last_move(self):
        """
        Reset the last move
        :return:none
        """
        self.board[self.lastmoves.pop()] = '-'
        self.winner = None

    def is_gameover(self):
        """
        Check whether the game has ended
        :return: true if game ended, false otherwise
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

            #self.print_board()

            if i % 2 == 0:
                #print("--Player1's Move--", end="")
                self.p1.move(self)
            else:
                #print("--Player2's Move--", end="")
                self.p2.move(self)

            if self.is_gameover():
                #self.print_board()
                if self.winner == '-':
                    #print("Game over with Draw")
                    return 0
                else:
                    #print("Winner : %s" % self.winner)
                    if (self.winner == 'X'):
                        return 1
                    if (self.winner == 'O'):
                        return 2

        #print("Game over with Draw")
        return 0

class AI:
    """
    Class for Automatic Player
    """
    def __init__(self, marker,start:int):
        self.marker = marker
        self.type = 'C'
        self.firstmove = True  # flag for first move
        self.start = start

        if self.marker == 'X':
            self.opponentmarker = 'O'
        else:
            self.opponentmarker = 'X'

    def move(self, gameinstance):
        if self.firstmove:
            if self.start == -1: move_position = random.randrange(0, 9)  # 1<=...<=9
            else: move_position = self.start
            self.firstmove = False
        else:
            move_position, score = self.maximized_move(gameinstance)
        gameinstance.mark(self.marker, move_position)

    def maximized_move(self, gameinstance):
        """
        Find maximized move
        :param gameinstance:
        :return:
        """
        bestscore = None
        bestmove = None

        for m in gameinstance.get_avail_positions():
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

        for m in gameinstance.get_avail_positions():
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
                return 1  # This player himself Won

            elif gameinstance.winner == self.opponentmarker:
                return -1  # The Opponent won

        return 0  # Draw


class MCS:  # for Monte Carlo Simulation
    def play1round(self, prob: float, count: int, start: int):
        """

        :param prob: probability of being player1
        :param count: total time of games played in this round
        :param start: first place the player1 want to move: valid number 0~8. -1 if goes a random first move.
        :return:
        """
        win = 0  # count the times of winning of user
        draw = 0  # count the times of game ending with draw

        # user is player1
        for i in range(int(count*prob)):
            game = Game()
            player1 = AI("X", start)
            player2 = AI("O", -1)
            res = game.play(player1, player2)
            if res == 1: win += 1
            elif res == 0: draw += 1

        # user is player2
        for i in range(int(count*(1.0-prob))):
            game = Game()
            player1 = AI("X", -1)
            player2 = AI("O", -1)
            res = game.play(player1, player2)
            if res == 2: win += 1
            elif res == 0: draw += 1
        print("time as player1", int(count*prob),";\ttime as player2", int(count*(1.0-prob)))
        return 100*float(win)/float(count), 100*float(draw)/float(count), 100*float(win)/float(count)+100*float(draw)/float(count)

    def all_1st_move_analysis(self):
        allPos = [1, 2, 3, 4, 5, 6, 7, 8, 9]  # index fo all positions
        win_of_AllPos = []
        draw_of_allPos = []
        win_draw_of_allPos = []
        for i in range(9):
            res=self.play1round(1, 5, i)
            win_of_AllPos.append(res[0])
            draw_of_allPos.append(res[1])
            win_draw_of_allPos.append(res[2])
        plt.plot(allPos, win_of_AllPos,linewidth=3,label="Win")
        plt.plot(allPos, draw_of_allPos,linewidth=3,label="Draw")
        plt.plot(allPos, win_draw_of_allPos,linewidth=3,label="Win & Draw")
        plt.title('Win/Draw/Win+Draw Percentage of the User when User is always the Player1')
        plt.xlabel('First Move Position of User')
        plt.ylabel('Win/Draw/Win+Draw Percentage of the User')
        plt.legend(('Win', 'Draw', 'Win & Draw'), loc='upper center', shadow=True)
        plt.show()


if __name__ == '__main__':
    mcs = MCS()
    mcs.all_1st_move_analysis()