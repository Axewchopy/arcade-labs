import arcade

def draw_section_outlines():
    # Draw squares on bottom
    arcade.draw_rectangle_outline(150, 150, 300, 300, arcade.color.BLACK)
    arcade.draw_rectangle_outline(450, 150, 300, 300, arcade.color.BLACK)
    arcade.draw_rectangle_outline(750, 150, 300, 300, arcade.color.BLACK)
    arcade.draw_rectangle_outline(1050, 150, 300, 300, arcade.color.BLACK)

    # Draw squares on top
    arcade.draw_rectangle_outline(150, 450, 300, 300, arcade.color.BLACK)
    arcade.draw_rectangle_outline(450, 450, 300, 300, arcade.color.BLACK)
    arcade.draw_rectangle_outline(750, 450, 300, 300, arcade.color.BLACK)
    arcade.draw_rectangle_outline(1050, 450, 300, 300, arcade.color.BLACK)


def draw_section_1():
    y = -7.5

    for row in range(30):
        x = 2.5
        y = y + 10
        for column in range(30):
            arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.WHITE)
            x = x + 10


def draw_section_2():
    contador = 0
    y = -7.5

    for row in range(30):
        x = 305
        y = y + 10
        for column in range(30):
            if (contador%2 == 0):
                arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.WHITE)

            else:
                arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.BLACK)

            x = x + 10
            contador = contador + 1



def draw_section_3():
    contador = 0
    y = -7.5

    for row in range(30):
        x = 605
        y = y + 10
        contador = contador + 1

        for column in range(30):
            if (contador % 2 == 0):
                arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.BLACK)

            else:
                arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.WHITE)

            x = x + 10



def draw_section_4():
    contadorfila = 1
    contadorcolumna = 0
    y = -7.5

    for row in range(30):
        x = 905
        y = y + 10
        contadorfila = contadorfila + 1

        for column in range(30):
            if (contadorfila % 2 != 0):
                arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.BLACK)

            elif ((contadorfila % 2 == 0) and (contadorcolumna % 2 != 0)):
                arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.BLACK)

            else:
                arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.WHITE)

            x = x + 10
            contadorcolumna = contadorcolumna + 1


def draw_section_5():
    y = 295
    x = 2.5
    cuadradosborrados = 1

    for row in range(30):
        contador = 30 - cuadradosborrados
        y = y + 10

        for column in range(contador):
            x = x + 10
            arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.WHITE)
            contador = contador - 1

        x = 2.5 + (10 * cuadradosborrados)
        cuadradosborrados = cuadradosborrados + 1



def draw_section_6():
    y = 295
    cuadradosborrados = 1

    for row in range(31):
        x = 295
        contador = 31 - cuadradosborrados
        y = y + 10

        for column in range(contador):
            x = x + 10
            arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.WHITE)
            contador = contador - 1

        cuadradosborrados = cuadradosborrados + 1


def draw_section_7():
    y = 295
    contador = 1
    cuadradospintados = 1

    for row in range(31):
        x = 595
        y = y + 10

        for column in range(contador):
            x = x + 10
            arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.WHITE)
            contador = contador - 1

        cuadradospintados = cuadradospintados + 1
        contador = cuadradospintados


def draw_section_8():
    y = 605
    x = 885
    guardarx = x
    contador = 30
    cuadradospintados = 30


    for row in range(31):
        y = y - 10
        x = guardarx + 10
        guardarx = guardarx + 10

        for column in range(contador):
            x = x + 10
            arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.WHITE)
            contador = contador - 1

        cuadradospintados = cuadradospintados - 1
        contador = cuadradospintados


def main():
    # Create a window
    arcade.open_window(1200, 600, "Lab 05 - Loopy Lab")
    arcade.set_background_color(arcade.color.AIR_FORCE_BLUE)

    arcade.start_render()

    # Draw the outlines for the sections
    draw_section_outlines()

    # Draw the sections
    draw_section_1()
    draw_section_2()
    draw_section_3()
    draw_section_4()
    draw_section_5()
    draw_section_6()
    draw_section_7()
    draw_section_8()

    arcade.finish_render()

    arcade.run()


main()