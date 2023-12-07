# Arjun G Ravi
Q = [[0,0], [0,1], [0,2], [0,3]]

def display(Q):
    board = [[' ' for _ in range(4)] for _ in range(4)] 
    for q in Q:
        board[q[0]][q[1]] = 'Q'
    for row in board:
        print(row)

def queen_attack(square_cord): # Returns the list of coords that a queen placed on 'square_cord' will attack
    att_sq = list()
    for i in range(4):
        att_sq.append([square_cord[0], i])
        att_sq.append([i, square_cord[1]])
    diag = [[1,1], [1,-1], [-1,1], [-1,-1]]
    for i in diag:
        this_sq = square_cord.copy()
        while True:
            this_sq[0] += i[0]
            this_sq[1] += i[1]
            if 4 in this_sq or -1 in this_sq:
                break    
            if 4 not in this_sq or -1 not in this_sq:
                att_sq.append(this_sq.copy())
    return att_sq

def main():
    current_queen = 0
    attack_sq = []
    while -1 < current_queen <= 3:
        if Q[current_queen] not in attack_sq and Q[current_queen][0]<4:
            print(f'Placed Queen:{current_queen} at', Q[current_queen])
            attack_sq.extend(queen_attack(Q[current_queen]))
            current_queen += 1
            
        else:
            if Q[current_queen][0] < 3: # move one sq below
                Q[current_queen][0] += 1
                
            else:
                print("BACKTRACKING")
                Q[current_queen][0] = 0
                current_queen -= 1
                print(f"Removed Queen:{current_queen} from", Q[current_queen])
                to_remove = queen_attack(Q[current_queen])
                for bad in to_remove:
                    if bad in attack_sq:
                        attack_sq.remove(bad)

                Q[current_queen][0] += 1
    display(Q)
main()