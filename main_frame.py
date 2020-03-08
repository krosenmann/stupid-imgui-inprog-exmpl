import pygame
import imgui
from imgui.integrations.pygame import PygameRenderer

s1 = True

def init():
    global show_about
    show_about = False
    pygame.init()
    size = 500, 400

    screen = pygame.display.set_mode(size, pygame.DOUBLEBUF
                                     | pygame.OPENGL
                                     )
    pygame.display.set_caption("Title restarts only on change main")

    imgui.create_context()
    impl = PygameRenderer()

    io = imgui.get_io()
    io.display_size = size
    return screen, impl
