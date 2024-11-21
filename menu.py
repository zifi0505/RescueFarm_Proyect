import pygame, sys, Nivel1, credits, Nivel2, Nivel3
# Inicializar Pygame

# Tamaño de pantalla
def Menu_Run(LanguageSelected):
    pygame.init()
    screen_width, screen_height = 1000, 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("RESCUE FARM")

    # Colores
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    CAFE = (139, 69, 19)
    HIGHLIGHT_VERDE = (0, 255, 0)#Color para resaltar en verde
    HIGHLIGHT_AMARILLO =(255, 255,  0)#Color para resaltar en  amarillo


    # Fuente estilo 8 bits (debes descargar la fuente y colocarla en la misma carpeta)
    font_8bit = pygame.font.Font("fuentes/PressStart2P-Regular.ttf", 30)

    #icono
    icono = pygame.image.load("imagenes/icono.jpeg")
    pygame.display.set_icon(icono)

    # Cargar la imagen del fondo
    background_image = pygame.image.load("imagenes/fondmenu.png")
    background_image = pygame.transform.scale(background_image, (screen_width, screen_height))
    Title = pygame.transform.scale(pygame.image.load("Title.png"), (500, 100))

    # Movimiento del fondo
    bg_x1 = 0  # posición inicial del primer fondo
    bg_x2 = screen_width  # posición inicial del segundo fondo

    # Velocidad del fondo
    bg_speed = 2

    # Cargar la imagen del botón "Regresar."
    back_button_image = pygame.image.load("imagenes/atras+.png")
    back_button_image = pygame.transform.scale(back_button_image, (100, 100))  # Ajustar según necesites

    # SONIDO DEL MENU

    button_click_sound = pygame.mixer.Sound("MUSICA/botonPress.mp3")


    # Estados del juego
    MENU = "menu"
    Credits = "credits"
    LEVEL = "level"
    Language = LanguageSelected
    state = MENU

    # Botones
    button_width, button_height = 300, 50


    # Función para dibujar texto centrado
    def draw_text(text, font, color, surface, x, y):
        text_obj = font.render(text, True, color)
        text_rect = text_obj.get_rect(center=(x, y))
        surface.blit(text_obj, text_rect)

    # Bucle principal del juego
    running = True
    difficulty = None
    Songplaying = True

    pygame.mixer.music.load("MUSICA/InicioJuego.mp3")
    pygame.mixer.music.play(-1)

    
    while running:
        
        # Dibujar el fondo en movimiento
        screen.blit(background_image, (bg_x1, 0))
        screen.blit(background_image, (bg_x2, 0))

    # Actualizar la posición del fondo
        bg_x1 -= bg_speed
        bg_x2 -= bg_speed

        # Reiniciar la posición del fondo cuando salga de la pantalla
        if bg_x1 <= -screen_width:
            bg_x1 = screen_width
        if bg_x2 <= -screen_width:
            bg_x2 = screen_width

        mouse_pos = pygame.mouse.get_pos()     
        screen.blit(pygame.transform.scale(pygame.image.load("imagenes/cartelon.png"), (636, 381)), (180, 218))             

        if state == MENU:
            # Dibujar el título del menú

            screen.blit(Title, (250, 100))

            
            # Dibujar el botón "Jugar"
            play_button = pygame.Rect(360, 310, 310, 60)


            LanguageButton = pygame.Rect(310, 390, 310, 60)


            credits_button = pygame.Rect(340, 470, 310, 60)
            
            SongButton = pygame.Rect(80, 460, 120, 60)
            #iluminacion de boton jugar    
                    
            if Songplaying == True:
                screen.blit(pygame.transform.scale(pygame.image.load("imagenes/volume+corregido.png"), (200, 200)), (40, 380))
            else:
                screen.blit(pygame.transform.scale(pygame.image.load("imagenes/volumeNTcorregido.png"), (200, 200)), (40, 380))

            if Language == "Spanish":
                draw_text('JUGAR', font_8bit, WHITE, screen, 500, 340)
                draw_text('ESPAÑOL', font_8bit, WHITE, screen, 455, 420)
                draw_text('CREDITOS', font_8bit, WHITE, screen, 490, 500)
            else:
                draw_text('PLAY', font_8bit, WHITE, screen, 500, 340)
                draw_text('ENGLISH', font_8bit, WHITE, screen, 455, 420)
                draw_text('CREDITS', font_8bit, WHITE, screen, 490, 500) 

            # Detección de clic en el botón
        
            for event in pygame.event.get():
            
                if event.type == pygame.QUIT:
                    pygame.quit()   
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if play_button.collidepoint(event.pos):
                        button_click_sound.play() #reproduce el sonido de click del boton jugar
                        state = LEVEL

                    if SongButton.collidepoint(event.pos):
                        if Songplaying == True:
                            Songplaying = False
                            pygame.mixer.music.stop()
                        else:
                            Songplaying = True
                            pygame.mixer.music.play(-1)
                    if LanguageButton.collidepoint(event.pos):
                        button_click_sound.play()
                        if Language == "Spanish":
                            Language = "English"
                        else:
                            Language = "Spanish"
                    if credits_button.collidepoint(mouse_pos):
                        credits.creditsWall(LanguageSelected=Language)
        



            # Detectar clic de dificultad
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if back_button.collidepoint(event.pos):
                        button_click_sound.play()
                        state = MENU  # Regresar al menú principal

        elif state == LEVEL:
            # Mostrar selección de nivele
            if Language == "Spanish":
                draw_text('SELECCIONA UN NIVEL', font_8bit, BLACK, screen, screen_width // 2, 100)
            else:
                draw_text('SELECT A LEVEL', font_8bit, BLACK, screen, screen_width // 2, 100)

            level1_button = pygame.Rect(360, 310, 310, 60)
            level2_button = pygame.Rect(310, 390, 310, 60)
            level3_button = pygame.Rect(340, 470, 310, 60)
            back_button = pygame.Rect(25, 500, button_width, button_height)

 
        
            
            
            # Dibujar la imagen del botón "Regresar"
            screen.blit(back_button_image, (50, 500))
            if Language == "Spanish":
                draw_text('NIVEL 1', font_8bit, WHITE, screen, 500, 340)
                draw_text('NIVEL 2', font_8bit, WHITE, screen, 455, 420)
                draw_text('NIVEL 3', font_8bit, WHITE, screen, 490, 500)
            else:
                draw_text('LEVEL 1', font_8bit, WHITE, screen, 500, 340)
                draw_text('LEVEL 2', font_8bit, WHITE, screen, 455, 420)
                draw_text('LEVEL 3', font_8bit, WHITE, screen, 490, 500)



            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if level1_button.collidepoint(event.pos):
                        button_click_sound.play()
                        print(f"Nivel 1 seleccionado en dificultad {difficulty}")
                        Nivel1.run_game(ScreenStatus="History", CharacterChoosen="Male", LanguageSelected=Language)
                    elif level2_button.collidepoint(event.pos):
                        button_click_sound.play()
                        print(f"Nivel 2 seleccionado en dificultad {difficulty}")
                        Nivel2.run_game(ScreenStatus="Characters", CharacterChoosen="Male", LanguageSelected=Language, SubLevel="SubLevel1") 
                    elif level3_button.collidepoint(event.pos):
                        button_click_sound.play()
                        print(f"Nivel 3 seleccionado en dificultad {difficulty}")
                        Nivel3.run_game(ScreenStatus="Characters", CharacterChoosen="Male", LanguageSelected=Language, SubLevel="SubLevel1")
                    elif back_button.collidepoint(event.pos):
                        button_click_sound.play()
                    if state == LEVEL:
                        state = MENU  # Regresar a la selección de dificultad
                
        pygame.display.flip()
        pygame.time.Clock().tick(60)

Menu_Run(LanguageSelected="Spanish")