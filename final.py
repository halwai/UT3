import random

class Player(object):
    '''
        Player Class Container.
    '''
    def __init__(self):
        self.H_O = 0
        self.H_X = 0
        self.h_o = [0,0,0,0,0,0,0,0,0]
        self.h_x = [0,0,0,0,0,0,0,0,0]
        self.number_of_moves = 0
        self.player_symbol = None
        self.opponent_symbol = None
        self.actual_board = [[]] # '-', 'x', 'o'
        self.status_board = [] # '-', 'x', 'o'
        self.backup_status_board = []

    def init(self):
        self.__init__()

    def get_block_coords(self,block_number):
        return {
            0 : (0, 0),
            1 : (3, 0),
            2 : (6, 0),
            3 : (0, 3),
            4 : (3, 3),
            5 : (6, 3),
            6 : (0, 6),
            7 : (3, 6),
            8 : (6, 6),
        }.get(block_number)
    
    def get_status_of_block(self,block_number,current_block,our_symbol):
        has_completed = False
        first_win=0     #0=none 1=me 2=other
        x,y = self.get_block_coords(block_number)

        our_symbol = self.player_symbol
        other_symbol = self.opponent_symbol

        for i in xrange(x,x+3):
            for j in xrange(y,y+3):
                if current_block[x][y] == other_symbol or current_block[x][y] == our_symbol:
                    has_completed = False

        if current_block[x][y] == our_symbol and current_block[x + 1][y] == our_symbol and current_block[x + 2][y] == our_symbol:
            if first_win==0:
                first_win=1
        elif current_block[x][y + 1] == our_symbol and current_block[x + 1][y + 1] == our_symbol and current_block[x + 2][y + 1] == our_symbol:
            if first_win==0:
                first_win=1
        elif current_block[x][y + 2] == our_symbol and current_block[x + 1][y + 2] == our_symbol and current_block[x + 2][y + 2] == our_symbol:
            if first_win==0:
                first_win=1
        elif current_block[x][y] == our_symbol and current_block[x][y + 1] == our_symbol and current_block[x][y + 2] == our_symbol:
            if first_win==0:
                first_win=1
        elif current_block[x + 1][y] == our_symbol and current_block[x + 1][y + 1] == our_symbol and current_block[x + 1][y + 2] == our_symbol:
            if first_win==0:
                first_win=1
        elif current_block[x + 2][y] == our_symbol and current_block[x + 2][y + 1] == our_symbol and current_block[x + 2][y + 2] == our_symbol:
            if first_win==0:
                first_win=1
        elif current_block[x][y] == our_symbol and current_block[x + 1][y + 1] == our_symbol and current_block[x + 2][y + 2] == our_symbol:
            if first_win==0:
                first_win=1
        elif current_block[x + 2][y] == our_symbol and current_block[x + 1][y + 1] == our_symbol and current_block[x][y + 2] == our_symbol:
            if first_win==0:
                first_win=1
        if current_block[x][y] == other_symbol and current_block[x + 1][y] == other_symbol and current_block[x + 2][y] == other_symbol:
            if first_win==0:
                first_win=-1
        elif current_block[x][y + 1] == other_symbol and current_block[x + 1][y + 1] == other_symbol and current_block[x + 2][y + 1] == other_symbol:
            if first_win==0:
                first_win=-1
        elif current_block[x][y + 2] == other_symbol and current_block[x + 1][y + 2] == other_symbol and current_block[x + 2][y + 2] == other_symbol:
            if first_win==0:
                first_win=-1
        elif current_block[x][y] == other_symbol and current_block[x][y + 1] == other_symbol and current_block[x][y + 2] == other_symbol:
            if first_win==0:
                first_win=-1
        elif current_block[x + 1][y] == other_symbol and current_block[x + 1][y + 1] == other_symbol and current_block[x + 1][y + 2] == other_symbol:
            if first_win==0:
                first_win=-1
        elif current_block[x + 2][y] == other_symbol and current_block[x + 2][y + 1] == other_symbol and current_block[x + 2][y + 2] == other_symbol:
            if first_win==0:
                first_win=-1
        elif current_block[x][y] == other_symbol and current_block[x + 1][y + 1] == other_symbol and current_block[x + 2][y + 2] == other_symbol:
            if first_win==0:
                first_win=-1
        elif current_block[x + 2][y] == other_symbol and current_block[x + 1][y + 1] == other_symbol and current_block[x][y + 2] == other_symbol:
            if first_win==0:
                first_win=-1
        return (has_completed,first_win)

    def get_permitted_blocks(self,old_move):
        for_corner = [0,2,3,5,6,8]

        #List of permitted blocks, based on old move.
        blocks_allowed  = []

        if old_move[0] in for_corner and old_move[1] in for_corner:
            ## we will have 3 representative blocks, to choose from

            if old_move[0] % 3 == 0 and old_move[1] % 3 == 0:
                ## top left 3 blocks are allowed
                blocks_allowed = [0, 1, 3]
            elif old_move[0] % 3 == 0 and old_move[1] in [2, 5, 8]:
                ## top right 3 blocks are allowed
                blocks_allowed = [1,2,5]
            elif old_move[0] in [2,5, 8] and old_move[1] % 3 == 0:
                ## bottom left 3 blocks are allowed
                blocks_allowed  = [3,6,7]
            elif old_move[0] in [2,5,8] and old_move[1] in [2,5,8]:
                ### bottom right 3 blocks are allowed
                blocks_allowed = [5,7,8]
            else:
                print "SOMETHING REALLY WEIRD HAPPENED!"
                sys.exit(1)
        else:
        #### we will have only 1 block to choose from (or maybe NONE of them, which calls for a free move)
            if old_move[0] % 3 == 0 and old_move[1] in [1,4,7]:
                ## upper-center block
                blocks_allowed = [1]
    
            elif old_move[0] in [1,4,7] and old_move[1] % 3 == 0:
                ## middle-left block
                blocks_allowed = [3]
        
            elif old_move[0] in [2,5,8] and old_move[1] in [1,4,7]:
                ## lower-center block
                blocks_allowed = [7]

            elif old_move[0] in [1,4,7] and old_move[1] in [2,5,8]:
                ## middle-right block
                blocks_allowed = [5]
            elif old_move[0] in [1,4,7] and old_move[1] in [1,4,7]:
                blocks_allowed = [4]
                
        for i in reversed(blocks_allowed):
            if self.status_board[i] != '-':
                blocks_allowed.remove(i)

        return blocks_allowed
    

    def get_empty_out_of(self,blal):
        cells = []
        for idb in blal:
            id1 = idb/3
            id2 = idb%3
            for i in range(id1*3,id1*3+3):
                for j in range(id2*3,id2*3+3):
                    if self.actual_board[i][j] == '-':
                        cells.append((i,j))
        if cells == []:
            for i in range(9):
                for j in range(9):
                    no = (i/3)*3
                    no += (j/3)
                    if self.actual_board[i][j] == '-' and self.status_board[no] == '-':
                        cells.append((i,j)) 
        return cells

    def get_baseline_allowed_moves(self,current_board,moves):       #permitted moves(gand bachao)
        pass

    def game_completed(self,current_board,our_symbol):
        q = [0 for x in xrange(0,9)]
        w = [0 for x in xrange(0,9)]
        j=0
        for i in xrange(0,9):
            q[i],w[i]=self.get_status_of_block(i,current_board,our_symbol)
        for i in xrange(0,9):
            if q[i]==True or w[i]!=0:
                j += 1
        if w[1]+w[2]+w[0]==3 or w[3]+w[4]+w[5]==3 or w[6]+w[7]+w[8]==3 or w[0]+w[3]+w[6]==3 or w[1]+w[4]+w[7]==3 or w[2]+w[5]+w[8]==3 or w[0]+w[5]+w[8]==3 or w[2]+w[5]+w[7]==3:
            return (j,10)
        elif w[1]+w[2]+w[0]==-3 or w[3]+w[4]+w[5]==-3 or w[6]+w[7]+w[8]==-3 or w[0]+w[3]+w[6]==-3 or w[1]+w[4]+w[7]==-3 or w[2]+w[5]+w[8]==-3 or w[0]+w[5]+w[8]==-3 or w[2]+w[5]+w[7]==-3:
            return (j,-10)
        else:
            return (j,0)

    def return_random_move(self,possible_moves):
        return random.choice(possible_moves)

    def get_board_status(self):
        return self.get_status_block(0, self.status_board, self.player_symbol)

    def bind_symbol(self,our_symbol):
        self.player_symbol = our_symbol
        self.opponent_symbol = 'x'
        if self.player_symbol == self.opponent_symbol:
            self.opponent_symbol = 'o'
        

    def copy_current_board_elems(self,current_board,board_stat):
        self.actual_board = current_board[:]
        self.status_board = board_stat[:]
        
    def heuristic_score(self):
        return random.randint(-10,10)

    def update_and_save_board_status(self,move_ret,symbol):
        self.backup_status_board = self.status_board[:]
        block_no = (move_ret[0]/3)*3 + (move_ret[1])/3
        id1 = block_no/3
        id2 = block_no%3
        mg = 0
        mflg = 0
        if self.status_board[block_no] == '-':
            if self.actual_board[id1*3][id2*3] == self.actual_board[id1*3+1][id2*3+1] and self.actual_board[id1*3+1][id2*3+1] == self.actual_board[id1*3+2][id2*3+2] and self.actual_board[id1*3+1][id2*3+1] != '-':
                mflg=1
            if self.actual_board[id1*3+2][id2*3] == self.actual_board[id1*3+1][id2*3+1] and self.actual_board[id1*3+1][id2*3+1] == self.actual_board[id1*3][id2*3 + 2] and self.actual_board[id1*3+1][id2*3+1] != '-':
                mflg=1
            if mflg != 1:
                for i in range(id2*3,id2*3+3):
                    if self.actual_board[id1*3][i]==self.actual_board[id1*3+1][i] and self.actual_board[id1*3+1][i] == self.actual_board[id1*3+2][i] and self.actual_board[id1*3][i] != '-':
                        mflg = 1
                        break
            if mflg != 1:
                for i in range(id1*3,id1*3+3):
                    if self.actual_board[i][id2*3]==self.actual_board[i][id2*3+1] and self.actual_board[i][id2*3+1] == self.actual_board[i][id2*3+2] and self.actual_board[i][id2*3] != '-':
                        mflg = 1
                        break
        if mflg == 1:
            self.status_board[block_no] = symbol
        id1 = block_no/3
        id2 = block_no%3
        cells = []
        for i in range(id1*3,id1*3+3):
            for j in range(id2*3,id2*3+3):
                if self.actual_board[i][j] == '-':
                    cells.append((i,j))
        if cells == [] and mflg != 1:
            self.status_board[block_no] = 'd'

    def reverse_board_status(self):
        self.status_board = self.backup_status_board[:]

    def free_move(self):
        pass # return whatever

    def _get_symbol_from_is_maximizing_player(self, is_maximizing_player):
        if is_maximizing_player:
            return self.player_symbol
        else:
            return self.opponent_symbol

    # """
    def real_alpha_beta(self, opponent_move, depth, alpha, beta, is_maximizing_player):
        blocks_allowed = self.get_permitted_blocks(opponent_move)
        cells = self.get_empty_out_of(blocks_allowed)

        # check termination conditions
        if not cells:
            if is_maximizing_player:
                return (None, -99999)
            else:
                return (None, 99999)

        game_status, game_score = self.game_completed(self.actual_board, self._get_symbol_from_is_maximizing_player(is_maximizing_player))
        if depth == 0: # Or is terminal node
            return ((cells[0]), self.heuristic_score())
        elif game_status == 9:
            return ((cells[0]), game_score)
        else:

            # begin to prune
            if is_maximizing_player:
                v = -99999 # for the first case only
                for cell in cells:
                    x,y = cell
                    self.actual_board[x][y] = self._get_symbol_from_is_maximizing_player(is_maximizing_player)
                    self.update_and_save_board_status(cell, self._get_symbol_from_is_maximizing_player(is_maximizing_player))
                    child_node_values = self.real_alpha_beta(cell, depth - 1, alpha, beta, False)
                    self.actual_board[x][y] = '-'
                    v = child_node_values[1]
                    if v > alpha:
                        alpha = v
                    
                    if beta <= alpha:
                        break

                return (cells[0], v) # return the cell of the calling function 
            else:
                v = 99999 # for the first case only
                for cell in cells:
                    x,y = cell
                    self.actual_board[x][y] = self._get_symbol_from_is_maximizing_player(is_maximizing_player)
                    self.update_and_save_board_status(cell, self._get_symbol_from_is_maximizing_player(is_maximizing_player))
                    child_node_values = self.real_alpha_beta(cell, depth - 1, alpha, beta, True)
                    self.actual_board[x][y] = '-'
                    v = child_node_values[1]
                    if beta < v:
                        beta = v

                    if beta <= alpha:
                        break

                return (cells[0], v) # return the cell of the calling function

    # """
    def min_max_with_alpha_beta_pruning(self,opponent_move,our_symbol,depth):
        blocks_allowed = self.get_permitted_blocks(opponent_move)
        cells = self.get_empty_out_of(blocks_allowed)
        game_status,game_score = self.game_completed(self.actual_board,'x')
        if depth <= 0: 
            return ((cells[0]),self.heuristic_score());
        elif game_status == 9: # Terminal Condition
            return ((cells[0]),game_score) # -10or0or10 and move that can't be made
        else:
            alpha=beta=utility=((cells[0]), float("nan"))
            if our_symbol == 'x': # TODO : remove the assumption that x is max-node
                for cell in cells:
                    x,y = cell
                    self.actual_board[x][y] = 'x'
                    self.update_and_save_board_status(cell,our_symbol)
                    child = self.min_max_with_alpha_beta_pruning(cell,'o',depth-1)
                    self.actual_board[x][y] = '-'
                    self.reverse_board_status()
                    if utility[1] == float("nan") or utility[1] < child[1]:
                        utility = (cell,child[1])
                    if alpha[1] == float("nan") or utility[1] > alpha[1]:
                        alpha = utility
                    if beta[1] != float("nan") and alpha[1] > beta[1]:
                        break
                return alpha
            elif our_symbol == 'o':
                for cell in cells:
                    x,y = cell
                    self.actual_board[x][y] = 'o'
                    self.update_and_save_board_status(cell,our_symbolipy)
                    child = self.min_max_with_alpha_beta_pruning(cell,'x',depth-1)
                    self.actual_board[x][y] = '-'
                    self.reverse_board_status()
                    if utility[1] == float("nan") or utility[1] > child[1]:
                        utility = (cell,child[1])
                    if alpha[1] == float("nan") or utility[1] < beta[1]:
                        beta = utility
                    if beta[1] != float("nan") and alpha[1] > beta[1]:
                        break
                return beta

    def free_move(self):
        print "Reached free move"
        return None

    def move(self,current_board,board_stat,opponent_move,our_symbol):
        '''
        Parameters - opponent_move - <(a,b)> previous move by opponent; board_stat - <[]> info of blocks won/lost; 
                    current_board - <[]> current board situation; our_symbol
        Return Value - move- <(row,column)> 
        '''
        self.bind_symbol(our_symbol)
        self.copy_current_board_elems(current_board,board_stat)
        self.number_of_moves = self.number_of_moves + 1

        blocks_allowed = self.get_permitted_blocks(opponent_move)
        cells = self.get_empty_out_of(blocks_allowed)

        if not cells:
            return self.free_move()

        if self.number_of_moves < 15:
            print "switching to level 3"
            depth = 3
        else:
            print "switching to level 5"
            depth = 3

        move, value = self.real_alpha_beta(opponent_move, depth, -99999, 99999, True) 
        # move,value = self.min_max_with_alpha_beta_pruning(opponent_move,self.player_symbol,1)
        # print move
        return move