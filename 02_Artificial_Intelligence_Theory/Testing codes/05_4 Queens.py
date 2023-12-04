# Arjun G Ravi
from time import sleep

Q = [[0,0], [0,1], [0,2], [0,3]]

def display(Q):
    board = [[' ' for _ in range(4)] for _ in range(4)] 
    for q in Q:
        board[q[0]][q[1]] = 'Q'
    for row in board:
        print(row)
# display(Q)

def queen_attack(square_cord):
    att_sq = list()
    for i in range(4):
        att_sq.append([square_cord[0], i])
        att_sq.append([i, square_cord[1]])
    # to add diagonals
    diag = [[1,1], [1,-1], [-1,1], [-1,-1]]
    for i in diag:
        # print('i is', i)
        this_sq = square_cord.copy()
        while True:
            this_sq[0] += i[0]
            this_sq[1] += i[1]
            # print(this_sq)
            # sleep(1)
            if 4 in this_sq or -1 in this_sq:
                break    
            if 4 not in this_sq or -1 not in this_sq:
                # print('appended', this_sq)
                att_sq.append(this_sq.copy())
             
        
    return att_sq
print(queen_attack([3,2]))

def main():
    current_queen = 0
    attack_sq = []
    while current_queen <= 3:
        # print(Q[current_queen], 'cow')
        if Q[current_queen] not in attack_sq:
            attack_sq.extend(queen_attack(Q[current_queen]))
            # print(attack_sq)
            print('Placed Queen at', Q[current_queen])
            current_queen += 1
            
        else:
            if Q[current_queen][0] < 3:
                # move one sq below
                Q[current_queen][0] += 1
                
            else:
                print("BACKTRACKING")
                to_remove = queen_attack(Q[current_queen])
                for bad in to_remove:
                    if bad in attack_sq:
                        attack_sq.remove(bad)
                print("Removed Queen from", Q[current_queen])
                current_queen -= 1 
                print(current_queen)

    display(Q)
main()




