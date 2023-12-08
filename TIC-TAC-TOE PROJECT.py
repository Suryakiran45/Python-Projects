#!/usr/bin/env python
# coding: utf-8

# In[ ]:


board=[' '] * 10
player1 = 'x'
player2 = 'o'
       
def display_board(board):
    print(f'{board[1]} | {board[2]} | {board[3]}')
    print(f'{board[4]} | {board[5]} | {board[6]}')
    print(f'{board[7]} | {board[8]} | {board[9]}')
    print('-'*10)
    
def check_win():
    if board[1]==board[2]==board[3] and board[1]!=' ':
        return True
    elif board[4]==board[5]==board[6] and board[4]!=' ':
        return True
    elif board[7]==board[8]==board[9] and board[7]!=' ':
        return True
    elif board[1]==board[4]==board[7] and board[1]!=' ':
        return True
    elif board[2]==board[5]==board[8] and board[2]!=' ':
        return True
    elif board[3]==board[6]==board[9] and board[3]!=' ':
        return True
    elif board[1]==board[5]==board[9] and board[1]!=' ':
        return True
    elif board[3]==board[5]==board[7] and board[3]!=' ':
        return True
    else:
        return False
    
def check_draw():
    if board.count(' ')<2:
        return True
    else:
        return False   
    
def is_available(pos):
    if board[pos]==' ':
        return True
    else:
        return False
        
def insert(letter,pos):
    if is_available(pos):
        board[pos]=letter
        display_board(board)
        if check_win():
            if letter=='x':
                print('player1 wins')
                exit()
            else:
                print('player2 wins')
                exit()
        if check_draw():
            print('draw')
            exit()
    else:
        if letter=='x':
            pos=int(input('not available,re-enter pos'))
            insert(letter,pos)
        if letter=='0':
            pos=int(input('not available re-enter pos'))
            insert(letter,pos) 
            
def player1_move(letter):    
    pos=int(input("enter the position "))
    insert(letter,pos)
    
def player2_move(letter):
    pos=int(input("enter the position u "))
    insert(letter,pos)
    
while not check_win():
    display_board(board)
    player1_move(player1)
    player2_move(player2)
    


# In[ ]:


print(board)


# In[ ]:




