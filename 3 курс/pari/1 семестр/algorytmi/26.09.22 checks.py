
def solve():
    board = [-1, -1, -1, -1, -1, -1, -1, -1]
    solutions_cnt = 0

    # 1 столбец
    for i0 in range(len(board)):
        board[0] = i0
        
        # 2 столбец
        for i1 in range(len(board)):
            if i1 in board: continue

            if i1 != board[0] + 1 and i1 != board[0] - 1:
                board[1] = i1

                # 3 столбец
                for i2 in range(len(board)):
                    if i2 in board: continue

                    if (i2 != board[0] + 2 and i2 != board[0] - 2 
                    and i2 != board[1] + 1 and i2 != board[1] - 1):
                        board[2] = i2
                
                        # 4 столбец
                        for i3 in range(len(board)):
                            if i3 in board: continue

                            if (i3 != board[0] + 3 and
                                i3 != board[0] - 3 and
                                i3 != board[1] + 2 and
                                i3 != board[1] - 2 and 
                                i3 != board[2] + 1 and 
                                i3 != board[2] - 1):
                                board[3] = i3

                            # 5 столбец
                                for i4 in range(len(board)):
                                    if i4 in board: continue

                                    if (i4 != board[0] + 4 and i4 != board[0] - 4 
                                    and i4 != board[1] + 3 and i4 != board[1] - 3
                                    and i4 != board[2] + 2 and i4 != board[2] - 2
                                    and i4 != board[3] + 1 and i4 != board[3] - 1):
                                        board[4] = i4
                                    
                        
                                    # 6 столбец
                                        for i5 in range(len(board)):
                                            if i5 in board: continue

                                            if (i5 != board[0] + 5 and i5 != board[0] - 5 
                                            and i5 != board[1] + 4 and i5 != board[1] - 4
                                            and i5 != board[2] + 3 and i5 != board[2] - 3
                                            and i5 != board[3] + 2 and i5 != board[3] - 2
                                            and i5 != board[4] + 1 and i5 != board[4] - 1):
                                                board[5] = i5

                                            # 7 столбец
                                                for i6 in range(len(board)):
                                                    if i6 in board: continue

                                                    if (i6 != board[0] + 6 and i6 != board[0] - 6 
                                                    and i6 != board[1] + 5 and i6 != board[1] - 5
                                                    and i6 != board[2] + 4 and i6 != board[2] - 4
                                                    and i6 != board[3] + 3 and i6 != board[3] - 3
                                                    and i6 != board[4] + 2 and i6 != board[4] - 2
                                                    and i6 != board[5] + 1 and i6 != board[5] - 1):
                                                        board[6] = i6

                                                        for i7 in range(len(board)):
                                                            if i7 in board: continue

                                                            if (i7 != board[0] + 7 and i7 != board[0] - 7 
                                                            and i7 != board[1] + 6 and i7 != board[1] - 6
                                                            and i7 != board[2] + 5 and i7 != board[2] - 5
                                                            and i7 != board[3] + 4 and i7 != board[3] - 4
                                                            and i7 != board[4] + 3 and i7 != board[4] - 3
                                                            and i7 != board[5] + 2 and i7 != board[5] - 2
                                                            and i7 != board[6] + 1 and i7 != board[6] - 1):
                                                                board[7] = i7
                                                                solutions_cnt += 1
                                                            
                                                            board[7] = -1

                                                    board[6] = -1

                                            board[5] = -1

                                    board[4] = -1
                            
                            board[3] = -1

                    board[2] = -1

            board[1] = -1

    return solutions_cnt

                            
            

# сделать словарь для хранения возможных полей по столбцам
# переход между столбцами внутри цикла while(i != -1)
# i = -1 когда захотим выйти из цикла? 

# def solve(board_size = 6):
#     solutions_cnt = 0

#     # возможные расположения ферзей по колонкам
#     board_positions = {}
#     for i in range(board_size):
#         board_positions[i] = [-1] * board_size

#     # номер столбца с которым мы сейчас работаем
#     c = 0
#     while(c != -1):
#         for i in board_positions[c]:


print(solve())
