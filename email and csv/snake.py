import random
import curses

s=curses.initscr() #get the window cursor
curses.curs_set(0) #locate the cursor at the beginning
sh, sw=s.getmaxyx() #get size of the window and apply the height to sh and width to sw
sh=int(sh) #i prefer to load an int again. 
sw=int(sw) #at least until i learn how to control int and float
w= curses.newwin(sh,sw,0,0) #create window with screen size
w.keypad(1) #IDK
w.timeout(100) #IDK , cursor blinking time? SPEED

#create the snake based on the screen size
#snk_XY is the location of the head, first is located in halfHeightScreen and QuarterWidthScreen
snk_x=sw//4 
snk_y=sh//2
#snake body, out of 3 blocks, where block1 and block2 preceed block0, by 1 in x
snake=[
	[snk_y,snk_x],
	[snk_y,snk_x-1],
	[snk_y,snk_x-2]
]

#locate food in center of screen
food= [sh//2,sw//2] #double division to ensurre is an int instead of a float.

#in window add a character in the location of foodXY, and put PI character
w.addch(food[0], food[1], curses.ACS_PI)# this method requires int for values.
#set the initial direction of the snake to right
key = curses.KEY_RIGHT

#continuous loop that will read keyboard arrows presses
while True:
	next_key=w.getch()
	key = key if next_key == -1 else next_key #not sure about this condition and the else. but it controls that if the key hasnt been preesed, then continues that path
#if hasnt pressed any key [-1] nothing happen, key still key. but, ELSE ley becomes next_key

#if snake collides [coincide] with the walls or the same space as the snake it will close the app
	if snake[0][0] in [0,sh] or snake[0][1] in [0,sw] or snake[0] in snake[1]:
		curses.endwin()
		quit()

#create a newhead and place at the beginning of snake list
	new_head = [snake[0][0],snake[0][1]]   #[11,21]
#I really have no idea what is happening here. but I know depending on the arrow, it will ad a value to an element
#changing the direction
	if key== curses.KEY_DOWN:
		new_head[0]+=1                     #[12++,21]
	if key == curses.KEY_UP:
		new_head[0]-=1                     #[11--,21]
	if key == curses.KEY_RIGHT:
		new_head[1]+=1                     #[12,22++]
	if key==curses.KEY_LEFT:
		new_head[1]-=1                     #[12,21--]
#add the new head->direction to the snake
	snake.insert(0,new_head)

#snake[0] is the head of the snake
#if that position is the same as food (that is a list with 2 elements, coords)
                                           #(11,21)==(11,21):
	if snake[0] == food:
		food=None             #delete that node of coords
		while food is None:   #while it doesnt have coords, assign some random
			nf=[              #create new temp food location
				random.randint(1,sh-1),
				random.randint(1,sw-1)	
			]
			food = nf if nf not in snake else None #locate it anywhere else but the snake, else delete and start again
		w.addch(food[0],food[1],curses.ACS_PI) #place pi in coordenates of screen
	else:                          #if it is not in food, will pop a tail
		tail= snake.pop()
		w.addch(tail[0],tail[1],' ')  #place a blank space in tail. it keeps the snake in one size [ remove it] where else is used?

	w.addch(snake[0][0],snake[0][1], curses.ACS_CKBOARD) #create character ckboard in location of snakehead








