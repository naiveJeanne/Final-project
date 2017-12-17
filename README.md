# Tic Tac Toe Wining Percentage Analysis  
  
Team Member:  Zijun Cai  
  
## Monte Carlo Simulation Scenario & Purpose:  
### Scenario:  
Two players automatically play tic tac toe game in a round, using MiniMax Theorem. Each round executes many tries on this game. The user can choose two aspect of analysis  
1. All 1st move position analysis  
   - User can decide the first move position. 
   - In this case, user is always the first player in this round.  
   - The program is set to execute games with every possible postion, via the function "all_1st_move_analysis" of class MCS.  
2. All probability of being the player1 analysis  
   - User can decide the probablity of being the first player in this round. 
   - In this case, user goes a random move in every game.
   - The program is set to execute games with a continous probability from 0 to 1 of being the first player in a round, via the function "player1_win_percentage_analysis" of class MCS.
  
The outcome of each round (contains many tries in a roll) is the winning percentage of the user.  
  
    
### Purpose:  
To explore the relationship between 
- being the first player in this game and being the winner  
- the first move position and being the winner    
  
  
### Hypothesis before running the simulation:  
Since I use MiniMax Theorem to optimize every move instead of going a random move, I think  
**1. For 1st move position:** When choosing the central position of the board as the opening move, the winning percentage of user would be highest. Choosing other positions would lead to relatively lower winning percantage in a round.

**2. For probability of being the player1:** There is a linear positive correlation between the winning percentage of the user and the probability of being the first player. If there is 50% probability of the user to become the first player, the winning percentage may be around 50% as well. If 100%, then around 100% of wining percentage. If 0%, then around 0% of wining percentage.

### Simulation's variables of uncertainty
The parameter of every round (K,N,P)  
- K 
  - the position of the open move of the first player 
  - int in 1, 2, 3, 4, 5, 6, 7, 8 (discrete distribution)  
- N 
  - times of playing tic tac toe games in a roll 
  - int in 50, 100, 1000 (discrete distribution)  
- P 
  - the probability of the user to be the first player in the round 
  - float between 0 and 1 with gap 0.02 (continuous distribution)  

Since I choose optimized move using MiniMax Theorem instead of a random one, I believe the former one is more like a human act. So my projects is a representation of reality to some extent.  
  
## Instructions on how to use the program:  
Run Main.py and there will be plots of all first move position result and all probability of being the player1 result, with 50, 100 and 1000 tries in a round. 
  
## Report
### Game Virtualization
(This function is turned off by annotation in the program)  
One try on this game would be like this:  
Player1: X  
Player2: O  
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
  
### Plot & Analysis
1. All 1st move position analysis  
  ![figure_1](https://user-images.githubusercontent.com/16079206/34077870-ea72e522-e2d3-11e7-822b-8c232fec01df.png)  
  ![figure_2](https://user-images.githubusercontent.com/16079206/34077877-06c34bfe-e2d4-11e7-83ea-210b7f78ae2f.png)  
  ![figure_3](https://user-images.githubusercontent.com/16079206/34077878-0b50edac-e2d4-11e7-8934-79de65d0cb03.png)  
As we can see in the plots, choosing the corner position 1, 3, 7 or 9 in opening move has the highest winning percentage. Choosing other postitions has same lower winning percentage. This is different from what I expect. I thought take the central position of the board is the best.  
  
2. All probability of being the player1 analysis  
  ![figure_4](https://user-images.githubusercontent.com/16079206/34077879-0b5d9764-e2d4-11e7-8150-df836436631d.png)  
  ![figure_5](https://user-images.githubusercontent.com/16079206/34077880-0b6cb80c-e2d4-11e7-9973-ee9f57a12a01.png)  
  ![figure_6](https://user-images.githubusercontent.com/16079206/34077881-0b7c4042-e2d4-11e7-9c3b-9a4d0e636013.png)  
As we can see in the plots, there is a linear positive correlation between the winning percentage of the user and the probability of being the first player, which is the same as my hypothesis.  
  However, I expected 100% winning percentage of user when he has 100% probability of being the first player, 50% to 50%, and 0% to 0%. While the result is 50% winning percentage of user when he has 100% probability of being the first player, 25% to 50%, and 0% to 0%. When plusing the percentage of game ending with draw, the total percentage of win plus draw to probability of being the first player is the relationship of 100% to 100%, 50% to 50%, 0% to 0%. This is a little confusing.  
   
## Conclusion
1. Choosing the corner position of the board as opening move has the highest winning probability.  
2. Choosing to be the first player is the key to win. There is a linear positive correlation between the winning percentage of the user and the probability of being the first player.  

## Sources Used:  
https://en.wikipedia.org/wiki/Tic-tac-toe  
https://en.wikipedia.org/wiki/Minimax_theorem

