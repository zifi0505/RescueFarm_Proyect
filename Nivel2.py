import pygame, sys, menu, random, Nivel3

pygame.quit()


def run_game(ScreenStatus, CharacterChoosen, LanguageSelected, SubLevel):
    # Inicializar Pygame
    pygame.init()

    # Configurar la pantalla
    screen = pygame.display.set_mode((1000, 600))
    pygame.display.set_caption("Colisión de Imágenes Aleatorias")

    # Cargar imágenes
    Mapa_Nivel = pygame.image.load("Mapa Nivel 2.png")
    Player_male = pygame.transform.scale(pygame.image.load("personajes/niñoParado (1).png"), (70, 70))
    Player_Female = pygame.transform.scale(pygame.image.load("personajes/niñaParada.png"), (70, 70))
    Oveja_image = pygame.image.load("imagenes/animales/Oveja.png")
    
    LetrasEscala_X = 32
    LetrasEscala_Y = 32

    CAFE = (139, 69, 19)

    RandomEnglishQuoteWin = random.choice(['WELL DONE!', 'YOU CAN!'])
    RandomSpanishQuoteWin = random.choice(['¡SIGUE ASI!', '¡BIEN HECHO!'])

    RandomSpanishQuoteLose = random.choice(['¡NO TE RINDAS!', '¡INTENTALO HASTA QUELO LOGRES!'])
    RandomEnglishQuoteLose = random.choice(['NOT GIVE UP!', 'TRY IT UNTIL YO2NE!'])
    


    Letra_H = pygame.transform.scale(pygame.image.load("Letras/Blancas/Hjuego.png"), (LetrasEscala_X, LetrasEscala_Y))
    Letra_O = pygame.transform.scale(pygame.image.load("Letras/Blancas/Ojuego.png"), (LetrasEscala_X, LetrasEscala_Y))
    Letra_V = pygame.transform.scale(pygame.image.load("Letras/Blancas/Vjuego.png"), (LetrasEscala_X, LetrasEscala_Y))
    Letra_J = pygame.transform.scale(pygame.image.load("Letras/Blancas/Jjuego.png"), (LetrasEscala_X, LetrasEscala_Y))
    Letra_R = pygame.transform.scale(pygame.image.load("Letras/Blancas/Hjuego.png"), (LetrasEscala_X, LetrasEscala_Y))
    Letra_S = pygame.transform.scale(pygame.image.load("Letras/Blancas/Sjuego.png"), (LetrasEscala_X, LetrasEscala_Y))
    Letra_T = pygame.transform.scale(pygame.image.load("Letras/Blancas/Tjuego.png"), (LetrasEscala_X, LetrasEscala_Y))
    Letra_I = pygame.transform.scale(pygame.image.load("Letras/Blancas/Ijuego.png"), (LetrasEscala_X, LetrasEscala_Y))
    Letra_A = pygame.transform.scale(pygame.image.load("Letras/Blancas/Ajuego.png"), (LetrasEscala_X, LetrasEscala_Y))
    Letra_E= pygame.transform.scale(pygame.image.load("Letras/Blancas/Ejuego.png"), (LetrasEscala_X, LetrasEscala_Y))
    Letra_C = pygame.transform.scale(pygame.image.load("Letras/Blancas/Cjuego.png"), (LetrasEscala_X, LetrasEscala_Y))
    Letra_D = pygame.transform.scale(pygame.image.load("Letras/Blancas/Djuego.png"), (LetrasEscala_X, LetrasEscala_Y))
    Letra_R = pygame.transform.scale(pygame.image.load("Letras/Blancas/Rjuego.png"), (LetrasEscala_X, LetrasEscala_Y))
    Letra_W = pygame.transform.scale(pygame.image.load("Letras/Blancas/Wjuego.png"), (LetrasEscala_X, LetrasEscala_Y))
    Letra_P = pygame.transform.scale(pygame.image.load("Letras/Blancas/Pjuego.png"), (LetrasEscala_X, LetrasEscala_Y))
    Letra_G = pygame.transform.scale(pygame.image.load("Letras/Blancas/Gjuego.png"), (LetrasEscala_X, LetrasEscala_Y))

    AInt = 0
    BInt = 0
    CInt = 0
    DInt = 0
    EInt = 0
    GInt = 0
    HInt = 0
    IInt = 0
    JInt = 0
    KInt = 0
    LInt = 0
    MInt = 0
    NInt = 0
    OInt = 0
    PInt = 0
    SInt = 0
    VInt = 0
    RInt = 0
    WInt = 0

    

    farmer_image = pygame.transform.scale(pygame.image.load("personajes/granjero.png"),(80,80))
    win_image = pygame.image.load("imagenes/Ganar 8.png")  # Cargar la imagen de ganar
    Heart_Image = pygame.transform.scale(pygame.image.load("imagenes/CorazonDeVida.png"), (40, 40))


    # Posición inicial del jugador
    player_pos = [400, 520]

    # Lista para almacenar las ovejas
    targets = []
    PauseValue = False

    # Función para comprobar colisión
    def check_collision(pos1, size1, pos2, size2):
        return (pos1[0] < pos2[0] + size2[0] and
                pos1[0] + size1[0] > pos2[0] and
                pos1[1] < pos2[1] + size2[1] and
                pos1[1] + size1[1] > pos2[1])

    # Crea una fuente
    font = pygame.font.Font('fuentes/PressStart2P-Regular.ttf', 15)


    # Bucle principal
    Character = CharacterChoosen
    StatusScreen = ScreenStatus
    Status = ""
    Language = LanguageSelected
    score = 0
    Timecounter = 40  # Tiempo inicial
    running = True
    farmer_pos = [280, 100] # Posición inicial del granjero
    farmer_direction = 1  # 1 para mover a la derecha, -1 para mover a la izquierda
    farmer_speed = 2  # Velocidad de movimiento del granjero

    # Límites de movimiento del granjero
    farmer_left_limit = 280  # Límite izquierdo
    farmer_right_limit = 670  # Límite derecho

    # Vida
    Life = 3

    # Velocidad de caida de las letras
    if Language == "English":
        VelocidadDeCaida = 5
    else:
        VelocidadDeCaida = 10


    # Tiempo de la última caída
    Last_Letter_Time = pygame.time.get_ticks()

    # Guardar el tiempo inicial
    # Captura el tiempo de inicio

    font_8bit = pygame.font.Font("fuentes/PressStart2P-Regular.ttf", 17)

    def draw_text(text, font, color, surface, x, y):
        text_obj = font.render(text, True, color)
        text_rect = text_obj.get_rect(center=(x, y))
        surface.blit(text_obj, text_rect)


    back_button = pygame.Rect(25, 500, 100, 100)
    back_button_image = pygame.transform.scale(pygame.image.load("imagenes/atras+.png"), (100, 100))
    if Language == "English":
        Time = 20
    else:
        Time = 20
    pause_start_time = 0
    paused_time = 0
    start_ticks = pygame.time.get_ticks() #tiempo al inicio


    while running:
    
        if StatusScreen == "Characters":
            screen.blit(pygame.transform.scale(pygame.image.load("imagenes/fondmenu.png"), (1000, 600)), (0, 0))

            FemaleCharacterButton = pygame.Rect(630, 270, 100, 100)

            screen.blit(pygame.transform.scale(pygame.image.load("imagenes/seleccionC.png"), (833, 500)), (83, 0))

     
            mouse_pos = pygame.mouse.get_pos()

            MaleCharacterButton = pygame.Rect(270, 240, 130, 130)


            screen.blit(pygame.transform.scale(pygame.image.load("personajes/niñaParada.png"), (100, 100)), (620, 255))
            screen.blit(pygame.transform.scale(pygame.image.load("personajes/niñoParado (1).png"), (100, 100)), (280, 255))
            screen.blit(back_button_image, (25, 500))

            if Language == "English":
                draw_text('SELECT YOUT CHARACTER', font_8bit, (255, 255, 255), screen, 500 , 165)
            else:
                draw_text('SELECCIONA TU CARACTER', font_8bit, (255, 255, 255), screen, 500, 165)
            


            for event in pygame.event.get():
            
                if event.type == pygame.QUIT:

                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if FemaleCharacterButton.collidepoint(event.pos):
                        Character = "Female"
                        StatusScreen = "Game"
                        print("Character has been choosen", Character)
                        start_ticks = pygame.time.get_ticks()
                    if MaleCharacterButton.collidepoint(event.pos):
                        Character = "Male"
                        StatusScreen = "Game"
                        print("Character has been choosen", Character)
                        start_ticks = pygame.time.get_ticks()
                    if back_button.collidepoint(event.pos):
                        menu.Menu_Run(LanguageSelected=Language)



        if StatusScreen == "Game":
            # Mover el jugador con las teclas de flecha

            if PauseValue == False and not Status == "Winner" and not Status == "Lose":
                keys = pygame.key.get_pressed()
                if keys[pygame.K_LEFT] and player_pos[0] > 280:
                    player_pos[0] -= 5
                    if Character == "Female":
                        Player_Female = pygame.transform.scale(pygame.image.load("personajes/niñaCorriendoI.png"), (70, 70))
                    elif Character == "Male":
                        Player_male = pygame.transform.scale(pygame.image.load("personajes/niñoCorriendoI.png"), (70, 70))
                elif keys[pygame.K_RIGHT] and player_pos[0] < 670:
                    player_pos[0] += 5
                    if Character == "Female":
                        Player_Female = pygame.transform.scale(pygame.image.load("personajes/niñaCorriendoD.png"), (70, 70))
                    elif Character == "Male":
                        Player_male = pygame.transform.scale(pygame.image.load("personajes/niñoCorriendoD.png"), (70, 70))
                
                else:
                    if Character == "Female":
                        Player_Female = pygame.transform.scale(pygame.image.load("personajes/niñaParada.png"), (70, 70))
                    if Character == "Male":
                        Player_male = pygame.transform.scale(pygame.image.load("personajes/niñoParado (1).png"), (70, 70))
                    


                if keys[pygame.K_UP]:
                    player_pos[1] = 535  # Resetear la posición vertical del jugador




            # Movimiento del granjero
            if PauseValue == False and not Status == "Winner" and not Status == "Lose":
                farmer_pos[0] += farmer_direction * farmer_speed



            # Cambiar dirección al llegar a los límites
            if farmer_pos[0] >= farmer_right_limit or farmer_pos[0] <= farmer_left_limit:
                farmer_direction *= -1  # Cambiar dirección

            # Comprobar colisiones
            player_size = Player_male.get_size()
            Letra_A_Size = Letra_A.get_size()

            

            # Verificar colisión entre jugador y ovejas
            for target in targets[:]:  # [:] para hacer una copia de la lista mientras iteramos
                if check_collision(player_pos, player_size, target[:2], Letra_A_Size):
                    score += 1
                    if SubLevel == "SubLevel1":
                        if Language == "Spanish":
                            if randomLetters == 1 and AInt < 2:
                                AInt += 1
                            elif randomLetters == 2 and VInt < 1:
                                VInt += 1
                            elif randomLetters == 3 and CInt < 2:
                                CInt += 1
                            else:
                                Life -= 1
                        if Language == "English":
                            if randomLetters == 1 and CInt < 1:
                                CInt += 1
                            elif randomLetters == 2 and OInt < 1:
                                OInt += 1
                            elif randomLetters == 3 and WInt < 1:
                                WInt += 1
                            else:
                                Life -= 1
                    if SubLevel == "SubLevel2":
                        if Language == "Spanish":
                            if randomLetters == 4 and DInt < 1:
                                DInt += 1
                            elif randomLetters == 5 and RInt < 1:
                                RInt += 1
                            elif randomLetters == 6 and EInt < 1:
                                EInt += 1
                            elif randomLetters == 7 and CInt < 1:
                                CInt += 1
                            elif randomLetters == 8 and OInt < 1:
                                OInt += 1
                            else:
                                Life -= 1
                        if Language == "English":
                            if randomLetters == 4 and PInt < 1:
                                PInt += 1
                            elif randomLetters == 5 and IInt < 1:
                                IInt += 1
                            elif randomLetters == 6 and GInt < 1:
                                GInt += 1
                            else:
                                Life -= 1
                                
                        
                    
                    targets.remove(target) # Eliminar letra después de la colisión

            
            
            # Movel las letras hacia abajo
            if PauseValue == False and not Status == "Winner" and not Status == "Lose":
                for target in targets:
                    target[1] += VelocidadDeCaida #Velocidad

            # Caída de ovejas (generación de nuevas ovejas cada 2 segundos)
            if PauseValue == False and not Status == "Winner" and not Status == "Lose":
                current_time = pygame.time.get_ticks()
                if current_time - Last_Letter_Time > 2000:  # Cada 2 segundos
                    x = farmer_pos[0] + farmer_image.get_width() // 2  # Posición del granjero
                    targets.append([x, farmer_pos[1], True])  # Crear nueva oveja en la posición del granjero
                    Last_Letter_Time = current_time  # Reiniciar el temporizado
                    if SubLevel == "SubLevel1":
                        randomLetters = random.choice([1, 2, 3])
                    if SubLevel == "SubLevel2":
                        if Language == "Spanish":
                            randomLetters = random.choice([4, 5, 6, 7, 8])
                        if Language == "English":
                            randomLetters = random.choice([4, 5, 6])


            # Actualizar el tiempo
            if PauseValue == False and Status != "Winner" or Status != "Lose" and ScreenStatus == "Game":
                seconds = (pygame.time.get_ticks() - start_ticks) / 1000  # Tiempo en segundos
                Timecounter = Time  # Calcular el tiempo restante
                Timecounter -= seconds

            # Comprobar condiciones de finalización
            

            # Dibujar todo
            screen.fill((0, 0, 0))  # Limpiar la pantalla
            screen.blit(Mapa_Nivel, [0, 0])
            if Character == "Male":
                screen.blit(Player_male, player_pos)
            if Character == "Female":
                screen.blit(Player_Female, player_pos)
            
            screen.blit(farmer_image, farmer_pos)  # Dibujar el granjero

            
            if Life >= 3:
                screen.blit(Heart_Image, (112, 50))
            if Life >= 2:
                screen.blit(Heart_Image, (174, 50))
            if Life >= 1:
                screen.blit(Heart_Image, (236, 50))

            
            
            # Dibujar Letras

            for Letra_target in targets:
                if SubLevel == "SubLevel1":
                    if Language == "Spanish":
                        if randomLetters == 1:
                            screen.blit(Letra_A, Letra_target[:2])
                        if randomLetters == 2:
                            screen.blit(Letra_V, Letra_target[:2])
                        if randomLetters == 3:
                            screen.blit(Letra_C, Letra_target[:2])
                    if Language == "English":
                        if randomLetters == 1:
                            screen.blit(Letra_C, Letra_target[:2])
                        if randomLetters == 2:
                            screen.blit(Letra_O, Letra_target[:2])
                        if randomLetters == 3:
                            screen.blit(Letra_W, Letra_target[:2])
                if SubLevel == "SubLevel2":
                    if Language == "English":
                        if randomLetters == 4:
                            screen.blit(Letra_P, Letra_target[:2])
                        if randomLetters == 5:
                            screen.blit(Letra_I, Letra_target[:2])
                        if randomLetters == 6:
                            screen.blit(Letra_G, Letra_target[:2])
                    if Language == "Spanish":
                        if randomLetters == 4:
                            screen.blit(Letra_D, Letra_target[:2])
                        if randomLetters == 5:
                            screen.blit(Letra_R, Letra_target[:2])
                        if randomLetters == 6:
                            screen.blit(Letra_E, Letra_target[:2])
                        if randomLetters == 7:
                            screen.blit(Letra_C, Letra_target[:2])
                        if randomLetters == 8:
                            screen.blit(Letra_O, Letra_target[:2])

            if SubLevel == "SubLevel1":
                if Language == "Spanish":
                    if VInt >= 1:
                        screen.blit(pygame.transform.scale(pygame.image.load("Letras/Amarillas/Vama.png"), (LetrasEscala_X, LetrasEscala_Y)),  (452, 10))
                    else:
                        screen.blit(pygame.transform.scale(pygame.image.load("Letras/Grises/V.png"), (LetrasEscala_X, LetrasEscala_Y)),  (452, 10))
                    if CInt >= 1:
                        screen.blit(pygame.transform.scale(pygame.image.load("Letras/Amarillas/Cama.png"), (LetrasEscala_X, LetrasEscala_Y)),  (516 , 10))
                    else:
                        screen.blit(pygame.transform.scale(pygame.image.load("Letras/Grises/C.png"), (LetrasEscala_X, LetrasEscala_Y)), (516 , 10))
                    if AInt >= 1:
                        screen.blit(pygame.transform.scale(pygame.image.load("Letras/Amarillas/Aama.png"), (LetrasEscala_X, LetrasEscala_Y)), (484, 10))
                    else:
                        screen.blit(pygame.transform.scale(pygame.image.load("Letras/Grises/A.png"), (LetrasEscala_X, LetrasEscala_Y)), (484, 10))
                    if AInt >= 2:
                        screen.blit(pygame.transform.scale(pygame.image.load("Letras/Amarillas/Aama.png"), (LetrasEscala_X, LetrasEscala_Y)), (548, 10))
                    else:
                        screen.blit(pygame.transform.scale(pygame.image.load("Letras/Grises/A.png"), (LetrasEscala_X, LetrasEscala_Y)), (548, 10))
                if Language == "English":
                    if CInt >= 1:
                        screen.blit(pygame.transform.scale(pygame.image.load("Letras/Amarillas/Cama.png"), (LetrasEscala_X, LetrasEscala_Y)),  (460 , 20))
                    else:
                        screen.blit(pygame.transform.scale(pygame.image.load("Letras/Grises/C.png"), (LetrasEscala_X, LetrasEscala_Y)),  (460 , 20))
                    if OInt >= 1:
                        screen.blit(pygame.transform.scale(pygame.image.load("Letras/Amarillas/Oama.png"), (LetrasEscala_X, LetrasEscala_Y)),  (492  , 20))
                    else:
                        screen.blit(pygame.transform.scale(pygame.image.load("Letras/Grises/O.png"), (LetrasEscala_X, LetrasEscala_Y)), (492  , 20))
                    if WInt >= 1:
                        screen.blit(pygame.transform.scale(pygame.image.load("Letras/Amarillas/Wama.png"), (LetrasEscala_X, LetrasEscala_Y)), (524 , 20))
                    else:
                        screen.blit(pygame.transform.scale(pygame.image.load("Letras/Grises/W.png"), (LetrasEscala_X, LetrasEscala_Y)), (524 , 20))


            if SubLevel == "SubLevel2":
                if Language == "Spanish":
                    if CInt >= 1:
                        screen.blit(pygame.transform.scale(pygame.image.load("Letras/Amarillas/Cama.png"), (LetrasEscala_X, LetrasEscala_Y)),  (452, 10))
                    else:
                        screen.blit(pygame.transform.scale(pygame.image.load("Letras/Grises/C.png"), (LetrasEscala_X, LetrasEscala_Y)),  (452, 10))
                    if EInt >= 1:
                        screen.blit(pygame.transform.scale(pygame.image.load("Letras/Amarillas/Eama.png"), (LetrasEscala_X, LetrasEscala_Y)),  (484 , 10))
                    else:
                        screen.blit(pygame.transform.scale(pygame.image.load("Letras/Grises/E.png"), (LetrasEscala_X, LetrasEscala_Y)), (484 , 10))
                    if RInt >= 1:
                        screen.blit(pygame.transform.scale(pygame.image.load("Letras/Amarillas/Rama.png"), (LetrasEscala_X, LetrasEscala_Y)), (516, 10))
                    else:
                        screen.blit(pygame.transform.scale(pygame.image.load("Letras/Grises/R.png"), (LetrasEscala_X, LetrasEscala_Y)), (516, 10))
                    if DInt >= 1:
                        screen.blit(pygame.transform.scale(pygame.image.load("Letras/Amarillas/Dama.png"), (LetrasEscala_X, LetrasEscala_Y)), (548, 10))
                    else:
                        screen.blit(pygame.transform.scale(pygame.image.load("Letras/Grises/D.png"), (LetrasEscala_X, LetrasEscala_Y)), (548, 10))
                    if OInt >= 1:
                        screen.blit(pygame.transform.scale(pygame.image.load("Letras/Amarillas/Oama.png"), (LetrasEscala_X, LetrasEscala_Y)), (580, 10))
                    else:
                        screen.blit(pygame.transform.scale(pygame.image.load("Letras/Grises/O.png"), (LetrasEscala_X, LetrasEscala_Y)), (580, 10))
                if Language == "English":
                    if PInt >= 1:
                        screen.blit(pygame.transform.scale(pygame.image.load("Letras/Amarillas/Pama.png"), (LetrasEscala_X, LetrasEscala_Y)),  (460 , 20))
                    else:
                        screen.blit(pygame.transform.scale(pygame.image.load("Letras/Grises/P.png"), (LetrasEscala_X, LetrasEscala_Y)),  (460 , 20))
                    if IInt >= 1:
                        screen.blit(pygame.transform.scale(pygame.image.load("Letras/Amarillas/Iama.png"), (LetrasEscala_X, LetrasEscala_Y)),  (492  , 20))
                    else:
                        screen.blit(pygame.transform.scale(pygame.image.load("Letras/Grises/I.png"), (LetrasEscala_X, LetrasEscala_Y)), (492  , 20))
                    if GInt >= 1:
                        screen.blit(pygame.transform.scale(pygame.image.load("Letras/Amarillas/Gama.png"), (LetrasEscala_X, LetrasEscala_Y)), (524 , 20))
                    else:
                        screen.blit(pygame.transform.scale(pygame.image.load("Letras/Grises/G.png"), (LetrasEscala_X, LetrasEscala_Y)), (524 , 20))
            

            # Mostrar puntaje y tiempo
    
            #score_surface = font.render(f'A: {AInt:}, V: {VInt}, J: {JInt}, O: {OInt}, E: {EInt}', True, (255, 255, 255))
            time_surface = font.render(f'Time: 0:{int(Timecounter)}', True, (255, 255, 255))
            #screen.blit(score_surface, (100, 30))  # Ajustar posición de puntaje
            screen.blit(time_surface, (850, 20))   # Ajustar posición de tiempo

            if Timecounter <= 0 or Life == 0:
                Status = "Lose"
            if SubLevel == "SubLevel1":
                if Language == "Spanish":
                    if VInt >= 1 and AInt >= 2 and CInt >= 1:
                        Status = "Winner"
                if Language == "English":
                    if CInt >= 1 and OInt >= 1 and WInt >= 1:
                        Status = "Winner"
            if SubLevel == "SubLevel2":
                if Language == "Spanish":
                    if CInt >= 1 and EInt >= 1 and RInt >= 1 and DInt >= 1 and OInt >= 1:
                        Status = "Winner"
                if Language == "English":
                    if PInt >= 1 and IInt >= 1 and GInt >= 1:
                            Status = "Winner"
            

            if PauseValue == True:
                Time_PauseTicks = (pygame.time.get_ticks() - start_ticks) / 1000

            if SubLevel == "SubLevel1":
                if Language == "Spanish":
                    if PInt >= 1 and OInt >= 2 and LInt >= 2:
                        Status = "Winner"
                if Language == "English":
                    if CInt >= 2 and IInt >= 1 and HInt >= 1 and KInt >= 1 and EInt >= 1 and NInt >= 1:
                        Status = "Winner"
            if SubLevel == "SubLevel2":
                if Language == "Spanish":
                    if CInt >= 1 and AInt >= 2 and BInt >= 1 and LInt >= 2 and OInt >= 1:
                        Status = "Winner"
            

            if PauseValue == True:
                Time_PauseTicks = (pygame.time.get_ticks() - start_ticks) / 1000
            if PauseValue == False and not Status == "Winner" or not Status == "Lose":
                Pause_Button = pygame.Rect(30, 30, 70, 70)
                screen.blit(pygame.transform.scale(pygame.image.load("imagenes/Pause button.png"), (70, 70)), (30, 30))
            
            

            if Language == "Spanish":
                screen.blit(pygame.image.load("imagenes/INSTRUCCIONES.png"), (850 ,80 ))

            if Language == "English":
                screen.blit(pygame.image.load("imagenes/INSTRUCCIONESINGLES.png"), (850 , 80 ))


            if Status == "Winner" or Status == "Lose" or PauseValue == True:
                    if Status == "Winner":
                        RepeatLevel = pygame.Rect(20, 440, 220, 80)
                        BackMenu = pygame.Rect(390, 40, 220, 80)
                        NextLevel = pygame.Rect(750, 440, 220, 80)
                        if Language == "English":
                            screen.blit(pygame.image.load("imagenes/nextlevel.png"), (0 ,0))
                            draw_text(RandomEnglishQuoteWin, font_8bit, (255, 255, 255), screen, 490  , 460 )
                        else:
                            screen.blit(pygame.image.load("imagenes/signivel.png"), (0 ,0))
                            draw_text(RandomSpanishQuoteWin, font_8bit, (255, 255, 255), screen, 490  , 460)
                    if Status == "Lose":
                        RepeatLevel = pygame.Rect(40, 480, 220, 80)
                        if Language == "English":
                            screen.blit(pygame.image.load("imagenes/perderESP.png"), (0 ,0))
                            draw_text(RandomEnglishQuoteLose, font_8bit, (255, 255, 255), screen, 490  , 460)
                        else:
                            screen.blit(pygame.image.load("imagenes/tryagain.png"), (0 ,0))
                            draw_text(RandomSpanishQuoteLose, font_8bit, (255, 255, 255), screen, 490  , 460)           

                        BackMenu = pygame.Rect(740, 480, 220, 80)
                    if PauseValue == True:
                        ResumeButton = pygame.Rect(370, 390, 300, 60)
                        screen.blit(pygame.transform.scale(pygame.image.load("imagenes/PausaYperder.png"), (666, 400)), (190, 200))
                        if Language == "Spanish":
                            screen.blit(pygame.image.load("imagenes/PAUSA.png"), (0, 0))
                            screen.blit(pygame.transform.scale(pygame.image.load("imagenes/PausaYperder.png"), (666, 400)), (190, 200))
                            draw_text('RENUDAR', font_8bit, (255, 255, 255), screen, 520, 410)
                            draw_text('MENU', font_8bit, (255, 255, 255), screen, 520, 500)
                        if Language == "English":
                            screen.blit(pygame.image.load("imagenes/PAUSE.png"), (0, 0))
                            screen.blit(pygame.transform.scale(pygame.image.load("imagenes/PausaYperder.png"), (666, 400)), (190, 200))
                            draw_text('RESUME', font_8bit, (255, 255, 255), screen, 520, 410)
                            draw_text('MENU', font_8bit, (255, 255, 255), screen, 520, 500)

                        BackMenu = pygame.Rect(360, 470, 320, 60)
                    
                    

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if Status == "Winner" or Status == "Lose" or PauseValue == True:
                         if BackMenu.collidepoint(event.pos):
                                menu.Menu_Run(LanguageSelected=Language)
                         if PauseValue == True:
                            if ResumeButton.collidepoint(event.pos):
                                    PauseValue = False
                         if Status == "Winner" or Status == "Lose":
                            if RepeatLevel.collidepoint(event.pos):
                                run_game(ScreenStatus="Game", CharacterChoosen=Character, LanguageSelected=Language, SubLevel="SubLevel1")
                            
                            if NextLevel.collidepoint(event.pos):
                                if SubLevel == "SubLevel1":
                                    run_game(ScreenStatus="Game", CharacterChoosen=Character, LanguageSelected=Language, SubLevel="SubLevel2")
                                if SubLevel == "SubLevel2":
                                    Nivel3.run_game(ScreenStatus="Game", CharacterChoosen="Male", LanguageSelected=Language, SubLevel="SubLevel1")
                    if Pause_Button.collidepoint(event.pos):
                            PauseValue = True



        # Mostrar imagen de resultado            
        pygame.display.flip()