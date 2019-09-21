import time
import pygame, sys
from pygame.locals import QUIT
from pygame.locals import KEYDOWN,K_LEFT,K_RIGHT,K_DOWN
import random
BLUE= (0,0,155)
BOX_SIZE=20
SCREEN_WIDTH=640
SCREEN_HEIGHT=480
# BOARD_WIDTH=90
SPEED=0.5
S_SHAPE = [['.....',
			'.....',
			'..cc.',
			'.cc..',
			'.....']]

I_SHAPE = [['..c..',
			'..c..',
			'..c..',
			'..c..',
			'.....']]

O_SHAPE = [['.....',
			'.....',
			'.cc..',
			'.cc..',
			'.....']]


def available_tetris_pieces():
	return{
	'S':S_SHAPE,
	'I':I_SHAPE,
	'O':O_SHAPE
	}

def draw_moving_piece():
	#get the puece matrix
	shape_to_draw=available_tetris_pieces()[piece['shape']][0]
	#loop over each cell and draw a blok if necesary
	for row in range(5):
		for col in range(5):
			if shape[row][col] != '.':
	#draw single_tetris_block
				single_tetris_block(screen,piece['row']+row, piece['column']+col,(255,255,255),(217,217,220))
	return

def update_game_matrix(matrix, piece):
	#loop over each cell in the piece matrix
	for row in range(5):
		for col in range(5):
	#update the fame matrix when necesary
			if(available_tetris_pieces()[piece['shape']][0][row] != '.'):
				matrix[piece['row']+row][piece['column']+col]='c'
	return matrix






def run_tetris_game():
	pygame.init() #start the game engine
	screen= pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT)) #create window
	pygame.display.set_caption("Tetris") #title of the window
	game_matrix = create_game_matrix()
	#Create the shape
	last_time_piece_moved=time.time()
	piece=create_piece()
	
	score=0
	while True:
		screen.fill((0,0,0)) #black background
		#Move piece down the screen each second
		if(time.time()-last_time_piece_moved>SPEED):
			piece['row']=piece['row']+1
			last_time_piece_moved=time.time() #este continua avanzando, y se checa cada ciclo , hasta que avance 1 segundo, ejecuta de nuevo
			# SPEED=0.5
		#display piece on board
		draw_piece(screen, piece) #draw the shape with shadow
		pygame.draw.rect(
			screen,
			BLUE,
			[100,50,10*20,20*20],5) #10*20> 10 times box, 20x20, 20times BOX, 5 is the boldness of line

		#Draw board
		draw_board(screen,game_matrix)
		draw_score(screen,score)

		#User Input
		listen_to_user_input(game_matrix, piece)

		# if(not isValidRotationPosition(game_matrix,piece,adjRow=1)):
		# 	game_matrix = update_game_matrix(game_matrix,piece)
		# 	lines_removed = remove_completed_lines(game_matrix)
		# 	score+=lines_removed
		# 	piece = create_piece()

		#Check if piece reaches the end
		if(piece['row']==19 or game_matrix[piece['row']+1][piece['column']]!='.'):
			game_matrix[piece['row']][piece['column']]='c'
			lines_removed=remove_completed_line(game_matrix)
			score+=lines_removed
			piece= create_piece() #removes actual falling piece, and set location of touchpiece with 'c'


		pygame.display.update()

		for event in pygame.event.get(QUIT):
			pygame.quit()
			sys.exit()


def setScore():
	#draw text with pygame
	#createFontObject
	#parameters: font type and size
	myFont= pygame.font.Font('arial.ttf',10)
	#create image of the text
	#parameters: text, antialias, color
	test_surface= myfont.render('text to display',True, (255,255,255))

	#Add text image to your game window
	#@parameters: window and location to start drawing
	screen.blit(text_surface, (100,100))

#Draw score text
def draw_score(screen,score):
	font= pygame.font.Font('freesansbold.ttf',18)
	scoreSurf=font.render('Score: %s' % score, True, (255,255,255))
	screen.blit(scoreSurf, (640-150,20))


def isOnBoard(row, column):
    return column >= 0 and column < 10 and row < 20

def listen_to_user_input(game_matrix, piece):
	for event in pygame.event.get():
		if event.type==KEYDOWN:
			if(event.key ==K_LEFT) and isValidPosition(game_matrix, piece['row'],piece['column']-1):#send row/col position
				piece['column']-=1
			if(event.key==K_RIGHT) and isValidPosition(game_matrix, piece['row'],piece['column']+1):
				piece['column']+=1
			if(event.key==K_DOWN):
				SPEED=0.1
				piece['row']+=1
			# else:
				# SPEED=1

def isValidRotationPosition(game_matrix, piece, adjColumn=0, adjRow=0):
	#loop every cell in the piece matrix and if not empty check if
	# the block is moving to a cell within the board and empty
	piece_matrix = available_tetris_pieces()[piece['shape']][0]
	for row in range(5):
		for col in range(5):
			if piece_matrix[row][col]==".":
				continue
			if not isOnBoard(piece['row']+row+adjRow, piece['column']+col+adjColumn):
				return False
			if game_matrix[piece['row']+row +adjRow][piece['column'] + col + adjColumn]!= '.':
				return False
	return True

def isValidPosition(game_matrix, row, column):

	#loop over each cell in the piece matrix and if not empty check if the block is moving ro a cell within the board and empty


	#if piece is within the board boundaries
	# if(piece['column']<=50 or piece[column]>=(20*20))
	if not (column>=0 and column <10 and row <20):
		return False
	#if space is empty on the sides
	if game_matrix[row][column]!= '.': 
		return False

	return True


#check if any cell is empty, the line is not complete so return false
def isLineComplete(game_matrix,row):
	for column in range(10): 
		if(game_matrix[row][column]=='.'): #if found a space, end the loop, not complete
			return False
	return True 

def remove_completed_line(game_matrix):
	num_lines_removed=0
	for row in range(20):
		if(isLineComplete(game_matrix,row)):
			for row_to_move_down in range(row,0,-1): #loop from the completed row to the top row [as it is going to move down all blocks]
				for column in range(10):
					game_matrix[row_to_move_down][column] = game_matrix[row_to_move_down-1][column] #move cell one row down
			#set very top line to blank
			for x in range(10):
				game_matrix[0][x]='.'
			num_lines_removed+=1
	return num_lines_removed


#will read the whole board matrix and draw a tetris_box, for each space with 'c'
def draw_board(screen, matrix):
	game_matrix_columns=10
	game_matrix_rows=20
	for row in range(game_matrix_rows):
		for column in range(game_matrix_columns):
			if(matrix[row][column]!='.'):
				create_single_tetris_box(screen, row, column, (255,255,255),(217,222,226))

def create_piece():
	piece={}
	random_shape = random.choice(list(available_tetris_pieces().keys()))
	piece['shape'] = random_shape
	piece['row']=0
	piece['column']=2 #Start position
	return piece

def draw_piece(screen, piece):
	white_color=(255,255,255)
	grey_color=(217,222,226)
	#board margin + line thickness+ (Column+box_size)
	origin_x=100+(piece['column']*20+1)
	origin_y=50+ (piece['row']*20+1)
	pygame.draw.rect(screen, grey_color, [origin_x, origin_y, 20, 20])
	pygame.draw.rect(screen, white_color, [origin_x, origin_y, 18,18])

def create_single_tetris_box(screen, matrix_cell_row, matrix_cell_column,color, clor_shadow_color):
	origin_x=100+(matrix_cell_column*20+1)
	origin_y=50+(matrix_cell_row*20+1)
	pygame.draw.rect(screen,clor_shadow_color,[origin_x,origin_y,20,20]) #draw gray square
	pygame.draw.rect(screen, color, [origin_x, origin_y,18,18]) #draw white square on top of it


def create_game_matrix():
	game_matrix_columns=10
	game_matrix_rows=20
	matrix=[]
	#TO DO
	for row in range(game_matrix_rows):
		new_row=[]
		for column in range(game_matrix_columns):
			new_row.append('.')
		matrix.append(new_row)
	return matrix

run_tetris_game()



#clock
# clock = pygame.time.Clock()