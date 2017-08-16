
# coding: utf-8

# # Single Pile Nim Game - SCU AMTH 377/ COEN 279

# ### Group: Minh Do, Troy Ibanez, Angela Lam, Marcos Alvarez, Susan Xie.

# This is an implementation of a Wining_Move function for a Single-Pile Nim Game. 
# #### Overview
# * The game starts with a pile of N nims. Two players take turns to remove nims from the pile. The one who removes the last nim wins.
# * On the first move, the player who starts can remove a maximum of N-1 nims.
# * After that, players can take a maximum of twice the number of nims the previous player took.
# * 0 move is not allowed.
# 

# ### Possible solutions
# There are several aproaches to this game.
# * Fibbonaci Sequence: In order for Player 1 to win, she must try to leave Player 2 with a number of nims that is in the Fibbonaci sequence. To ensure that, she must find all the previous numbers of the fibbonaci sequence up to N, and try to make Player 2 stay in those numbers. To do that, Player 1 should divide the problem into smaller problems, and look at the difference between N and its closest smaller Fib number as a new pile. The new pile would have to be also divided Fibo numbers, and so on. This is a recursive solution. It is a bottom-up solution.
# 
# * Dynamic Programming: This approach makes no assumptions whatsoever. The main idea behind this algorithm is to explore all possible ways to leave the other player without a Winning_Move. The recursion in this algorithm comes into play by recursively solving smaller problems. It is an up-bottom solution. 
# 
# In our solution, we will let the machine make its own decissions independently with no a-priori information of a winning strategy, but just the rules of the game. Thus, we will implement the Dynamic Programming approach.
# 
# 

# ### Solution:
# * N( i ) = Pile of items
# * q( i ) = Max allowable items to pick
# * W(i) = Move(N(i), q(i), i)  is winning pick
# * Pick W(i) such that N(i) - 2 * W(i) > 0 and place the player in the stable winning position throughout the subsequent turns
# 

# In[65]:

from random import randint
import math
max_moves = {}  #makes a hashmap for easy lookup (so program doesn't take forever)


# In[66]:

def winning_move(pile, n_max_move):
  if pile <= n_max_move:  #if your max move is the same as your pile, you win
    return pile
  for move in range(n_max_move, 0, -1):   #cycle through all your options
    new_pile = pile - move       #your opponent's pile is based on how many you take
    new_max = min(new_pile, 2 * move)
    if (new_pile, new_max) in max_moves:    #if we've done this combo before
      opponent_move = max_moves[new_pile, new_max]    #read the value from the hashmap
    else:
      opponent_move = winning_move(new_pile, new_max)  #else, call winningmove for your opponent
      max_moves[new_pile, new_max] = opponent_move            #add the value to the hashmap
    if opponent_move == 0:                #if your opponent has no winning moves
      return move        #return the number of chips you took
  return 0            #if you've gone through all your options and your opponent always had winning moves, you don't have a winning move


# In[86]:

def simulatedGame(ipile):
    imaxMoves=ipile-1
    print "\t\t ----STARTING A SIMULATED GAME---"
    print "\t\t ------Player 2 takes random-----"
    p1 = winning_move(ipile, imaxMoves)
    if p1==0:
        if imaxMoves<4:
            p1=1
        else:
            p1=randint(1, math.ceil(imaxMoves/4))
        print "Starting pile is %d. Player 1 does not have any move that guarantees victory. Randomly takes %d" %(ipile, p1)
    else:
        print "Starting pile is %d . Player 1 starts. Max-move is %d. Winning-number is %d " %(ipile, imaxMoves, p1)
    ipile=ipile-p1
    imaxMoves=2*p1
    player = 2
    while ipile>0:
        if player == 2:
            if ipile<=imaxMoves:
                p2 = ipile
            else:
                p2 = randint(1, imaxMoves)
            print "The pile is %d . Max-move is %d . Player 2 takes %d " %(ipile, imaxMoves, p2)
            ipile=ipile-p2
            imaxMoves=2*p2
        if player == 1: 
            p1 = winning_move(ipile, imaxMoves)
            if p1==0:
                pi=randint(1, imaxMoves)
                print "Player 1: Pile is %d. There is not any move that guarantees victory. Takes %d" %(ipile, p1)
            else:
                print "Player 1: Pile is %d . Max-move is %d. Winning-number is %d " %(ipile, imaxMoves, p1)
            ipile=ipile-p1
            imaxMoves=2*p1
        if player == 2:
            player = 1
        else:
            player = 2
    if player == 1:
        print "Player 2 wins."
    else:
        print "Player 1 wins."
    
    


# ### Testing: (Asumption that both players use the same strategy)

# In[87]:

def main(ipile):
    original = ipile
    imaxMoves = ipile-1
    m = winning_move(ipile, imaxMoves)
    print "\t Starting pile: is %d, Player1 max-move is %d,  and winning-number is %d" %(ipile, imaxMoves, m)
    if (m == 0):
        print "\t Winning-number is %d. Player 1 has no movements that would lead to a win." %(m)
        simulatedGame(original)
        return 0
    iturn = 1
    while (ipile > 0 and imaxMoves > 0 and ipile > m):
        iturn=iturn+1
        if (iturn % 2 == 0):
            player = 2
        else:
            player = 1
        ipile = ipile - m
        imaxMoves = m * 2
        m = winning_move(ipile, imaxMoves)
        if (m == 0):
            print "\t pile: is %d, Player%d max-move is %d,  and winning-number is %d. So Player%d has no moves that would lead to a win." %(ipile, player, imaxMoves, m, player)
            #simulatedGame(original)
            break
        print "\t pile: is %d, Player%d max-move is %d,  and winning-number is %d" %(ipile, player, imaxMoves, m)

    simulatedGame(original)
main(3)


# In[ ]:




# In[ ]:



