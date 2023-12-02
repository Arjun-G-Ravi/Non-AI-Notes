from copy import deepcopy

init_state = [['' for i in range(3)] for j in range(3)] # empty
state1 = [['X', '', 'O'], ['X', '', ''], ['X', '', '']] # x win
state2 = [['X', 'X', 'O'], ['X', 'O', 'X'], ['O', 'X', 'O']] # O win, filled
state3 = [['X', 'X', 'O'], ['', '', 'O'], ['', '', 'O']] # o win
state4 = [['X', 'X', 'X'], ['O', 'O', 'O'], ['', '', '']] # both win

all_states = (init_state, state1, state2, state3, state4)

def action(state):
    l = []
    for i in range(3):
        for j in range(3):
            if state[i][j] == '':
                l.append([i,j])   
    return l

def result(state, action, player):
     temp_state = deepcopy(state)
     temp_state[action[0]][action[1]] = player
     return temp_state
 
def X_win(state):
    win_pos = [([0, 0], [0, 1], [0, 2]),
               ([1, 0], [1, 1], [1, 2]),
               ([2, 0], [2, 1], [2, 2]),
               ([0, 0], [1, 1], [2, 2]),
               ([0, 2], [2, 2], [2, 0]),
               ([0, 0], [1, 0], [2, 0]),
               ([0, 1], [1, 1], [2, 1]),
               ([0, 2], [1, 2], [2, 2])
               ]
    for val in win_pos:
        flag = 0
        for case in val:
            if state[case[0]][case[1]] == 'X':
                flag += 1
        if flag == 3:
            return True
    return False

def O_win(state):
    win_pos = [([0, 0], [0, 1], [0, 2]),
               ([1, 0], [1, 1], [1, 2]),
               ([2, 0], [2, 1], [2, 2]),
               ([0, 0], [1, 1], [2, 2]),
               ([0, 2], [2, 2], [2, 0]),
               ([0, 0], [1, 0], [2, 0]),
               ([0, 1], [1, 1], [2, 1]),
               ([0, 2], [1, 2], [2, 2])
               ]
    for val in win_pos:
        flag = 0
        for case in val:
            if state[case[0]][case[1]] == 'O':
                flag += 1
        if flag == 3:
            return True
    return False

def terminal_state(state):
    if X_win(state) or O_win(state):
        return True
    for i in state:
        for j in i:
            print(j)
            if j == '':
                return False
    return True

def utility(state):
    if not terminal_state(state):
        raise Exception('Non terminal state in utility function')
    if X_win(state):
        return -1
    elif O_win(state):
        return 1
    else:
        return 0
    
def max_val(state):
    if terminal_state(state):
        print('goat')
        return utility(state),
    
    v = -float('inf')
    print('cow')
    for a in action(state):
        new_state = result(state,a,'O')
        new_v = min_val(new_state)
        if new_v > v:
            v = new_v
            best_move = a
        return v, best_move

def min_val(state):
    if terminal_state(state):
        return utility(state)
    
    v = float('inf')
    for a in action(state):
        new_state = result(state,a,'O')
        new_v = max_val(new_state)[0]
        print("HERE", max_val(new_state))
        if new_v < v:
            v = new_v
        return v

def board_check(state):
    if X_win(state):
        print("You won")
    elif O_win(state):
        print("The computer won")
    else:
        print('It is a draw')
    # exit(0)
    
def display(state):
    for i in state:
        print(i)
        
def main():
    board = init_state
    print('BOARD:\n[1, 2, 3]\n[4, 5, 6]\n[7, 8, 9]\n\n')
    while True:
        player_move = int(input("Enter move: "))
        hmap = {1:[0, 0], 2:[0, 1], 3:[0, 2],4: [1, 0],5: [1, 1],6: [1, 2],7: [2, 0], 8:[2, 1], 9:[2, 2]}
        X_move = hmap[player_move]
        board = result(board, X_move, 'X')
        if terminal_state(board):
            board_check(board)
        
        # Computer plays
        print(max_val(board))
        display(board)
        
            
main()