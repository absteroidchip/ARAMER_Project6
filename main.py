import time
import types

import arcade
import random

import moving_data


def main():
    window = moving_data.Comp151Window(800, 800, "Frogger")
    window.background_color = arcade.color.AFRICAN_VIOLET
    # all images and starting coordinates below:
    window.frog = arcade.Sprite("frog.png")
    window.frog.center_x = 400
    window.frog.center_y = 50
    window.frog_dx = 0 # what are these two lines for
    window.frog_dy = 0
    window.blue_bug = arcade.Sprite("blue_bug.png")
    window.blue_bug.center_x = 0
    window.blue_bug.center_y = 142.5
    window.blue_mercedes = arcade.Sprite("blue_mercedes.png")
    window.blue_mercedes.center_x = 800
    window.blue_mercedes.center_y = 397.5
    window.yellow_porsche = arcade.Sprite("yellow_porsche.png")
    window.yellow_porsche.center_x = 0
    window.yellow_porsche.center_y = 312.5
    window.yellow_porsche2 = arcade.Sprite("yellow_porsche.png")
    window.yellow_porsche2.center_x = 300
    window.yellow_porsche2.center_y = 312.5
    window.white_jaguar = arcade.Sprite("white_jaguar.png")
    window.white_jaguar.center_x = 800
    window.white_jaguar.center_y = 227.5
    window.white_jaguar2 = arcade.Sprite("white_jaguar.png")
    window.white_jaguar2.center_x = 300
    window.white_jaguar2.center_y = 227.5
    window.log = arcade.Sprite("log.png")
    window.log.center_x = 800
    window.log.center_y = 657.5
    window.log2 = arcade.Sprite("log.png")
    window.log2.center_x = 550
    window.log2.center_y = 657.5
    window.log3 = arcade.Sprite("log.png")
    window.log3.center_x = 200
    window.log3.center_y = 657.5
    window.turtle = arcade.Sprite("turtle.png")
    window.turtle.center_x = 0
    window.turtle.center_y = 572.5
    window.turtle2 = arcade.Sprite("turtle.png")
    window.turtle2.center_x = 257
    window.turtle2.center_y = 572.5
    window.turtle3 = arcade.Sprite("turtle.png")
    window.turtle3.center_x = 654
    window.turtle3.center_y = 572.5
    #each lane  should have different spacing between cars
    # Below are the Road Sections
    window.start_zone = arcade.create_rectangle_filled(400, 50, 800, 100, arcade.color.AERO_BLUE)
    window.road1 = arcade.create_rectangle_filled(400, 142.5, 800, 85, arcade.color.LIGHT_GRAY)
    window.road2 = arcade.create_rectangle_filled(400, 227.5, 800, 85, arcade.color.LIGHT_GRAY)
    window.road3 = arcade.create_rectangle_filled(400, 312.5, 800, 85, arcade.color.LIGHT_GRAY)
    window.road4 = arcade.create_rectangle_filled(400, 397.5, 800, 85, arcade.color.LIGHT_GRAY)
    window.safe_zone = arcade.create_rectangle_filled(400, 485, 800, 90, arcade.color.AERO_BLUE)
    window.river1 = arcade.create_rectangle_filled(400, 572.5, 800, 85, arcade.color.BLUEBERRY)
    window.river2 = arcade.create_rectangle_filled(400, 657.5, 800, 85, arcade.color.BLUEBERRY)
    window.finish_zone = arcade.create_rectangle_filled(400, 750, 800, 100, arcade.color.AERO_BLUE)
    #
    window.lose = False
    #
    window.on_draw = types.MethodType(comp151_draw, window) #magic line to make comp151 draw work for arcade
    window.on_key_press = types.MethodType(handle_key_press, window)
    window.on_key_release = types.MethodType(handle_key_release, window)
    arcade.run()


def move_object_left(window):
    window.white_jaguar.center_x -= 5
    window.white_jaguar2.center_x -= 5
    window.blue_mercedes.center_x -= 5
    window.log.center_x -= 5
    window.log_dx = -5
    window.log2.center_x -= 5
    window.log2_dx = -5
    window.log3.center_x -= 5
    window.log3_dx = -5
    if window.white_jaguar.center_x <-36:
        window.white_jaguar.center_x = 836
    if window.white_jaguar2.center_x < -36:
        window.white_jaguar2.center_x = 836
    if window.blue_mercedes.center_x <-36:
        window.blue_mercedes.center_x = 836
    if window.log.center_x <-36:
        window.log.center_x = 836
    if window.log2.center_x <-36:
        window.log2.center_x = 836
        if window.log3.center_x < -36:
            window.log3.center_x = 836


def move_object_right(window):
    window.blue_bug.center_x += 5
    window.yellow_porsche.center_x += 5
    window.yellow_porsche2.center_x += 5
    window.turtle.center_x += 5
    window.turtle_dx = 5
    window.turtle2.center_x += 5
    window.turtle2_dx = 5
    window.turtle3.center_x += 5
    window.turtle3_dx = 5
    if window.blue_bug.center_x > 836:
        window.blue_bug.center_x = -36
    if window.yellow_porsche.center_x > 836:
        window.yellow_porsche.center_x = -36
    if window.yellow_porsche2.center_x > 836:
        window.yellow_porsche2.center_x = -36
    if window.turtle.center_x > 836:
        window.turtle.center_x = -36
    if window.turtle2.center_x > 836:
        window.turtle2.center_x = -36
    if window.turtle3.center_x > 836:
        window.turtle3.center_x = -36



def does_collide(sprite1, sprite2):
    return sprite1.collides_with_sprite(sprite2)


def comp151_draw(window):
    arcade.start_render()
    if not window.lose:
        update_frog_location(window)
        move_object_right(window)
        move_object_left(window)
        in_road(window)
        in_river(window)
        window.start_zone.draw()
        window.road1.draw()
        window.road2.draw()
        window.road3.draw()
        window.road4.draw()
        window.safe_zone.draw()
        window.river1.draw()
        window.river2.draw()
        window.finish_zone.draw()
        window.log.draw()
        window.log2.draw()
        window.log3.draw()
        window.turtle.draw()
        window.turtle2.draw()
        window.turtle3.draw()
        window.white_jaguar.draw()
        window.white_jaguar2.draw()
        window.blue_bug.draw()
        window.blue_mercedes.draw()
        window.yellow_porsche.draw()
        window.yellow_porsche2.draw()
        window.frog.draw()
        win_game(window)
    else:
        arcade.draw_text("GAME OVER", 200, 400, arcade.color.ANTI_FLASH_WHITE, font_size=40)
    arcade.finish_render()


#this function tells the game to end if the frog collides with any of the cars
def in_road(window):
    if does_collide(window.frog, window.white_jaguar):
        arcade.draw_text("aww man you got squished", 50, 750, arcade.color.ANTI_FLASH_WHITE, font_size=20)
        lose_game(window)
    if does_collide(window.frog, window.blue_bug):
        arcade.draw_text("aww man you got squished", 50, 750, arcade.color.ANTI_FLASH_WHITE, font_size=20)
        lose_game(window)
    if does_collide(window.frog, window.blue_mercedes):
        arcade.draw_text("aww man you got squished", 50, 750, arcade.color.ANTI_FLASH_WHITE, font_size=20)
        lose_game(window)
    if does_collide(window.frog, window.yellow_porsche):
        arcade.draw_text("aww man you got squished", 50, 750, arcade.color.ANTI_FLASH_WHITE, font_size=20)
        lose_game(window)


#this tells the game whether the frog landed on a turtle/log, and if he doesn't
# the game ends and displays accordingly
def in_river(window):
    if 500 < window.frog.center_y < 615:
        if does_collide(window.frog, window.turtle):
            window.frog.center_x = window.turtle.center_x
        if does_collide(window.frog, window.turtle2):
            window.frog.center_x = window.turtle2.center_x
        if does_collide(window.frog, window.turtle3):
            window.frog.center_x = window.turtle3.center_x
        else:
            arcade.draw_text("aww man this frog doesn't know how to swim", 400, 750, arcade.color.ANTI_FLASH_WHITE, font_size=20)
            lose_game(window)
    if 615 < window.frog.center_y < 700:
        if does_collide(window.frog, window.log):
            window.frog_dx = window.log_dx
        if does_collide(window.frog, window.log2):
            window.frog_dx = window.log2_dx
        if does_collide(window.frog, window.log3):
            window.frog_dx = window.log3_dx
        else:
            arcade.draw_text("aww man this frog doesn't know how to swim", 400, 750, arcade.color.ANTI_FLASH_WHITE, font_size=20)
            lose_game(window)


#this function only happens when the player reaches the end, shows the player they won
def win_game(window):
    if 700 < window.frog.center_y < 800:
        window.background_color = arcade.color.LIGHT_CORNFLOWER_BLUE
        arcade.draw_text("YOU WIN!", 400, 750, arcade.color.BLACK, font_size=40)


#this function shows when the player lost
def lose_game(window):
    window.background_color = arcade.color.BLACK
    arcade.draw_text("GAME OVER", 400, 400, arcade.color.ANTI_FLASH_WHITE, font_size=40)
    window.lose = True


#this makes the frog move
def update_frog_location(window):
    if window.frog_dx != 0:
        window.frog.center_x += window.frog_dx
    if window.frog_dy !=0:
        window.frog.center_y += window.frog_dy
    if window.frog.center_x <-36:
        window.frog.center_x = 836
    if window.frog.center_x > 836:
        window.frog.center_x = -36


# this makes the frog move when the keys are pressed
def handle_key_press(window, key, mod):
    jump_distance = 5
    if key == arcade.key.LEFT:
        window.frog_dx= -jump_distance
    elif key == arcade.key.RIGHT:
        window.frog_dx = jump_distance
    if key == arcade.key.UP:
        window.frog_dy = jump_distance
    elif key == arcade.key.DOWN:
        window.frog_dy = -jump_distance


#this makes the frog stop when the keys are released
def handle_key_release(window, key, mod):
    if key == arcade.key.LEFT or key == arcade.key.RIGHT:
        window.frog_dx =0
    if key == arcade.key.UP or key == arcade.key.DOWN:
        window.frog_dy =0

main()
