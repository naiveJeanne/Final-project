import random
import matplotlib.pyplot as plt
import numpy as np


class Game:
    def __init__(self):
        self.board = ['-' for i in range(0, 9)]
        self.lastmoves = []
        self.winner = None

    def print_board(self):
        """
        Print the current game board
        :return: none
        >>> g = Game()
        >>> g.print_board()
        <BLANKLINE>
        --Current board--
        0 |1 |2 |
        3 |4 |5 |
        6 |7 |8 |
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
        :return: moves that still available (from 0 to 8)
        >>> g = Game()
        >>> g.get_avail_positions()
        [0, 1, 2, 3, 4, 5, 6, 7, 8]
        """
        moves = []
        for i, v in enumerate(self.board):  # start from 0
            if v == '-':
                moves.append(i)
        return moves

    def mark(self, marker, pos):
        """
        Mark a position with marker X or O
        :param marker: the marker X or O
        :param pos: the position index
        :return: none
        >>> g = Game()
        >>> g.board
        ['-', '-', '-', '-', '-', '-', '-', '-', '-']
        >>> g.mark('X',1)
        >>> g.board
        ['-', 'X', '-', '-', '-', '-', '-', '-', '-']
        """
        self.board[pos] = marker
        self.lastmoves.append(pos)

    def revert_last_move(self):
        """
        Revert the last move
        :return: none
        >>> g = Game()
        >>> g.board
        ['-', '-', '-', '-', '-', '-', '-', '-', '-']
        >>> g.mark('X',1)
        >>> g.board
        ['-', 'X', '-', '-', '-', '-', '-', '-', '-']
        >>> g.revert_last_move()
        >>> g.board
        ['-', '-', '-', '-', '-', '-', '-', '-', '-']
        """
        self.board[self.lastmoves.pop()] = '-'
        self.winner = None

    def is_gameover(self):
        """
        Check whether the game has ended
        :return: true if game ended, false otherwise
        >>> g = Game()
        >>> g.is_gameover()
        False
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
        Execute the game with 2 players
        :param player1: Automatic Player1
        :param player2: Automatic Player2
        :return: 0 if game ends with draw, 1 if player1 wins, 2 if player2 wins
        """

        self.p1 = player1
        self.p2 = player2

        for i in range(9):

            # self.print_board()

            if i % 2 == 0:
                # print("--Player1's Move--", end="")
                self.p1.move(self)
            else:
                # print("--Player2's Move--", end="")
                self.p2.move(self)

            if self.is_gameover():
                # self.print_board()
                if self.winner == '-':
                    # print("Game over with Draw")
                    return 0
                else:
                    # print("Winner : %s" % self.winner)
                    if (self.winner == 'X'):
                        return 1
                    if (self.winner == 'O'):
                        return 2

        # print("Game over with Draw")
        return 0


class AI:
    """
    Class for Automatic Player
    """

    def __init__(self, marker, start: int):
        self.marker = marker
        self.firstmove = True  # flag for first move
        self.start = start

        if self.marker == 'X':
            self.opponentmarker = 'O'
        else:
            self.opponentmarker = 'X'

    def move(self, gameinstance):
        """
        make a move in the board of game instance with mark
        :param gameinstance: a game instance with a board
        :return: none
        >>> g = Game()
        >>> player = AI('X',2)
        >>> player.move(g)
        >>> g.board
        ['-', '-', 'X', '-', '-', '-', '-', '-', '-']
        """
        if self.firstmove:
            if self.start == -1:
                move_position = random.randrange(0, 9)  # 1<=...<=9
            else:
                move_position = self.start
            self.firstmove = False
        else:
            move_position, score = self.maximized_move(gameinstance)
        gameinstance.mark(self.marker, move_position)

    def maximized_move(self, gameinstance):
        """
        Find the best move for the player himself. It is the best situation for the player who call this funtion.
        :param gameinstance: a game instance with a board.
        :return: move postion index of the player (int), score of the final result if the player makes this move (int)
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
        Find the worst move for opponent. It is the best situation for the player who call this funtion.
        :param gameinstance: a game instance with a board.
        :return: move postion index of the opponent (int), score of the final result if the opponent makes this move (int)
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
        """
        get the final result of game
        :param gameinstance: a game instance with a board.
        :return: 0 if the game ends with draw, 1 if the player who call this function wins, -1 if the opponent wins
        """
        if gameinstance.is_gameover():
            if gameinstance.winner == self.marker:
                return 1  # This player himself Won

            elif gameinstance.winner == self.opponentmarker:
                return -1  # The Opponent won

        return 0  # Draw


class MCS:  # for Monte Carlo Simulation
    def play1round(self, prob: float, count: int, start: int):
        """
        play <count> times of games with the probability <prob> of being the player1 & with the 1st move index <start>
        :param prob: probability of being player1
        :param count: total time of games played in this round
        :param start: first place the player1 want to move: valid number 0~8. -1 if goes a random first move.
        :return: win percentage, draw percentage, win+draw percentage
        """
        win = 0  # count the times of winning of user
        draw = 0  # count the times of game ending with draw

        # user is player1
        for i in range(int(count * prob)):
            game = Game()
            player1 = AI("X", start)
            player2 = AI("O", -1)
            res = game.play(player1, player2)
            if res == 1:
                win += 1
            elif res == 0:
                draw += 1

        # user is player2
        for i in range(int(count * (1.0 - prob))):
            game = Game()
            player1 = AI("X", -1)
            player2 = AI("O", -1)
            res = game.play(player1, player2)
            if res == 2:
                win += 1
            elif res == 0:
                draw += 1
        print("time as player1", int(count * prob), ";\ttime as player2", int(count * (1.0 - prob)))
        return 100 * float(win) / float(count), 100 * float(draw) / float(count), 100 * float(win) / float(
            count) + 100 * float(draw) / float(count)

    def all_1st_move_analysis(self, times: int):
        """
        Try <times> of game in a round with different first move position (0 ~ 8).
        Create a line chart of the result with 3 lines.
        :param times: the number of games executed in a round
        :return: none
        """
        allPos = [1, 2, 3, 4, 5, 6, 7, 8, 9]  # index fo all positions. show them as 1 ~ 9 for easier read.
        win_of_AllPos = []  # time of win in the round
        draw_of_allPos = []  # time of draw in the round
        win_draw_of_allPos = []  # time of win plus draw in the round
        for i in range(9):
            res = self.play1round(1, times, i)
            win_of_AllPos.append(res[0])
            draw_of_allPos.append(res[1])
            win_draw_of_allPos.append(res[2])
        plt.figure()
        plt.plot(allPos, win_of_AllPos, linewidth=3, label="Win")
        plt.plot(allPos, draw_of_allPos, linewidth=3, label="Draw")
        plt.plot(allPos, win_draw_of_allPos, linewidth=3, label="Win & Draw")
        plt.title('Win/Draw/Win+Draw Percentage of User with Different Percentage of Being Player1 (' + str(
            times) + ' times)')
        plt.xlabel('First Move Position index of User')
        plt.ylabel('Win/Draw/Win+Draw Percentage of User')
        plt.legend(('Win', 'Draw', 'Win & Draw'), loc='upper center', shadow=True)

    def player1_win_percentage_analysis(self, times: int):
        """
        Try <times> of game in a round with different probability of being the player1 of user.
        Create a line chart of the result with 3 lines.
        :param times: the number of games executed in a round
        :return: none
        """
        all_probability = np.arange(0.0, 1.02, 0.02)  # index fo all positions
        win_of_AllPos = []  # time of win in the round
        draw_of_allPos = []  # time of draw in the round
        win_draw_of_allPos = []  # time of win plus draw in the round
        for i in all_probability:
            res = self.play1round(i, times, -1)
            win_of_AllPos.append(res[0])
            draw_of_allPos.append(res[1])
            win_draw_of_allPos.append(res[2])
        plt.figure()
        plt.plot(all_probability, win_of_AllPos, linewidth=3, label="Win")
        plt.plot(all_probability, draw_of_allPos, linewidth=3, label="Draw")
        plt.plot(all_probability, win_draw_of_allPos, linewidth=3, label="Win & Draw")
        plt.title('Win/Draw/Win+Draw Percentage of User with Different Percentage of Being Player1 (' + str(
            times) + ' times)')
        plt.xlabel('Percentage of being Player1 of User')
        plt.ylabel('Win/Draw/Win+Draw Percentage of User')
        plt.legend(('Win', 'Draw', 'Win & Draw'), loc='upper center', shadow=True)


if __name__ == '__main__':
    mcs = MCS()
    mcs.all_1st_move_analysis(50)
    mcs.all_1st_move_analysis(100)
    mcs.all_1st_move_analysis(1000)
    mcs.player1_win_percentage_analysis(50)
    mcs.player1_win_percentage_analysis(100)
    mcs.player1_win_percentage_analysis(1000)
    plt.show()
