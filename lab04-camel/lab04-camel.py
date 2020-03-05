# Import the "arcade" library
import arcade
import random

def main():
    arcade.open_window(800, 600, "Camello")

    # Set the background color
    arcade.set_background_color(arcade.color.WHITE)

    arcade.start_render()

    arcade.draw_text("Welcome to Camel!", start_x=50, start_y=550, color=arcade.color.BLACK)
    arcade.draw_text("You have stolen a camel to make your way across the great Mobi desert.", start_x=50, start_y=525, color=arcade.color.BLACK)
    arcade.draw_text("The natives want their camel back and are chasing you down! Survive your", start_x=50, start_y=500, color=arcade.color.BLACK)
    arcade.draw_text("desert trek and out run the natives.", start_x=50, start_y=475, color=arcade.color.BLACK)


    done = True
    contador = 0
    x = 425
    millas = 0
    cansancio = 0
    bebidas = 3
    distancia = 20

    while done:

        arcade.draw_text("A. Drink from your canteen.", start_x=50, start_y=x, color=arcade.color.BLACK)
        arcade.draw_text("B. Ahead moderate speed.", start_x=50, start_y=x-25, color=arcade.color.BLACK)
        arcade.draw_text("C. Ahead full speed.", start_x=50, start_y=x-50, color=arcade.color.BLACK)
        arcade.draw_text("D. Stop for the night.", start_x=50, start_y=x-75, color=arcade.color.BLACK)
        arcade.draw_text("E. Status check.", start_x=50, start_y=x-100, color=arcade.color.BLACK)
        arcade.draw_text("Q. Quit.", start_x=50, start_y=x-125, color=arcade.color.BLACK)
        arcade.draw_text("What is your choice?", start_x=50, start_y=x-150, color=arcade.color.BLACK)

        arcade.finish_render()

        a = input()

        a = a.upper()

        if (a == 'Q'):
            done = False

        else:
            if (contador == 0):
                x = 550

        if (a == 'E'):
            arcade.start_render()

            print("Dato leido")
            arcade.draw_text("Millas recorridas: " + str(millas), start_x = 50, start_y = x-200, color=arcade.color.BLACK)
            arcade.draw_text("Bebidas restantes: " + str(bebidas), start_x = 50, start_y = x-225, color=arcade.color.BLACK)
            arcade.draw_text("Los nativos están a " + str(distancia) + " millas de ti", start_x=50, start_y=x-250, color=arcade.color.BLACK)

            arcade.finish_render()


borrar estas palabras





main()

# --- Finish drawing ---
arcade.finish_render()

