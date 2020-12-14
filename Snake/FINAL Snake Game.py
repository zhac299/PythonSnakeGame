import simplegui, random
from user305_o32FtUyCKk_0 import Vector

#Constant Values
CANVAS_WIDTH = 800
CANVAS_HEIGHT = 800

SNAKE_STARTING_POS = 400

#Varible checks including Score, lives and game running checks
x = 0
score = 0
lives = 3
dead = False
gameRun = True

enemy = []
obstacle = []

gap = 200
alongline = False

Down =False
Up = False
Left = False
Right = False 

snake_col = ''
user_input = ""

welcome_close = False
scorepage_close = False

#Hold the high scores
score1 = 0
score2 = 0
score3 = 0


#Code below allows the user to choose the colour of the snake
def choose_snake_col():
    global snake_col, user_input

    if (user_input == ""):
        user_input = raw_input("What Colour do you want your snake to be? (Red (R), White (W) or Yellow (Y)")
    
    if (user_input == "R"):
        snake_col = 'Red'
    elif (user_input == "W"):
        snake_col = 'White'
    elif (user_input == "Y"):
        snake_col = 'Yellow'
    else:
        print("Input not recognized, snake will be default colour.")
        snake_col = 'White'

#Creates objects whcih are used in the game
def create_objects():
    #increases the scope of all the named variables
    global newSnake, newFood, enemy, line1B, B1, line1E, E1, line2B, B2, line2E, E2, lineL, interaction
    
    #creating objects below        
    newSnake = Snake(SNAKE_STARTING_POS, SNAKE_STARTING_POS, 5, snake_col)
    newFood = Food()
    enemy = Enemy(random.randrange(10, CANVAS_WIDTH - 100, 33), random.randrange(0, CANVAS_WIDTH - 100, 33), 5, snake_col)

    line1B = Obstacle([0, 150], [random.randint(50,600), 150], 15, 'White')
    B1 = line1B.p2[0] + 10
    line1E = Obstacle([line1B.p2[0] + gap, 150], [CANVAS_WIDTH, 150], 15, 'White')
    E1 = line1B.p2[0] + gap - 10
    line2B = Obstacle([0, 650], [random.randint(50, 600), 650], 15, 'White')
    B2 = line2B.p2[0] + 10
    line2E = Obstacle([line2B.p2[0] + gap, 650], [CANVAS_WIDTH, 650], 15, 'White')
    E2 = line2B.p2[0] + gap - 10
    lineL = [line1B, line1E, line2B, line2E]

    for x in lineL:
        obstacle.append(x)
    
    interaction = Interaction(newSnake, newFood, enemy, obstacle)   
    
#Method below sorts the scores for the scoreboard        
def score_sorter():
    global score, score1, score2, score3
    
    #simple compare and sort algorithm
    if (score > score1):
        score1 = score
    elif (score > score2 and score < score1):
        score2 = score
    elif (score > score3 and score < score2):
        score3 = score        

#Method below compares scores for the scoreboard
def score_compare():
    #increase the scope of named variables
    global score, score1, score2, score3
    
    #compares the players score to the old score1 and score2 and replace them accordingly
    if (score > score1):
        score3 = score2
        score2 = score1
        score1 = score
    elif (score > score2):
        score3 = score2
        score2 = score
        
#Method below is the mouse_handler for the welcome page    
def mouse_handler(pos): 
    #increases the scope of frame
    global frame
    
    #when the user clicks the start button will open the main frame for the game
    if pos > (CANVAS_WIDTH/2 - 60, CANVAS_HEIGHT/2) and pos < (CANVAS_WIDTH/2 + 40, CANVAS_HEIGHT/2 - 5):
        frame = simplegui.create_frame("Snake", CANVAS_WIDTH, CANVAS_HEIGHT) 
        frame.start()
        frame.set_draw_handler(interaction.draw)
        frame.set_keydown_handler(interaction.keydown)

        #closes the welcome window
        welcome.stop() 
        
#Method below produces the welcome page
def welcomepage(canvas):
    #design for the welcome page
    canvas.draw_text("Group 13: Snake Game", (CANVAS_WIDTH/2 - 225, CANVAS_HEIGHT/ 3), 50, "Red")
    canvas.draw_polygon([(CANVAS_WIDTH / 2 - 60, CANVAS_HEIGHT/2 -5), (CANVAS_WIDTH/2 + 40, CANVAS_HEIGHT/2 -5)], 40, 'White')
    canvas.draw_text("Start", (CANVAS_WIDTH/2 - 40, CANVAS_HEIGHT/2), 30, "Blue")
    
    #displays the instructions for the game for the user
    canvas.draw_text("To move the snake around use the arrow keys.", (CANVAS_WIDTH/2 - 375, CANVAS_HEIGHT/1.75 + 100), 40, "White")
    canvas.draw_text("Collect as many pellets as you can!", (CANVAS_WIDTH/2 - 300, CANVAS_HEIGHT/1.75 + 150), 40, "White")       
        
#Method below opens the welcome page    
def open_welcomepage():
    #allows methods that would normally be out of welcome's scope
    global welcome
    
    #creates the frame for the welcome page        
    welcome = simplegui.create_frame("Menu", CANVAS_WIDTH, CANVAS_HEIGHT) 
    welcome.set_draw_handler(welcomepage)
    welcome.set_mouseclick_handler(mouse_handler)
    
    #starts the welocme frame
    welcome.start()

#Method below maps the keys used on the score page        
def scorepage_keyhandler(key):
    #increases scope of dead
    global dead, lives, score, obstacle
    
    #if statement checks if the user has pressed the space key
    if key == simplegui.KEY_MAP['space']:
        #closes the scorepage
        scorepage.stop()
        
        #recreates the game environment
        #empties the list
        del obstacle[:]
        
        #creates new lines each time the game is restarted
        line1B = Obstacle([0, 150], [random.randint(50,600), 150], 15, 'White')
        B1 = line1B.p2[0] + 10
        line1E = Obstacle([line1B.p2[0] + gap, 150], [CANVAS_WIDTH, 150], 15, 'White')
        E1 = line1B.p2[0] + gap - 10
        line2B = Obstacle([0, 650], [random.randint(50, 600), 650], 15, 'White')
        B2 = line2B.p2[0] + 10
        line2E = Obstacle([line2B.p2[0] + gap, 650], [CANVAS_WIDTH, 650], 15, 'White')
        E2 = line2B.p2[0] + gap - 10
        lineL = [line1B, line1E, line2B, line2E]
        
        #adding lines to obstacle
        for x in lineL:
            obstacle.append(x)
        
        #adding the new lines to the interaction object
        interaction = Interaction(newSnake, newFood, enemy, obstacle) 
        
        #reseting some variables back to their original values
        dead = False
        lives = 3
        score = 0
        
        frame = simplegui.create_frame("Snake", CANVAS_WIDTH, CANVAS_HEIGHT) 
        frame.start()
        frame.set_draw_handler(interaction.draw)
        frame.set_keydown_handler(interaction.keydown)

#Method below calls the score_sorted method to sort the scores as well as display them        
def score_page(canvas):
    #design for the score page
    canvas.draw_text("1: " +str(score1), (CANVAS_WIDTH/2 - 100 , CANVAS_HEIGHT/3), 50, "Red")
    canvas.draw_text("2: " +str(score2), (CANVAS_WIDTH/2 - 100 , CANVAS_HEIGHT/3 + 100), 50, "White")
    canvas.draw_text("3: " +str(score3), (CANVAS_WIDTH/2 - 100 , CANVAS_HEIGHT/3 + 250), 50, "Yellow")
    canvas.draw_text("To restart press space.", (CANVAS_WIDTH/2 - 100 , CANVAS_HEIGHT/3 + 350), 50, "Green")   

#Method below opens the score page    
def open_scorepage():
    #allows methods that would normally be out of welcome's scope
    global scorepage
    
    #makes a call to the score_sorter method and the score_compare method
    score_compare()
    score_sorter()
    
    #frame for score page        
    scorepage = simplegui.create_frame("Scoreboard", CANVAS_WIDTH, CANVAS_HEIGHT) 
    scorepage.set_draw_handler(score_page)
    scorepage.set_keydown_handler(scorepage_keyhandler)

    #starts the scorepage frame
    scorepage.start()
        

#Food Class        
class Food():
    #initiates varaible method
    def __init__(self):
        self.pos = Vector(random.randint(1,CANVAS_WIDTH), random.randint(1,CANVAS_HEIGHT))
        self.rad = 5
    
    #draws the food to the canvas
    def draw(self, canvas):
        canvas.draw_circle((self.pos.x, self.pos.y), self.rad, 1, "Red", "Red")


#Obstacle Class        
class Obstacle():
    #initiates the variables for the Obstacle class
    def __init__(self, p1, p2, width, color):
        self.p1 = p1
        self.p2 = p2
        self.width = width
        self.color = color
        
    #draws the obstacle to the canvas        
    def draw(self, canvas):
        canvas.draw_line(self.p1, self.p2, self.width, self.color)

        
#Snake Class        
class Snake():
    #initiates variables used by the snake Class
    def __init__(self, snakeX, snakeY, snakeRad, snakeCol):
        self.snakeX = snakeX
        self.snakeY = snakeY
        self.snakePos = [[self.snakeX, self.snakeY]]
        self.snakeRad = snakeRad
        self.snakeScalar = Vector(0, 0)
        self.snakeTails = 40
        self.speedScalar = 1
        self.x = 0
        self.snakeCol = snakeCol

    #consistently updates variables
    def update(self):
        global score, lives
        
        if gameRun:
            #used to increase the speed + size of the snake
            self.snakeX += self.snakeScalar.x * self.speedScalar
            self.snakeY += self.snakeScalar.y * self.speedScalar
    
    #Draws the snake to the canvas as well as call the update method above to keep snake moving
    def draw(self, canvas):

        #draws the snake to the canvas
        for snake in self.snakePos:
            canvas.draw_circle(snake, self.snakeRad, 1, self.snakeCol, self.snakeCol)
            
        #making the snake a constant size
        while(self.x<self.snakeTails):    
            self.snakePos.append([-50, -50])
            self.x += 1
            
        #adding the body of the snake   
        self.snakePos.pop(-1)
        self.snakePos.insert(0, [self.snakeX, self.snakeY])   
        self.update()
        
        
#Enemy Class       
class Enemy(Snake):
    #Initiates required variables
    def __init__(self, snakeX, snakeY, snakeRad, snakeCol):
        #Inherit Snake's init function
        Snake.__init__(self, snakeX, snakeY, snakeRad, snakeCol)
        
    #Used to keep varaibles updated while the game is running
    def update(self):
        global score, lives
        
        if gameRun:
            #used to increase the speed + size of the snake
            self.snakeX += self.snakeScalar.x * self.speedScalar
            self.snakeY += self.snakeScalar.y * self.speedScalar
            
        #enemy snake hit wall then it turns around
        for x in self.snakePos:
            if (x[0] <= 0):
                self.snakeScalar = Vector(0.5,0)
            elif (x[1] <= 0):
                self.snakeScalar = Vector(0, 0.5)
            elif (x[0] >= CANVAS_WIDTH):
                self.snakeScalar = Vector(-0.5,0)
            elif (x[1] >= CANVAS_HEIGHT):
                self.snakeScalar = Vector(0,-0.5)

    #Draws the enemies to the canvas as well as keep variables updated via update method
    def draw(self, canvas):
        
        #drawing the enemy to the canvas
        for snake in self.snakePos:
            canvas.draw_circle(snake, self.snakeRad, 1, "green", "green")
        
        #creating the snake tail
        while(self.x < self.snakeTails):    
            self.snakePos.append([-1, -1])
            self.x += 1
        
        #adding to the body
        self.snakePos.pop(-1)
        self.snakePos.insert(0, [self.snakeX, self.snakeY])   
        self.update()
        
        
#Interaction Class            
class Interaction():
    #Initiates required variables
    def __init__(self, snake, food, enemy, obstacle):
        self.snake = snake
        self.food = food
        self.enemy = enemy
        self.obstacle = obstacle

    #Consistently keeps all the game variables updated that are being used
    def update(self):
        global score, lives, dead, B1, B2, E1, E2, Up, Down, Left, Right, alongline, SNAKE_STARTING_POS

        #makes a call to the update methods for each object snake and enemy
        self.snake.update()
        self.enemy.update()
            
        #check if snake eats food
        if(self.food.pos.x - 2.5 * self.snake.snakeRad <= self.snake.snakeX and self.food.pos.x + 2.5 * self.snake.snakeRad >= self.snake.snakeX and self.food.pos.y - self.snake.snakeRad < self.snake.snakeY and self.food.pos.y + self.snake.snakeRad > self.snake.snakeY):
            #increment the score by 1 if the player snake is in contact with the food
            score += 1
            #increase the speed + size of snake when it consumes food
            self.snake.speedScalar += 0.1
            self.food.pos = Vector(random.randint(1, CANVAS_WIDTH), random.randint(1, CANVAS_HEIGHT))
            Down = False
            Up = False
            Left = False
            Right = False
            
        #check if snake touches border
        if(self.snake.snakeX > CANVAS_WIDTH or self.snake.snakeY > CANVAS_HEIGHT or self.snake.snakeX < 0 or self.snake.snakeY < 0):
            #checks users current amount of lives and adjusts them appropriatly as well as reseting the snake back to its starting position
            if(lives == 3):
                lives = 2
                self.snake.snakeX = SNAKE_STARTING_POS
                self.snake.snakeY = SNAKE_STARTING_POS
            elif(lives == 2):
                lives = 1
                self.snake.snakeX = SNAKE_STARTING_POS
                self.snake.snakeY = SNAKE_STARTING_POS
            elif(lives == 1):
                lives = 0
                dead = True
                open_scorepage()

        #code runs for the obstacle which is the line
        for line in self.obstacle:
            HalfW = line.width/2 + 10
            
            #food so its not between border
            if (self.food.pos.y > line.p1[1] - HalfW and self.food.pos.y < line.p1[1] + HalfW) and (self.food.pos.x > line.p1[0] and self.food.pos.x < line.p2[0]):
                self.food.pos = Vector(random.randint(10,CANVAS_WIDTH), random.randint(10, CANVAS_HEIGHT))
                
            #player touches the line
            if (self.snake.snakeY > line.p1[1] - HalfW and self.snake.snakeY < line.p1[1] + HalfW) and (self.snake.snakeX >line.p1[0] and self.snake.snakeX < line.p2[0]):
                lives -= 1
                self.snake.snakeX = SNAKE_STARTING_POS
                self.snake.snakeY = SNAKE_STARTING_POS
                
                if lives == 0:
                    dead = True
                    open_scorepage()
             
            #enemy not hitting line
            if (self.enemy.snakeY > line.p1[1] - HalfW and self.enemy.snakeY < line.p1[1] + HalfW) and (self.enemy.snakeX > line.p1[0] and self.enemy.snakeX < line.p2[0]):
                if self.enemy.snakeY < CANVAS_HEIGHT/2:
                    if self.enemy.snakeX < B1:
                        self.enemy.snakeScalar = Vector(0.5, 0)
                    elif self.enemy.snakeX > E1:
                        self.enemy.snakeScalar = Vector(-0.5, 0)
                elif self.enemy.snakeY > CANVAS_HEIGHT/2:
                    if self.enemy.snakeX < B2:
                        self.enemy.snakeScalar = Vector(0.5, 0)
                    elif self.enemy.snakeX > E2:
                        self.enemy.snakeScalar = Vector(-0.5, 0)
                        
                alongline = True
                Down =False
                Up = False
                Left = False
                Right = False 
                
        if alongline and self.enemy.snakeY < CANVAS_HEIGHT/2:
            if (self.enemy.snakeX == B1 or self.enemy.snakeX == E1):
                alongline = False 
        elif alongline and self.enemy.snakeY > CANVAS_HEIGHT/2:
            if (self.enemy.snakeX == B2 or self.enemy.snakeX == E2):
                alongline = False

            
        #enemy trying to get the food 
        if not alongline:
            if not Down and (self.enemy.snakeY - self.food.pos.y) > 0:
                self.enemy.snakeScalar = Vector(0, -0.5)            
                Up = True
            elif not Up and (self.enemy.snakeY - self.food.pos.y) < 0:
                self.enemy.snakeScalar = Vector(0, 0.5)
                Down = True
            else:
                if not Right and(self.enemy.snakeX - self.food.pos.x) > 0:
                    self.enemy.snakeScalar = Vector(-0.5, 0)
                    Left = True
                elif not Left and(self.enemy.snakeX - self.food.pos.x) < 0:
                    self.enemy.snakeScalar = Vector(0.5, 0)            
                    Right = True
                    
        #reposition food if the enemy gets it
        if(self.food.pos.x - 2.5 * self.enemy.snakeRad <= self.enemy.snakeX and self.food.pos.x + 2.5 * self.enemy.snakeRad >= self.enemy.snakeX and self.food.pos.y - self.enemy.snakeRad < self.enemy.snakeY and self.food.pos.y + self.enemy.snakeRad > self.enemy.snakeY):
            self.food.pos = Vector(random.randint(10,CANVAS_WIDTH), random.randint(10, CANVAS_HEIGHT))
            Down =False
            Up = False
            Left = False
            Right = False 
                
    #Draws information and objects to the canvas as well as keeping variables updated via update method from above
    def draw(self, canvas):
        #calls the local class update method
        self.update()

        #displays the score and the number of lives so the user can see the value of both variables
        canvas.draw_text(('Score: ' + str(score)), (0, 40), 40, 'Red')
        canvas.draw_text(('Lives: ' + str(lives)), (650, 40), 40, 'Red')

        #calls the draw method for each object from their class
        self.snake.draw(canvas)
        self.food.draw(canvas)
        self.enemy.draw(canvas)

        #draws the line to the canvas
        for b in self.obstacle:
            b.draw(canvas)
            
        #when user has no lives left
        if(dead):
            self.snake.snakeScalar = Vector(0,0)
            
    #Holds code which controls what happens when keys are pressed            
    def keydown(self, key):
        if key == simplegui.KEY_MAP['down']:
            self.snake.snakeScalar = Vector(0,0.5)
            
        if key == simplegui.KEY_MAP['up']:
            self.snake.snakeScalar = Vector(0,-0.5)
            
        if key == simplegui.KEY_MAP['left']:
            self.snake.snakeScalar = Vector(-0.5,0)
            
        if key == simplegui.KEY_MAP['right']:
            self.snake.snakeScalar = Vector(0.5,0)            

            
#calls the named method below which allows the user to select the colour of their snake
choose_snake_col()
#calls the create_objects method which creates all the objects used in the game
create_objects()
#calls the open welcomepage method which opens the welcome page
open_welcomepage()       