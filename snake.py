import turtle
import random #We'll need this later in the lab

turtle.tracer(1,0) #This helps the turtle move more smoothly

SIZE_X=800
SIZE_Y=500
turtle.setup(SIZE_X, SIZE_Y) #Curious? It's the turtle window  
                             #size. 
turtle.penup()

SQUARE_SIZE = 20
START_LENGTH = 6

#Initialize lists
pos_list = []
stamp_list = []
food_pos = []
food_stamps = []

#Set up positions (x,y) of boxes that make up the snake
snake = turtle.clone()
snake.shape("square")

#Hide the turtle object (it's an arrow - we don't need to see it)
turtle.hideturtle()

#Draw a snake at the start of the game with a for loop
#for loop should use range() and count up to the number of pieces
#in the snake (i.e START_LENGTH)

for positions in range(START_LENGTH) :

    x_pos=snake.pos()[0]  #Get x-position with snake.pos()[0]
    y_pos=snake.pos()[1]

    #Add SQUARE_SIZE to x_pos. Where does x_pos point to now?
    # You're RIGHT!
    x_pos+=SQUARE_SIZE

    my_pos=(x_pos,y_pos) #Store position variables in a tuple
    snake.goto(x_pos,y_pos)    #Move snake to new (x,y)

    #Append the position tuple to pos_list
    pos_list.append(my_pos)

    #Save the stamp ID! You'll need to erase it later. Then append
    # it to stamp_list.
    stamp_ID=snake.stamp()
    stamp_list.append(stamp_ID)

START_LENGTH = 6

UP_ARROW = "Up" #Make sure you pay attention to the upper and the lower case
LEFT_ARROW = "Left" #Make sure you pay attention to the upper and the lower case
DOWN_ARROW = "Down" #Make sure you pay attention to the upper and the lower case
RIGHT_ARROW = "Right" #Make sure you pay attention to the upper and the lower case
TIME_STEP = 100 #Update snake position after this many milliseconds

SPACEBAR = "space" # Careful, it's not supposed to be capitalized!

UP = 0

#1. Make variables LEFT , DOWN , and RIGHT with values 1,2, and 3
####WRITE YOUR CODE HERE!!

LEFT = 1
DOWN = 2
RIGHT = 3

direction = UP

UP_EDGE = 250
DOWN_EDGE = -250
RIGHT_EDGE = 400
LEFT_EDGE = -400

#2. Make functions down(), left(), and right() that change diection
####WRITE YOUR CODE HERE!!
    
def up():
    global direction
    direction=UP #change direction to up
    #move_snake() #update the snake drawing <- remember me later
    print ("You pressed the up key!")

def left():
    global direction
    direction=LEFT
    #move_snake()
    print ("You pressed the left key!")

def down():
    global direction
    direction=DOWN
    #move_snake()
    print ("You pressed the down key!")

def right():
    global direction
    direction=RIGHT
    #move_snake()
    print ("You pressed the right key!")

turtle.onkeypress(up, UP_ARROW) # Create listener for up key
    
#3. Do the same for the other arrow keys
####WRITE YOUR CODE HERE!!

turtle.onkeypress(left, LEFT_ARROW)
turtle.onkeypress(down, DOWN_ARROW)
turtle.onkeypress(right, RIGHT_ARROW)

turtle.listen()

def move_snake():
    my_pos = snake.pos()
    x_pos = my_pos[0]
    y_pos = my_pos[1]

    if direction == RIGHT:
        snake.goto(x_pos + SQUARE_SIZE, y_pos)
        print ("You moved right!")
    elif direction == LEFT:                     #4. Write the conditioins for UP and
        snake.goto(x_pos - SQUARE_SIZE, y_pos)  # DOWN on your own
        print ("You moved left!")               #### YOUR CODE HERE
    elif direction == UP:
        snake.goto(x_pos, y_pos + SQUARE_SIZE)
        print ("You moved up!")
    elif direction == DOWN:
        snake.goto(x_pos, y_pos - SQUARE_SIZE)
        print ("You moved down!")

    
    new_pos = snake.pos()
    new_x_pos = new_pos[0]
    new_y_pos = new_pos[1]
    
    # The next three lines check if the snake is hitting the right edge 

    if new_x_pos >= RIGHT_EDGE:
        print ("You hit the right edge! Game over!")
        quit ()

    elif new_x_pos <= LEFT_EDGE:
        print ("You hit the left edge! Game over!")
        quit ()

    elif new_y_pos >= UP_EDGE:
        print ("You hit the top edge! Game over!")
        quit ()

    elif new_y_pos <= DOWN_EDGE:
        print ("You hit the bottom edge! Game over!")
        quit ()
    
    #Stamp new element and append new stamp in list
    #Remember: The snake position changed - update my_pos()
    
    ######## SPECIAL PLACE - Remember it for part 5
    #pop zeroth element in pos_list to get rid of last the last piece of the tail
    grow = False
    global food_stamps, food_pos
    #If snake is on topo  of the food item
    if snake.pos() in food_pos :
        food_ind=food_pos.index(snake.pos()) #What does this do ?
        food.clearstamp(food_stamps[food_ind]) #Remove eaten food stamp
        print ("You have eaten the food!")

        food_pos.pop(food_ind)   #Remove eaten food position
        food_stamps.pop(food_ind)#Remove eaten food stamp
        print ("You have eaten the food!")
        make_food()
        grow = True
    if grow:
        #do this and that
        my_pos = snake.pos()
        pos_list.append(my_pos)
        new_stamp = snake.stamp()
        #old_stamp = stamp_list.pop(0)
        
        grow = False
    else:
        
        my_pos = snake.pos()
        pos_list.append(my_pos)
        new_stamp = snake.stamp()
        old_stamp = stamp_list.pop(0)
        snake.clearstamp(old_stamp)
        pos_list.pop(0)
        
    stamp_list.append(new_stamp)
        
    

    if snake.pos() in pos_list[0:-1]:
        quit()

    turtle.ontimer(move_snake,TIME_STEP)

def make_food():
    
    #The screen positions go from -SIZE/2 to +SIZE/2
    #But we need to make food pieces only appear on game squares
    #So we cut up the game board into multiples of SQUARE_SIZE.

    min_x=-int(SIZE_X/2/SQUARE_SIZE)+1
    max_x=int(SIZE_X/2/SQUARE_SIZE)-1
    min_y=-int(SIZE_Y/2/SQUARE_SIZE)-1
    max_y=int(SIZE_Y/2/SQUARE_SIZE)+1

    #Pick a position that is a random multiple of SQUARE_SIZE
    food_x = random.randint(min_x,max_x)*SQUARE_SIZE
    food_y = random.randint(min_y,max_y)*SQUARE_SIZE
    
    food.goto(food_x,food_y)
    food_pos.append((food_x,food_y))
    food_stamps.append(food.stamp())
    

    
turtle.register_shape("trash.gif") # Add trash picture
                                   # Make sure you have downloaded this shape
                                   #from the Google Drive folder and saved it
                                   #in the same folder as this Python script
    
food = turtle.clone()
food.shape ("trash.gif")

# locations of food

food_pos = [(100,100) , (-100,100) , (-100,-100) , (100,-100)]

# Write the code that:
#1. moves the food turtle to each food position
#2. stamps the food turtle at that location
#3. saves the stamp by appending it to the food_stamp list
# using food_stamp.append()

for this_food_pos in food_pos :
    
    food.goto(this_food_pos)
    foodstamps = food.stamp()
    food_stamps.append(foodstamps)

    
    
move_snake()




        
    
