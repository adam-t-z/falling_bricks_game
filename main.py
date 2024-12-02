from turtle import Turtle, Screen
from paddle import Paddle
from brick import Brick
from score import ScoreBoard
import time

# Set up the screen for the game
screen = Screen()
screen.setup(width=1000, height=800)  # Set the size of the window
screen.bgcolor("black")  # Set the background color of the screen to black
screen.tracer(0)  # Disable automatic screen updates to allow manual control

# Create game objects: paddle, brick, and score board
paddle = Paddle()  # The player's paddle
brick = Brick()  # The falling brick
score = ScoreBoard()  # The score board to keep track of the player's score

# Set up keyboard controls for moving the paddle
screen.listen()  # Listen for user input
screen.onkey(paddle.move_right, "Right")  # Move the paddle right when the right arrow key is pressed
screen.onkey(paddle.move_left, "Left")  # Move the paddle left when the left arrow key is pressed

# Initial game settings
sleep_time = 0.1  # Time delay for each game frame (controls game speed)
game_on = True  # Flag to control the game loop

# Main game loop
while game_on:
    time.sleep(sleep_time)  # Pause for a short time between frames to control speed
    screen.update()  # Update the screen manually

    brick.go_down()  # Move the brick down the screen

    # Check if the brick is close enough to the paddle and if it's in the collision zone
    if paddle.distance(brick) <= 70 and brick.ycor() <= -330:
        # If the brick is a "turtle" and white, the game ends
        if brick.shape() == "turtle" and brick.color()[0] == "white":
            game_on = False  # End the game
            screen.bgcolor("red")  # Change the background color to red to indicate game over
            score.game_over()  # Display the game over message

        # Update score based on the brick's shape
        if brick.shape() == "circle":
            score.update_score(1)  # Add 1 point for a circle brick
        elif brick.shape() == "square":
            score.update_score(2)  # Add 2 points for a square brick
        elif brick.shape() == "turtle":
            score.update_score(5)  # Add 5 points for a turtle brick
        elif brick.shape() == "triangle":
            score.update_score(is_triangle=True)  # Special rule for triangle-shaped bricks
            brick.ymove = 10  # Set a custom movement for triangle-shaped bricks
        
        # Reset the brick's position after it collides with the paddle
        brick.random_turtle()  
        
        # Gradually speed up the game by reducing the sleep time
        sleep_time *= 0.9  
    
    # If the brick moves past the bottom of the screen, reset its position and slow down the game
    if brick.ycor() <= -400:
        brick.random_turtle()  # Reset the brick position
        sleep_time *= 1.1  # Slow down the game by increasing the sleep time

# Wait for the user to click on the screen to exit the game
screen.exitonclick()
