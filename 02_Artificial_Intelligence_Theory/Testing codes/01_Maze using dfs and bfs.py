env= [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 0, 0, 1, 1, 0, 1],
    [1, 0, 1, 1, 1, 0, 1, 0, 0, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 1, 1],
    [1, 1, 1, 0, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]  # 1 is wall

start = (6,1)
end = (3, 8)

# Here state will the position of the object, moving around the maze

class Node:
    def __init__(self, state):
        self.state = state
        self.parent_state = None
        self.prev_action = None

init_state = start
init_node = Node(init_state)
frontier = [init_node]
visited = []

def action(state):  # possible actions given a state
    pass

def transition_model(state, action):
    return state # but cahnge

def dfs():
    pass


# DO LATER ... 