import pygame


# Initializes Pygame
pygame.init()

# Sets the screen dimensions and create a fullscreen display
screen = pygame.display.set_mode((1920, 1080), pygame.FULLSCREEN)

# Defines a dictionary, colors, which maps number keys (as strings) 
# to tuples containing the name and RGB value of each color.
colors = {
    '1': ("Black", (0, 0, 0)),
    '2': ("White", (255, 255, 255)),
    '3': ("Red", (255, 0, 0)),
    '4': ("Green", (0, 255, 0)),
    '5': ("Blue", (0, 0, 255)),
    '6': ("Yellow", (255, 255, 0)),
    '7': ("Brown", (165, 42, 42)),
    '8': ("Orange", (255, 165, 0)),
    '9': ("Purple", (160, 32, 240)),
    '0': ("Pink", (255, 192, 203))
}

# initializes current_color with the color black (as the default) 
# and sets up the text to display the currently selected color 
# and instructions for changing colors.
current_color = colors['1'][1]
color_text = "Current Color: Black"
instructions_text = """
Press number keys 
to change colors:

1 - Black
2 - White
3 - Red
4 - Green
5 - Blue
6 - Yellow
7 - Brown
8 - Orange
9 - Purple
0 - Pink
"""

# This sets up a square canvas of size 800x800 pixels. 
# The canvas is divided into cells of 20x20 pixels. 
# Each cell's initial color is set to white. 
# The canvas is a separate drawing surface that will be blitted onto the main screen.
canvas_size = 800
cell_size = 20  
canvas = pygame.Surface((canvas_size, canvas_size))
canvas.fill(colors['2'][1])  # Fill initial canvas with white

# Calculate the number of cells along each dimension
num_cells = canvas_size // cell_size

# Create a grid to track the colors of each cell
grid = [[colors['2'][1] for _ in range(num_cells)] for _ in range(num_cells)]

# Font for displaying the current color and instructions
font = pygame.font.Font(None, 36)

# draw_canvas() iterates over each cell in the grid and draws it in the color stored in grid. 
# It also draws light grey outlines around each cell.
def draw_canvas():
    for x in range(num_cells):
        for y in range(num_cells):
            rect = pygame.Rect(x * cell_size, y * cell_size, cell_size, cell_size)
            pygame.draw.rect(canvas, grid[y][x], rect)
            pygame.draw.rect(canvas, (200, 200, 200), rect, 1)  # Draw the outline with a width of 1

# draw_texts() handles rendering the current color text and the instructions on the screen.
def draw_texts():
    color_surface = font.render(color_text, True, (255, 255, 255), (100, 100, 100))
    screen.blit(color_surface, (50, 50))
    
    # Draws instruction text
    y_offset = 90
    for line in instructions_text.strip().split('\n'):
        instruction_surface = font.render(line, True, (255, 255, 255), (100, 100, 100))
        screen.blit(instruction_surface, (50, y_offset))
        y_offset += 30

# main() function runs the main loop.
# Processes key presses, mouse clicks, updates the color based on input, 
# handles drawing operations, updates the display.
def main():
    running = True
    global current_color, color_text

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                elif event.unicode in colors:
                    color_name, color_value = colors[event.unicode]
                    current_color = color_value
                    color_text = f"Current Color: {color_name}"
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Get mouse position and adjust to canvas coordinates
                mouse_x, mouse_y = pygame.mouse.get_pos()
                canvas_x = (screen.get_width() - canvas_size) // 2
                canvas_y = (screen.get_height() - canvas_size) // 2

                # Check if the click is within the canvas
                if canvas_x <= mouse_x <= canvas_x + canvas_size and canvas_y <= mouse_y <= canvas_y + canvas_size:
                    # Calculate the grid cell coordinates
                    cell_x = (mouse_x - canvas_x) // cell_size
                    cell_y = (mouse_y - canvas_y) // cell_size
                    # Change the cell color
                    grid[cell_y][cell_x] = current_color
                    
                    # If the user clicks on a cell, the color of the cell in the grid is updated to the currently selected color. 
                    # The canvas is then redrawn with the updated colors, and the screen is updated with the new frame.

        # Fills the background
        screen.fill((100, 100, 100))

        # Draws the canvas
        draw_canvas()

        # Blits the canvas onto the center of the screen
        screen.blit(canvas, ((screen.get_width() - canvas_size) // 2, (screen.get_height() - canvas_size) // 2))

        # Draws the color text and instructions
        draw_texts()

        # Updates the display
        pygame.display.flip()

    pygame.quit()
    

if __name__ == '__main__':
    main()
