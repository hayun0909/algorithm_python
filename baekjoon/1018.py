N, M = map(int, input().split())
cnt = None
board = []
chess = [
    [
        ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
        ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], 
        ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], 
        ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], 
        ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], 
        ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], 
        ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], 
        ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B']
    ],
    [
        ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
        ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], 
        ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], 
        ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], 
        ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], 
        ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], 
        ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], 
        ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W']
    ]]

for i in range(N):
    row = list(input())
    board.append(row)

num_row = N - 8 + 1
num_col = M - 8 + 1

for i in range(num_row):
    for j in range(num_col):
        w_cnt = 0
        b_cnt = 0
        for k in range(8):
            for l in range(8):
                if board[i+k][j+l] != chess[0][k][l]:
                    b_cnt += 1
                if board[i+k][j+l] != chess[1][k][l]:
                    w_cnt += 1

        if cnt == None:
            cnt = min(w_cnt, b_cnt)
        else:
            m = min(w_cnt, b_cnt)
            cnt = min(cnt, m)

print(cnt)