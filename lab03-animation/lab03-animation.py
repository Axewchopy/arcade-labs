# Import the "arcade" library
import arcade

def main():
    arcade.open_window(800, 600, "Dibujo navideño")

    # Set the background color
    arcade.set_background_color(arcade.color.QUEEN_BLUE)

    arcade.schedule(on_draw, 1/60)

    arcade.run()


def muñeco():
    # Bola de nieve (abajo)
    arcade.draw_circle_filled(400, 175, 120, arcade.color.WHITE)

    # Bola de nieve (borde abajo)
    arcade.draw_circle_outline(400, 175, 120, arcade.color.BLACK, 3)

    # Bola de nieve (arriba)
    arcade.draw_circle_filled(400, 300, 75, arcade.color.WHITE)

    # Bola de nieve (borde arriba)
    arcade.draw_circle_outline(400, 300, 75, arcade.color.BLACK, 3)

    # Zanahoria
    arcade.draw_triangle_filled(400, 300, 400, 275, 350, 275, arcade.color.ORANGE)

    # Ojo izquierdo
    arcade.draw_circle_filled(370, 320, 10, arcade.color.BLACK)

    # Ojo derecho
    arcade.draw_circle_filled(400, 320, 10, arcade.color.BLACK)

    # Boton 1
    arcade.draw_circle_filled(400, 170, 5, arcade.color.BLACK)

    # Boton 2
    arcade.draw_circle_filled(400, 190, 5, arcade.color.BLACK)

    # Boton 3
    arcade.draw_circle_filled(400, 210, 5, arcade.color.BLACK)

    # Brazo
    arcade.draw_polygon_filled([[490, 175],
                                [550, 225],
                                [565, 210],
                                [580, 230],
                                [570, 235],
                                [565, 225],
                                [560, 230],
                                [570, 240],
                                [560, 245],
                                [550, 235],
                                [540, 240],
                                [550, 250],
                                [540, 255],
                                [525, 235],
                                [530, 230],
                                [480, 190]],
                                arcade.color.RUSSET)


def copos(a, b):
    # Copos
    a_aux = a
    b_aux = b
    c = 650
    d = 640

    for t in range (7):

        for i in range (8):
            arcade.draw_circle_filled(c, b, 5, arcade.color.WHITE)
            arcade.draw_circle_filled(d, a, 5, arcade.color.WHITE)

            a = a - 100
            b = b - 100

        c = c - 75
        d = d - 75
        a = a_aux
        b = b_aux

def nube():
    # Nube
    arcade.draw_circle_filled(225, 570, 50, arcade.color.PASTEL_PURPLE)
    arcade.draw_circle_filled(300, 550, 60, arcade.color.PASTEL_PURPLE)
    arcade.draw_circle_filled(325, 570, 50, arcade.color.PASTEL_PURPLE)
    arcade.draw_circle_filled(400, 550, 60, arcade.color.PASTEL_PURPLE)
    arcade.draw_circle_filled(425, 570, 50, arcade.color.PASTEL_PURPLE)
    arcade.draw_circle_filled(500, 550, 60, arcade.color.PASTEL_PURPLE)
    arcade.draw_circle_filled(525, 570, 50, arcade.color.PASTEL_PURPLE)
    arcade.draw_circle_filled(600, 560, 60, arcade.color.PASTEL_PURPLE)


def on_draw(delta_time):

    arcade.start_render()

    arcade.draw_lrtb_rectangle_filled(0, 800, 250, 0, arcade.color.SAGE)
    muñeco()

    copos(on_draw.primerdato, on_draw.segundodato)

    on_draw.primerdato -= 20 * delta_time
    on_draw.segundodato -= 20 * delta_time

    nube()


on_draw.primerdato = 600
on_draw.segundodato = 650

main()

