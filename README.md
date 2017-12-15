# Tic Tac Toe First Player Wining Percentage Analysis

### Team Member(s):
Zijun Cai

## Monte Carlo Simulation Scenario & Purpose:
Scenario: Two players automatically play tic tac toe game, using MiniMax Theorem, starting with a random opening move of both users. The user of this program can choose to be one of the user. He can choose the opening move position, how many time he wants to play this game in a roll, and the probability of being the first player in these games. The outcome of each round (contains many tries in a roll) is the winning percentage of the user.

  
Purpose: To explore the relationship between being the first player in this game and being the loser.


### Hypothesis before running the simulation:
Since I use MiniMax Theorem to optimize every move instead of going a random move, I think there is a linear negative correlation between the losing percentage of the user and the probability of being the first player. If there is 50% probability of the user to become the first player, the winning percentage may be 50% as well. If 100%, then almost 100% of wining percentage. If 0%, then almost 0% of wining percentage.

### Simulation's variables of uncertainty
The parameter of every round (K,N,P)
K -- the position of the open move of the first player
N -- times of playing tic tac toe game in a roll -- int in 500, 1000, 2000 or more (discrete)
P -- the probability of the user to be the first player in the round -- float between 0 and 1 (continuous distribution)

I choose optimized move using MiniMax Theorem instead of a random one, I believe the former one is more like a human act. So my projects is a representation of reality to some extent.

## Instructions on how to use the program:
Run Main.py

## Every try on game would be like this:
--Current board--
0 |1 |2 |
3 |4 |5 |
6 |7 |8 |
--Player1's Move--
--Current board--
0 |X |2 |
3 |4 |5 |
6 |7 |8 |
--Player2's Move--
--Current board--
0 |X |2 |
3 |4 |O |
6 |7 |8 |
--Player1's Move--
--Current board--
0 |X |X |
3 |4 |O |
6 |7 |8 |
--Player2's Move--
--Current board--
O |X |X |
3 |4 |O |
6 |7 |8 |
--Player1's Move--
--Current board--
O |X |X |
3 |X |O |
6 |7 |8 |
--Player2's Move--
--Current board--
O |X |X |
O |X |O |
6 |7 |8 |
--Player1's Move--
--Current board--
O |X |X |
O |X |O |
X |7 |8 |
Winner : X

## Sources Used:
https://en.wikipedia.org/wiki/Tic-tac-toe  
https://en.wikipedia.org/wiki/Minimax_theorem

