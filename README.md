# pac man
its old game we all played before 

![Screenshot 2024-07-10 162730](https://github.com/Basil0X7/pac-man/assets/116971576/a74de635-faeb-46b5-abdb-6ae212ef8bb2)

# The ideas of ​​the game
- eat all pellets that player have to do it 
- let ghost catch pac man before he eats all pellets 
- When Pac-Man eats large pellets, he turns into a monster and can eat ghosts for a period of time

# board 

It is a road or a path through which Pac-Man and the ghosts can walk. \
It is numbers that you,through the pygame library, convert each number to either a line, a quarter circle, or an big and small pellets.

# fanctions

### check_collisions

- its let pac-man eat small pilets and big one
- if pac-man eat big pilets its turns up to monster and can eat ghosts

### draw_misc

- draw score
- if you eat big pilets its give you blue circle to let you now you are monster now 
- draw lives icone

### draw_board

- draw evry pilets small one and big one (add andreo tat here)
- draw evry line and corners

### draw_player

- draw player in evry direction he go to (up, down, left, right)

### check_position

- know the direction for the player

### move_player

- when player take direction up for exaple this function let player move in that direction if it can be

### get_targets

- let player thake the portels in the board
- let ghost target be the player if thay are alive and the plyer is not monster
- let ghost runaway from player if he is a monster if thay are not eaten
- let ghost go to the box if thay are have eaten from monster

# ghost class

It was the hardest part, as I am still a beginner in pygame and games in general (im a gamer by the way), \
so I had to identify the places where the ghost could walk in and then make him track Pac-Man. \
It is easier said than done, Trust me.

### def __init__

evry ghost have :
- posetion x in board
- posetion y in board
- target go to it
- speed
- img
- direction
- if he is dead
- if he in box
- id

### draw

- draw the ghost if thay are not scared of monster and not dead
- draw the ghost if thay are scared of monster and not dead
- draw the ghost if thay are dead

### check_collisions

- let you know if the ghost in box or not
- let the ghost know where he can go or not go
- let the ghost know he can go (up, down, left, right) now or he can't
like if he's direction is left or righte he can go up or down if it possible in the board

### move_blinky, move_pinky, move_inky, move_clyde

those functions in class are maked to 
- let four ghost maving in the direction that thay are takes
- let four use the portel in the board
if you open those functions you will see thay have a lot of if statment ?
- To cover all the possibilities of where the ghost might be and where it might move from its current location

In conclusion, this is just a simplified explanation of what is inside the ghost class. If you open it, you will see and understand it well (I don’t like talking, I like application).

# Current game mode

You can download it and play it continuously. There are only some (this is expected). \
I added some memes,but I want to add sounds, and perhaps I will add levels to increase the difficulty, \
but I want some advice about ghosts.
