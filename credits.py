import pygame, sys, menu

def creditsWall(LanguageSelected):
    pygame.init()
    font_8bit = pygame.font.Font("fuentes/PressStart2P-Regular.ttf", 15)

    screen = pygame.display.set_mode((1000, 600))
    Running = True
    Language = LanguageSelected
    Last_Image_Time = pygame.time.get_ticks()

    Title = pygame.transform.scale(pygame.image.load("Title.png"), (500, 100))

    back_button_image = pygame.transform.scale(pygame.image.load("imagenes/atras+.png"), (100, 100))

    def draw_text(text, font, color, surface, x, y):
        text_obj = font.render(text, True, color)
        text_rect = text_obj.get_rect(center=(x, y))
        surface.blit(text_obj, text_rect)

    Velocidad = 5

    Curreent = pygame.time.get_ticks()
    Altura = 0

    while Running:

        StartCredits = pygame.time.get_ticks()
        Altura -= Velocidad

        screen.fill((135, 206, 235))
        if Language == "Spanish":
            screen.blit(pygame.transform.scale(pygame.image.load("imagenes/CREDITOS.png"), (1000, 1776)), (0, Altura))
        if Language == "English":
            screen.blit(pygame.transform.scale(pygame.image.load("imagenes/CREDITS.png"), (1000, 1776)), (0, Altura))

        if Altura == -1350:
            menu.Menu_Run(LanguageSelected=Language)

        back_button = pygame.Rect(25, 500, 100, 100)

        screen.blit(back_button_image, (25, 500))


    


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if back_button.collidepoint(event.pos):
                    menu.Menu_Run(LanguageSelected=Language)


        pygame.display.flip()