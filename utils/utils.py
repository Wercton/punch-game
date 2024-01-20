import os
import pygame as pg

def get_image(path, size, colorkey = None):
    absolute_path = os.path.join('.', path)
    
    try:
        image = pg.image.load(absolute_path)
    except pg.error as message:
        print("Image not found: " + absolute_path)
        raise SystemExit(message)
    
    image = pg.transform.scale(image, size)
    image = image.convert()
    if colorkey == -1:
        colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    return image