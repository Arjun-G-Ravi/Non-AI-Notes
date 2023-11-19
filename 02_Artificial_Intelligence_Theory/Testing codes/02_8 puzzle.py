# init_state, ACTIONS, RESULT,  GOAL_TEST


init_state = [[1,2,3],[4,5,0],[7,8,6]]
final_state = [[1,2,3],[4,5,6],[7,8,0]]
    
    
def index_0(state):
    for i,v in enumerate(state):
        for j,vj in enumerate(v):
            if state[i][j] == 0:
                return(i,j)    
                

def ACTIONS(state):
    ind_0 = index_0(state)
    l = []
    for a in [(0,1),(1,0),(-1,0),(0,-1)]:
        if 3 not in (ind_0[0]+a[0],ind_0[1]+a[1]):
            # print('Ind',ind_0[0]+a[0],ind_0[1]+a[1])
            l.append(a)
    return l
            
def RESULT(state, action):
    pass

    