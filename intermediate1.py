import sys
import random
import signal

#Timer handler, helper function

class TimedOutExc(Exception):
        pass

def handler(signum, frame):
    #print 'Signal handler called with signal', signum
    raise TimedOutExc()


class Manual_player:
	def __init__(self):
		pass
	def move(self, temp_board, temp_block, old_move, flag):
		print 'Enter your move: <format:row column> (you\'re playing with', flag + ")"	
		mvp = raw_input()
		mvp = mvp.split()
		return (int(mvp[0]), int(mvp[1]))
		


class Player1(object):
    def __init__(self):
        self.player_prop = None
        self.opponent_prop = None
        self.actual_board = [[]] # '-', 'x', 'o'
        self.status_board = [] # '-', 'x', 'o'
        self.backup_status_board = []

    def get_block_coords(self,block_number):
        return {
            8 : (6, 6),
            7 : (3, 6),
            6 : (0, 6),
            5 : (6, 3),
            4 : (3, 3),
            3 : (0, 3),
            2 : (6, 0),
            1 : (3, 0),
            0 : (0, 0),
        }.get(block_number)
    
    def get_status_of_block(self,block_number,current_block,our_prop):
        has_completed = False
        first_win=0     #0=none 1=me 2=other
        x,y = self.get_block_coords(block_number)
        #print x,y,"here"
        our_prop = self.player_prop
        other_prop = self.opponent_prop

        for i in xrange(x,x+3):
            for j in xrange(y,y+3):
                if current_block[x][y] == other_prop or current_block[x][y] == our_prop:
                    has_completed = False

        if current_block[x][y] == our_prop and current_block[x + 1][y] == our_prop and current_block[x + 2][y] == our_prop:
            if first_win==0:
                first_win=1
        elif current_block[x][y + 1] == our_prop and current_block[x + 1][y + 1] == our_prop and current_block[x + 2][y + 1] == our_prop:
            if first_win==0:
                first_win=1
        elif current_block[x][y + 2] == our_prop and current_block[x + 1][y + 2] == our_prop and current_block[x + 2][y + 2] == our_prop:
            if first_win==0:
                first_win=1
        elif current_block[x][y] == our_prop and current_block[x][y + 1] == our_prop and current_block[x][y + 2] == our_prop:
            if first_win==0:
                first_win=1
        elif current_block[x + 1][y] == our_prop and current_block[x + 1][y + 1] == our_prop and current_block[x + 1][y + 2] == our_prop:
            if first_win==0:
                first_win=1
        elif current_block[x + 2][y] == our_prop and current_block[x + 2][y + 1] == our_prop and current_block[x + 2][y + 2] == our_prop:
            if first_win==0:
                first_win=1
        elif current_block[x][y] == our_prop and current_block[x + 1][y + 1] == our_prop and current_block[x + 2][y + 2] == our_prop:
            if first_win==0:
                first_win=1
        elif current_block[x + 2][y] == our_prop and current_block[x + 1][y + 1] == our_prop and current_block[x][y + 2] == our_prop:
            if first_win==0:
                first_win=1
        if current_block[x][y] == other_prop and current_block[x + 1][y] == other_prop and current_block[x + 2][y] == other_prop:
            if first_win==0:
                first_win=-1
        elif current_block[x][y + 1] == other_prop and current_block[x + 1][y + 1] == other_prop and current_block[x + 2][y + 1] == other_prop:
            if first_win==0:
                first_win=-1
        elif current_block[x][y + 2] == other_prop and current_block[x + 1][y + 2] == other_prop and current_block[x + 2][y + 2] == other_prop:
            if first_win==0:
                first_win=-1
        elif current_block[x][y] == other_prop and current_block[x][y + 1] == other_prop and current_block[x][y + 2] == other_prop:
            if first_win==0:
                first_win=-1
        elif current_block[x + 1][y] == other_prop and current_block[x + 1][y + 1] == other_prop and current_block[x + 1][y + 2] == other_prop:
            if first_win==0:
                first_win=-1
        elif current_block[x + 2][y] == other_prop and current_block[x + 2][y + 1] == other_prop and current_block[x + 2][y + 2] == other_prop:
            if first_win==0:
                first_win=-1
        elif current_block[x][y] == other_prop and current_block[x + 1][y + 1] == other_prop and current_block[x + 2][y + 2] == other_prop:
            if first_win==0:
                first_win=-1
        elif current_block[x + 2][y] == other_prop and current_block[x + 1][y + 1] == other_prop and current_block[x][y + 2] == other_prop:
            if first_win==0:
                first_win=-1
        return (has_completed,first_win)


    def game_completed(self,current_board,our_prop):
        q = [0 for x in xrange(0,9)]
        w = [0 for x in xrange(0,9)]
        j=0
        for i in xrange(0,9):
            q[i],w[i]=self.get_status_of_block(i,current_board,our_prop)
        for i in xrange(0,9):
            if q[i]==True or w[i]!=0:
                j += 1
        if w[1]+w[2]+w[0]==3 or w[3]+w[4]+w[5]==3 or w[6]+w[7]+w[8]==3 or w[0]+w[3]+w[6]==3 or w[1]+w[4]+w[7]==3 or w[2]+w[5]+w[8]==3 or w[0]+w[5]+w[8]==3 or w[2]+w[5]+w[7]==3:
            return (j,10)
        elif w[1]+w[2]+w[0]==-3 or w[3]+w[4]+w[5]==-3 or w[6]+w[7]+w[8]==-3 or w[0]+w[3]+w[6]==-3 or w[1]+w[4]+w[7]==-3 or w[2]+w[5]+w[8]==-3 or w[0]+w[5]+w[8]==-3 or w[2]+w[5]+w[7]==-3:
            return (j,-10)
        else:
            return (j,0)

    def get_board_status(self):
        return self.get_status_block(0, self.status_board, self.player_prop)
        
    def heuristic_score(self):
        	if self.player_prop == 'x':
			my_player = 'x'
			opponent_player = 'o'
		else:
			my_player ='o'
			opponent_player = 'x'
		Winning_combination = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
		Heuristic_array = [[0, -10, -100, -1000], [10, 0, 0, 0], [100, 0, 0, 0], [1000, 0, 0, 0]]
		heuristic_value = 0
		for i in range(9):
			offset_x = (i/3)*3
			offset_y = (i%3)*3
			for j in range(8):
				opponents = 0
				players = 0
				for k in range(3):
					x = Winning_combination[j][k]
					row_offset = x/3
					column_offset = x%3

					if(self.actual_board[offset_x+row_offset][offset_y+column_offset] is my_player):
						players = players + 1
					elif(self.actual_board[offset_x+row_offset][offset_y+column_offset] is opponent_player):
						opponents = opponents + 1
				heuristic_value = heuristic_value + Heuristic_array[players][opponents]
 
		for i in range(8):
			opponents = 0
			players = 0
			for j in range(3):
				if self.status_board[Winning_combination[i][j]] is  my_player:
					players =players + 1
				elif self.status_board[Winning_combination[i][j]] is opponent_player:
					opponents = opponents + 1
			heuristic_value = heuristic_value + 30*Heuristic_array[players][opponents]			
		return heuristic_value	

    def update_and_save_board_status(self,move_ret,prop,board_stat):
        status_board = board_stat[:]
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
            self.status_board[block_no] = prop
        id1 = block_no/3
        id2 = block_no%3
        cells = []
        for i in range(id1*3,id1*3+3):
            for j in range(id2*3,id2*3+3):
                if self.actual_board[i][j] == '-':
                    cells.append((i,j))
        if cells == [] and mflg != 1:
            self.status_board[block_no] = 'd'
        return status_board    

    def reverse_board_status(self):
        self.status_board = self.backup_status_board[:]

    def _get_prop_from_is_maximizing_player(self, is_max_player):
        if is_max_player:
            return self.player_prop
        else:
            return self.opponent_prop

    def move(self,current_board,board_stat,opponent_move,prop):
        self.player_prop = prop
        self.opponent_prop = 'x'
        if self.player_prop == self.opponent_prop:
            self.opponent_prop = 'o'
        self.actual_board = current_board[:]
        self.status_board = board_stat[:]
        cells=self.get_allowed_moves(opponent_move)
       # print "switching to level 3"
        depth = 3
        move, value = self.alpha_beta_pruning(opponent_move,board_stat, depth, -1000, 1000, False) 
        return move
    
    def alpha_beta_pruning(self, opponent_move,board_stat, depth, alpha, beta, is_maximizing_player):
        cells=self.get_allowed_moves(opponent_move)
        present_board_status=board_stat[:]
        if not cells:
            if is_maximizing_player:
                return (None, -1000)
            else:
                return (None, 1000)
        big_board_status, game_score = self.game_completed(self.actual_board, self._get_prop_from_is_maximizing_player(is_maximizing_player))
        if depth == 0: # Or is terminal node
            return ((cells[0]), self.heuristic_score())
        elif big_board_status == 9:
            return ((cells[0]), game_score)
        else:
            if is_maximizing_player:
                v = -1000 # for the first case only
                for cell in cells:
                    x,y = cell
                    #updated_board_status=[]
                    self.actual_board[x][y] = self._get_prop_from_is_maximizing_player(is_maximizing_player)
                    updated_board_status=self.update_and_save_board_status(cell, self._get_prop_from_is_maximizing_player(is_maximizing_player),board_stat)
                    child_node_values = self.alpha_beta_pruning(cell,updated_board_status ,depth - 1, alpha, beta, False)
                    self.actual_board[x][y] = '-'
                    v = child_node_values[1]
                    if alpha>v:
                        alpha = v
                    if alpha>=beta:
                        break
                return (cells[0], v) # return the cell of the calling function
            
            else:
                v = 1000 # for the first case only
                for cell in cells:
                    x,y = cell
                    self.actual_board[x][y] = self._get_prop_from_is_maximizing_player(is_maximizing_player)
                    updated_board_status=self.update_and_save_board_status(cell, self._get_prop_from_is_maximizing_player(is_maximizing_player),board_stat)
                    child_node_values = self.alpha_beta_pruning(cell, updated_board_status,depth - 1, alpha, beta, True)
                    self.actual_board[x][y] = '-'
                    v = child_node_values[1]
                    if v>beta:
                        beta = v
                    if alpha>=beta:
                        break        
                return (cells[0], v) # return the cell of the calling function


    def get_allowed_moves(self,old_move):
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

        blal=blocks_allowed;
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


class Player2:
	
	def __init__(self):
		pass
	def move(self,temp_board,temp_block,old_move,flag):
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
                    if temp_block[i] != '-':
                        blocks_allowed.remove(i)

	# We get all the empty cells in allowed blocks. If they're all full, we get all the empty cells in the entire board.
		cells = get_empty_out_of(temp_board,blocks_allowed,temp_block)
		return cells[random.randrange(len(cells))]

#Initializes the game
def get_init_board_and_blockstatus():
	board = []
	for i in range(9):
		row = ['-']*9
		board.append(row)
	
	block_stat = ['-']*9
	return board, block_stat

# Checks if player has messed with the board. Don't mess with the board that is passed to your move function. 
def verification_fails_board(board_game, temp_board_state):
	return board_game == temp_board_state	

# Checks if player has messed with the block. Don't mess with the block array that is passed to your move function. 
def verification_fails_block(block_stat, temp_block_stat):
	return block_stat == temp_block_stat	

#Gets empty cells from the list of possible blocks. Hence gets valid moves. 
def get_empty_out_of(gameb, blal,block_stat):
	cells = []  # it will be list of tuples
	#Iterate over possible blocks and get empty cells
	for idb in blal:
		id1 = idb/3
		id2 = idb%3
		for i in range(id1*3,id1*3+3):
			for j in range(id2*3,id2*3+3):
				if gameb[i][j] == '-':
					cells.append((i,j))

	# If all the possible blocks are full, you can move anywhere
	if cells == []:
		for i in range(9):
			for j in range(9):
                                no = (i/3)*3
                                no += (j/3)
				if gameb[i][j] == '-' and block_stat[no] == '-':
					cells.append((i,j))	
	return cells
		
# Note that even if someone has won a block, it is not abandoned. But then, there's no point winning it again!
# Returns True if move is valid
def check_valid_move(game_board,block_stat, current_move, old_move):

	# first we need to check whether current_move is tuple of not
	# old_move is guaranteed to be correct
	if type(current_move) is not tuple:
		return False
	
	if len(current_move) != 2:
		return False

	a = current_move[0]
	b = current_move[1]	

	if type(a) is not int or type(b) is not int:
		return False
	if a < 0 or a > 8 or b < 0 or b > 8:
		return False

	#Special case at start of game, any move is okay!
	if old_move[0] == -1 and old_move[1] == -1:
		return True


	for_corner = [0,2,3,5,6,8]

	#List of permitted blocks, based on old move.
	blocks_allowed  = []

	if old_move[0] in for_corner and old_move[1] in for_corner:
		## we will have 3 representative blocks, to choose from

		if old_move[0] % 3 == 0 and old_move[1] % 3 == 0:
			## top left 3 blocks are allowed
			blocks_allowed = [0,1,3]
		elif old_move[0] % 3 == 0 and old_move[1] in [2,5,8]:
			## top right 3 blocks are allowed
			blocks_allowed = [1,2,5]
		elif old_move[0] in [2,5,8] and old_move[1] % 3 == 0:
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

        #Check if the block is won, or completed. If so you cannot move there. 

        for i in reversed(blocks_allowed):
            if block_stat[i] != '-':
                blocks_allowed.remove(i)
        
        # We get all the empty cells in allowed blocks. If they're all full, we get all the empty cells in the entire board.
        cells = get_empty_out_of(game_board, blocks_allowed,block_stat)

	#Checks if you made a valid move. 
        if current_move in cells:
     	    return True
        else:
    	    return False

def update_lists(game_board, block_stat, move_ret, fl):
	#move_ret has the move to be made, so we modify the game_board, and then check if we need to modify block_stat
	game_board[move_ret[0]][move_ret[1]] = fl

	block_no = (move_ret[0]/3)*3 + move_ret[1]/3
	id1 = block_no/3
	id2 = block_no%3
	mg = 0
	mflg = 0
	if block_stat[block_no] == '-':
		if game_board[id1*3][id2*3] == game_board[id1*3+1][id2*3+1] and game_board[id1*3+1][id2*3+1] == game_board[id1*3+2][id2*3+2] and game_board[id1*3+1][id2*3+1] != '-':
			mflg=1
		if game_board[id1*3+2][id2*3] == game_board[id1*3+1][id2*3+1] and game_board[id1*3+1][id2*3+1] == game_board[id1*3][id2*3 + 2] and game_board[id1*3+1][id2*3+1] != '-':
			mflg=1
		
                if mflg != 1:
                    for i in range(id2*3,id2*3+3):
                        if game_board[id1*3][i]==game_board[id1*3+1][i] and game_board[id1*3+1][i] == game_board[id1*3+2][i] and game_board[id1*3][i] != '-':
                                mflg = 1
                                break

                ### row-wise
		if mflg != 1:
                    for i in range(id1*3,id1*3+3):
                        if game_board[i][id2*3]==game_board[i][id2*3+1] and game_board[i][id2*3+1] == game_board[i][id2*3+2] and game_board[i][id2*3] != '-':
                                mflg = 1
                                break

	
	if mflg == 1:
		block_stat[block_no] = fl
	
        #check for draw on the block.

        id1 = block_no/3
	id2 = block_no%3
        cells = []
	for i in range(id1*3,id1*3+3):
	    for j in range(id2*3,id2*3+3):
		if game_board[i][j] == '-':
		    cells.append((i,j))

        if cells == [] and mflg!=1:
            block_stat[block_no] = 'd' #Draw
        
        return

def terminal_state_reached(game_board, block_stat):
	
        #Check if game is won!
        bs = block_stat
	## Row win
	if (bs[0] == bs[1] and bs[1] == bs[2] and bs[1]!='-' and bs[1]!='d') or (bs[3]!='d' and bs[3]!='-' and bs[3] == bs[4] and bs[4] == bs[5]) or (bs[6]!='d' and bs[6]!='-' and bs[6] == bs[7] and bs[7] == bs[8]):
		print block_stat
		return True, 'W'
	## Col win
	elif (bs[0]!='d' and bs[0] == bs[3] and bs[3] == bs[6] and bs[0]!='-') or (bs[1]!='d'and bs[1] == bs[4] and bs[4] == bs[7] and bs[4]!='-') or (bs[2]!='d' and bs[2] == bs[5] and bs[5] == bs[8] and bs[5]!='-'):
		print block_stat
		return True, 'W'
	## Diag win
	elif (bs[0] == bs[4] and bs[4] == bs[8] and bs[0]!='-' and bs[0]!='d') or (bs[2] == bs[4] and bs[4] == bs[6] and bs[2]!='-' and bs[2]!='d'):
		print block_stat
		return True, 'W'
	else:
		smfl = 0
		for i in range(9):
			for j in range(9):
				if game_board[i][j] == '-' and block_stat[(i/3)*3+(j/3)] == '-':
					smfl = 1
					break
		if smfl == 1:
                        #Game is still on!
			return False, 'Continue'
		
		else:
                        #Changed scoring mechanism
                        # 1. If there is a tie, player with more boxes won, wins.
                        # 2. If no of boxes won is the same, player with more corner move, wins. 
                        point1 = 0
                        point2 = 0
                        for i in block_stat:
                            if i == 'x':
                                point1+=1
                            elif i=='o':
                                point2+=1
			if point1>point2:
				return True, 'P1'
			elif point2>point1:
				return True, 'P2'
			else:
                                point1 = 0
                                point2 = 0
                                for i in range(len(game_board)):
                                    for j in range(len(game_board[i])):
                                        if i%3!=1 and j%3!=1:
                                            if game_board[i][j] == 'x':
                                                point1+=1
                                            elif game_board[i][j]=='o':
                                                point2+=1
			        if point1>point2:
				    return True, 'P1'
			        elif point2>point1:
				    return True, 'P2'
                                else:
				    return True, 'D'	


def decide_winner_and_get_message(player,status, message):
	if player == 'P1' and status == 'L':
		return ('P2',message)
	elif player == 'P1' and status == 'W':
		return ('P1',message)
	elif player == 'P2' and status == 'L':
		return ('P1',message)
	elif player == 'P2' and status == 'W':
		return ('P2',message)
	else:
		return ('NO ONE','DRAW')
	return


def print_lists(gb, bs):
	print '=========== Game Board ==========='
	for i in range(9):
		if i > 0 and i % 3 == 0:
			print
		for j in range(9):
			if j > 0 and j % 3 == 0:
				print " " + gb[i][j],
			else:
				print gb[i][j],

		print
	print "=================================="

	print "=========== Block Status ========="
	for i in range(0, 9, 3):
		print bs[i] + " " + bs[i+1] + " " + bs[i+2] 
	print "=================================="
	print
	

def simulate(obj1,obj2):
	
	# Game board is a 9x9 list, block_stat is a 1D list of 9 elements
	game_board, block_stat = get_init_board_and_blockstatus()

	pl1 = obj1 
	pl2 = obj2

	### basically, player with flag 'x' will start the game
	pl1_fl = 'x'
	pl2_fl = 'o'

	old_move = (-1, -1) # For the first move

	WINNER = ''
	MESSAGE = ''

        #Make your move in 6 seconds!
	TIMEALLOWED = 6

	print_lists(game_board, block_stat)

	while(1):

		# Player1 will move
		
		temp_board_state = game_board[:]
		temp_block_stat = block_stat[:]
	
		signal.signal(signal.SIGALRM, handler)
		signal.alarm(TIMEALLOWED)
		# Player1 to complete in TIMEALLOWED secs. 
		try:
			ret_move_pl1 = pl1.move(temp_board_state, temp_block_stat, old_move, pl1_fl)
		except TimedOutExc as e:
			WINNER, MESSAGE = decide_winner_and_get_message('P1', 'L',   'TIMED OUT')
			break
		signal.alarm(0)
	
                #Checking if list hasn't been modified! Note: Do not make changes in the lists passed in move function!
		if not (verification_fails_board(game_board, temp_board_state) and verification_fails_block(block_stat, temp_block_stat)):
			#Player1 loses - he modified something
			WINNER, MESSAGE = decide_winner_and_get_message('P1', 'L',   'MODIFIED CONTENTS OF LISTS')
			break
		
		# Check if the move made is valid
		if not check_valid_move(game_board, block_stat,ret_move_pl1, old_move):
			## player1 loses - he made the wrong move.
			WINNER, MESSAGE = decide_winner_and_get_message('P1', 'L',   'MADE AN INVALID MOVE')
			break


		print "Player 1 made the move:", ret_move_pl1, 'with', pl1_fl

                #So if the move is valid, we update the 'game_board' and 'block_stat' lists with move of pl1
                update_lists(game_board, block_stat, ret_move_pl1, pl1_fl)

		# Checking if the last move resulted in a terminal state
		gamestatus, mesg =  terminal_state_reached(game_board, block_stat)
		if gamestatus == True:
			print_lists(game_board, block_stat)
			WINNER, MESSAGE = decide_winner_and_get_message('P1', mesg,  'COMPLETE')	
			break

		
		old_move = ret_move_pl1
		print_lists(game_board, block_stat)

                # Now player2 plays

                temp_board_state = game_board[:]
                temp_block_stat = block_stat[:]


		signal.signal(signal.SIGALRM, handler)
		signal.alarm(TIMEALLOWED)
		try:
                	ret_move_pl2 = pl2.move(temp_board_state, temp_block_stat, old_move, pl2_fl)
		except TimedOutExc as e:
			WINNER, MESSAGE = decide_winner_and_get_message('P2', 'L',   'TIMED OUT')
			break
		signal.alarm(0)

                if not (verification_fails_board(game_board, temp_board_state) and verification_fails_block(block_stat, temp_block_stat)):
			WINNER, MESSAGE = decide_winner_and_get_message('P2', 'L',   'MODIFIED CONTENTS OF LISTS')
			break
			
                if not check_valid_move(game_board, block_stat,ret_move_pl2, old_move):
			WINNER, MESSAGE = decide_winner_and_get_message('P2', 'L',   'MADE AN INVALID MOVE')
			break


		print "Player 2 made the move:", ret_move_pl2, 'with', pl2_fl
                
                update_lists(game_board, block_stat, ret_move_pl2, pl2_fl)

		gamestatus, mesg =  terminal_state_reached(game_board, block_stat)
                if gamestatus == True:
			print_lists(game_board, block_stat)
                        WINNER, MESSAGE = decide_winner_and_get_message('P2', mesg,  'COMPLETE' )
                        break
		old_move = ret_move_pl2
		print_lists(game_board, block_stat)
	
	print WINNER + " won!"
	print MESSAGE

if __name__ == '__main__':
	## get game playing objects

	if len(sys.argv) != 2:
		print 'Usage: python simulator.py <option>'
		print '<option> can be 1 => Random player vs. Random player'
		print '                2 => Human vs. Random Player'
		print '                3 => Human vs. Human'
		sys.exit(1)
 
	obj1 = ''
	obj2 = ''
	option = sys.argv[1]	
	if option == '1':
		obj1 = Player1()
		obj2 = Player2()

	elif option == '2':
		obj1 = Player1()
		obj2 = Manual_player()
	elif option == '3':
		obj1 = Manual_player()
		obj2 = Manual_player()
        
        # Deciding player1 / player2 after a coin toss
        # However, in the tournament, each player will get a chance to go 1st. 
        num = random.uniform(0,1)
     #   if num > 0.5:
	simulate(obj1, obj2)
	#else:
	#	simulate(obj1, obj2)
