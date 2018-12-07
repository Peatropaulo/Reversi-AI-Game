'''
Compute the value brought by a given move by placing a new token for player
at (row, column). The value is the number of opponent pieces getting flipped
by the move. 

A move is valid if for the player, the location specified by (row, column) is
(1) empty and (2) will cause some pieces from the other player to flip. The
return value for the function should be the number of pieces hat will be moved.
If the move is not valid, then the value 0 (zero) should be returned. Note
here that row and column both start with index 0. 
'''
import os
def get_move_value(state, player, row, column):
    flipped = 0
    # Your implementation goes here
    #Checks for used space
    if state[row][column]=='B' or state[row][column]=='W':
        return flipped
    curr = player
    if(curr == 'B'):
        opp = 'W'
    else:
        opp = 'B'
    m = len(state[0])
    #Ver

    val1 = column + 2
    val2 = column - 2
    if val1<m:
        if state[row][val1] == curr and state[row][val1-1] == opp:
            flipped = flipped + 1
    if val2>=0:
         if state[row][val2] == curr and state[row][val2+1] == opp:
            flipped = flipped + 1
            
    #Hori
   
    val3 = row + 2
    val4 = row - 2
    if val3<m:
        if state[val3][column] == curr and state[val3-1][column] == opp:
            flipped = flipped + 1
    if val4>=0:
         if state[val4][column] == curr and state[val4+1][column] == opp:
            flipped = flipped + 1
            
    #Diagonal
    if val3<m:
        if val1<m :
            if state[val3][val1] == curr and state[val3-1][val1-1] == opp:
                flipped = flipped + 1
    if val3<m:
        if val2>=0:
            if state[val3][val2] == curr and state[val3-1][val2+1] == opp:
                flipped = flipped + 1
    if val4>=0:
        if val1<m:
            if state[val4][val1] == curr and state[val4+1][val1-1] == opp:
                flipped = flipped + 1
    if val4>=0:
        if val2>=0:
            if state[val4][val2] == curr and state[val4+1][val2+1] == opp:
                flipped = flipped + 1


    return flipped


'''
Execute a move that updates the state. A new state should be crated. The move
must be valid. Note that the new state should be a clone of the old state and
in particular, should not share memory with the old state. 
'''
def execute_move(state, player, row, column):
    new_state = None
    # Your implementation goes here
    new_state = []
    n = len(state[0])
    for i in range(0, n):
        row1 = []
        for j in range(0, n):
            if state[i][j]=='B':
                row1.append('B')
            elif state[i][j]=='W':
                row1.append('W')
            else:
                row1.append(' ')
        new_state.append(row1)
    #if get_move_value(state, player, row, column)==0:
    #    return new_state
    #else:
        #Place piece
    new_state[row][column] = player
    #Change Flipped Values
    curr = player
    if(curr == 'B'):
        opp = 'W'
    else:
        opp = 'B'
    m = len(state[0])
    #Ver

    val1 = column + 2
    val2 = column - 2
    if val1<m:
        if state[row][val1] == curr and state[row][val1-1] == opp:
            new_state[row][val1-1] = curr
    if val2>=0:
         if state[row][val2] == curr and state[row][val2+1] == opp:
            new_state[row][val2+1] = curr
            
    #Hori
   
    val3 = row + 2
    val4 = row - 2
    if val3<m:
        if state[val3][column] == curr and state[val3-1][column] == opp:
            new_state[val3-1][column] = curr
    if val4>=0:
         if state[val4][column] == curr and state[val4+1][column] == opp:
            new_state[val4+1][column] = curr
            
    #Diagonal
    if val3<m:
        if val1<m :
            if state[val3][val1] == curr and state[val3-1][val1-1] == opp:
                new_state[val3-1][val1-1] = curr
    if val3<m:
        if val2>=0:
            if state[val3][val2] == curr and state[val3-1][val2+1] == opp:
                new_state[val3-1][val2+1] = curr
    if val4>=0:
        if val1<m:
            if state[val4][val1] == curr and state[val4+1][val1-1] == opp:
                new_state[val4+1][val1-1] = curr
    if val4>=0:
        if val2>=0:
            if state[val4][val2] == curr and state[val4+1][val2+1] == opp:
                new_state[val4+1][val2+1] = curr


    return new_state

'''
A method for counting the pieces owned by the two players for a given state. The
return value should be two tuple in the format of (blackpeices, white pieces), e.g.,

    return (4, 3)

'''
def count_pieces(state):
    blackpieces = 0
    whitepieces = 0
    # Your implementation goes here
    for x in range(0, len(state[0])):
        for y in range(0, len(state[0])):
            if(state[x][y]=='B'):
                blackpieces = blackpieces + 1
            if(state[x][y]=='W'):
                whitepieces = whitepieces + 1
    return (blackpieces, whitepieces)

'''
Check whether a state is a terminal state. 
'''
def is_terminal_state(state, state_list = None):
    terminal = False
    # Your implementation goes here
    size = len(state[0])
    for i in range(0, size):
        for j in range(0, size):
            if get_move_value(state, 'B', i, j)>0:
                return terminal
            if get_move_value(state, 'W', i, j)>0:
                return terminal
    terminal = True
    return terminal

'''
The minimax algorithm. Your implementation should return the best value for the
given state and player, as well as the next immediate move to take for the player. 
'''
def minimax(state, player):
    global count
    maxval = 0
    retx = -1
    rety = -1
    
    if(is_terminal_state(state)):
        count = count + 1
        value = count_pieces(state)[0]
        return (value,-1,-1)

    if(player  == 'B'):
        change = 0
        maxval = 0
        for x in range(0,len(state[0])):
            for y in range(0,len(state[0])):
                value = get_move_value(state,player,x,y);
                if(value != 0):
                    change = 1;
                    teststate = execute_move(state, player, x, y)
                    testvalue = minimax(teststate,'W')
                    if(testvalue[0]>maxval): 
                        retx=x
                        rety=y
                        maxval=testvalue[0];
        if(change == 0):
            testvalue=minimax(state,'W')
            if(testvalue[0]>maxval): 
                maxval=testvalue[0]
    else:
        maxval = 0
        change = 0
        for x in range(0,len(state[0])):
            for y in range(0,len(state[0])):
                value = get_move_value(state,player,x,y);
                if(value != 0):
                    change = 1;
                    teststate = execute_move(state, player, x, y)
                    testvalue = minimax(teststate,'B')
                    if(testvalue[0]>maxval):
                        retx=x
                        rety=y
                        maxval=testvalue[0]
        if(change == 0):
            testvalue = minimax(state,'B')
            if(testvalue[0]>maxval): 
                maxval=testvalue[0]

    return (maxval,retx,rety)

'''
This method should call the minimax algorithm to compute an optimal move sequence
that leads to an end game. 
'''
move_sequence = []
def full_minimax(state, player):
    global count
    value = 0
    print(state)
    move_sequence = []
    if(is_terminal_state(state)):
        count = count + 1
        print(count)
        if player == 'B':
            value = count_pieces(state)[1]
        else:
            value = count_pieces(state)[0]
        move_sequence.append((player,-1,-1))
        return (value,move_sequence)

    ret = minimax(state,player)
    
    states = execute_move(state,player,ret[1],ret[2])
    move_sequence.extend((player,ret[1],ret[2]))

    if player == 'B':
        testvalue = full_minimax(states,'W')

    else:
        testvalue = full_minimax(states,'B')
    if(testvalue[0]>value):
        value=testvalue[0]
    move_sequence.extend((testvalue[1]))
    return (value, move_sequence)



'''
The minimax algorithm with alpha-beta pruning. Your implementation should return the
best value for the given state and player, as well as the next immediate move to take
for the player. 
'''
def minimax_ab(state, player, alpha = -10000000, beta = 10000000):
    global count
    global trunc
    maxval = 0
    retx = -1
    rety = -1
    
    if(is_terminal_state(state)):
        count = count + 1
        value = count_pieces(state)[0]
        return (value,-1,-1)

    if(player  == 'B'):
        change = 0
        maxval = 0
        for x in range(0,len(state[0])):
            for y in range(0,len(state[0])):
                if(beta<=alpha):
                    trunc = trunc + 1
                    return(alpha,-1,-1)
                value = get_move_value(state,player,x,y);
                if(value != 0):
                    change = 1;
                    teststate = execute_move(state, player, x, y)
                    testvalue = minimax_ab(teststate,'W',alpha,beta)
                    if(testvalue[0]>maxval): 
                        retx=x
                        rety=y
                        maxval=testvalue[0];
                    if(testvalue[0] < beta):
                        beta = testvalue[0]
        if(change == 0):
            if(beta<=alpha):
                trunc = trunc + 1
                return(beta,-1,-1)
            testvalue=minimax_ab(state,'W',alpha,beta)
            if(testvalue[0]>maxval): 
                maxval=testvalue[0]
            if(testvalue[0] < beta):
                beta = testvalue[0]
    else:
        maxval = 0
        change = 0
        for x in range(0,len(state[0])):
            for y in range(0,len(state[0])):
                if(beta<=alpha):
                    trunc = trunc + 1
                    return(alpha,-1,-1)
                value = get_move_value(state,player,x,y);
                if(value != 0):
                    change = 1;
                    teststate = execute_move(state, player, x, y)
                    testvalue = minimax_ab(teststate,'B',alpha,beta)
                    if(testvalue[0]>maxval):
                        retx=x
                        rety=y
                        maxval=testvalue[0]
                    if(testvalue[0] > beta):
                        alpha = testvalue[0]

        if(change == 0):
            if(beta<=alpha):
                trunc = trunc + 1
                return(alpha,-1,-1)
            testvalue = minimax_ab(state,'B',alpha,beta)
            if(testvalue[0]>maxval): 
                maxval=testvalue[0]
            if(testvalue[0] > beta):
                alpha = testvalue[0]

    return (maxval,retx,rety)


'''
This method should call the minimax_ab algorithm to compute an optimal move sequence
that leads to an end game, using alpha-beta pruning.
'''
count = 0
trunc = 0
def full_minimax_ab(state, player):
    global count
    value = 0
    move_sequence = []
    print(state)
    if(is_terminal_state(state)):
        count = count + 1
        if player == 'B':
            value = count_pieces(state)[1]
        else:
            value = count_pieces(state)[0]
        move_sequence.append((player,-1,-1))
        return (value,move_sequence)

    ret = minimax_ab(state,player)
    
    states = execute_move(state,player,ret[1],ret[2])
    move_sequence.extend((player,ret[1],ret[2]))

    if player == 'B':
        testvalue = full_minimax_ab(states,'W')

    else:
        testvalue = full_minimax_ab(states,'B')
    if(testvalue[0]>value):
        value=testvalue[0]
    move_sequence.extend((testvalue[1]))
    return (value, move_sequence)
def printval():
    print("count: " + str(count))
    print("trunc: " + str(trunc))

