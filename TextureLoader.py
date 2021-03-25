import pygame, os


def load_textures(*args):
    for path in args:
        for f, sf, files in os.walk(path):
            for file in files:
                name = file.split('.')[0]
                file_path = f + '\\' + file
                img = pygame.image.load(file_path)
                textures[name] = img


textures = {}
load_textures('textures')
print(textures)