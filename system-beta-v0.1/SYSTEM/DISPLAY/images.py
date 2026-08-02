from SYSTEM.DISPLAY import display
def draw_image(image, pos_x=0, pos_y=0):
    import os
    display.tela.draw_image(f"/sd/image/{image}.raw", pos_x, pos_y)