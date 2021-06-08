board = [
    ["x", "x", ""],
    ["", "o", "x"],
    ["", "o", "o"]
]

# print(board[0][1])
# print(board[2][2])

for row in board:
    for col in row:
        print(col, "")