
# Single-Pile_Nim_Game
## SCU AMTH 377/ COEN 279: Minh Do, Troy Ibanez, Angela Lam, Marcos Alvarez, Susan Lie, Stephen Chen.

This is an implementation of a Wining_Move function for a Single-Pile Nim Game.
### Overview¶ 
The game starts with a pile of N nims. Two players take turns to remove nims from the pile. The one who removes the last nim wins.
On the first move, the player who starts can remove a maximum of N-1 nims.
After that, players can take a maximum of twice the number of nims the previous player took.
0 move is not allowed.

### Possible solutions
There are several aproaches to this game.
* Fibbonaci Sequence: In order for Player 1 to win, she must try to leave Player 2 with a number of nims that is in the Fibbonaci sequence. To ensure that, she must find all the previous numbers of the fibbonaci sequence up to N, and try to make Player 2 stay in those numbers. To do that, Player 1 should divide the problem into smaller problems, and look at the difference between N and its closest smaller Fib number as a new pile. The new pile would have to be also divided Fibo numbers, and so on. This is a recursive solution. It is a bottom-up solution.
* Dynamic Programming: This approach makes no assumptions whatsoever. The main idea behind this algorithm is to explore all possible ways to leave the other player without a Winning_Move. The recursion in this algorithm comes into play by recursively solving smaller problems. It is an up-bottom solution.

In our solution, we will let the machine make its own decissions independently with no a-priori information of a winning strategy, but just the rules of the game. Thus, we will implement the Dynamic Programming approach.
