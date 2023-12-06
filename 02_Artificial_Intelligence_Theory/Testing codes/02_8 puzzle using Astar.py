from copy import deepcopy

init_state = [[0,1,2],[4,5,6],[7,8,3]]
final_state = [[1,2,3],[4,5,6],[7,8,0]]

def index_0(state):
    for i,v in enumerate(state):
        for j,vj in enumerate(v):
            if state[i][j] == 0:
                return(i,j)

def huristic_value(state): # Misplaced tiles
    ct = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != final_state[i][j]:
                ct += 1
    return ct

def RESULT(state, action):
    to_change = [None,None] 
    for i in range(2):
        to_change[i] = index_0(state)[i] + action[i]
    temp = state[to_change[0]][to_change[1]]
    state[index_0(state)[0]][index_0(state)[1]] = temp
    state[to_change[0]][to_change[1]] = 0
    return state
 
def ACTIONS(state):
    ind_0 = index_0(state)
    l = []
    for a in [(0,1),(1,0),(-1,0),(0,-1)]:
        if 3 not in (ind_0[0]+a[0],ind_0[1]+a[1]):
            temp_state = deepcopy(state)
            new_state = RESULT(temp_state, a)
            l.append((huristic_value(new_state),a))
    return l # f, action

def GOAL_TEST(state):
    if state == final_state:
        return True
    return False

def main():
    depth = 0
    frontier = [(0, init_state)] # Priority queue
    visited = []
    while frontier:
        state = frontier.pop(0)
        depth += 1
        one_state = state[1]
        print(one_state)
        if GOAL_TEST(one_state):
            print('Goal state reached')
            break
        for a in ACTIONS(one_state):
            current_state = deepcopy(one_state)
            new_state = RESULT(current_state, a[1])
            if new_state not in visited:
                frontier.append((a[0]+depth, new_state)) 
        visited.append(one_state)
        frontier.sort()
    
    if not frontier:
        print("Solution cannot be obtained")
main()