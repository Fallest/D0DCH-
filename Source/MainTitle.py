import pygame, Config

import CreditScreen

def redraw():
    """
    Redibuja los componentes de la pantalla.
    :return: None
    """
    # Añade el bg con una capa de transparencia encima para oscurecerlo
    Config.screen.fill(Config.black)

    Config.screen.blit(Config.bgMainTitle, (0, 0))

    # Escribimos el título
    Config.screen.blit(Config.titleFontSurface, (Config.width // 20, Config.height // 20))

    # Dibujamos el botón para los créditos

    # Escribimos los controles
    Config.drawControls()

    # Dibujamos los botones:
    Config.drawButtons()

    # Al inicio está seleccionado "Créditos"
    Config.drawSelectedButton(5)

def run():
    """
    Pantalla principal.
    En ella se escoge la dificultad del juego (predefinido "Normal").

    Los niveles de dificultad son 1, 2, 3 (fácil, normal, y difícil, respectivamente).
    Si se presiona 5 veces para aumentar la dificultad se selecciona BulletHell (4).

    Si se selecciona "Salir", devuelve 0.
    Si se selecciona "Jugar", devuelve 1.
    """
    print("Iniciando MainTitle.run()...")
    # Ponemos la música de fondo
    pygame.mixer.music.unload()
    pygame.mixer.music.load(Config.ost)
    if Config.audio:
        pygame.mixer.music.play()

    # Añade el bg con una capa de transparencia encima para oscurecerlo
    Config.screen.fill(Config.black)

    Config.screen.blit(Config.bgMainTitle, (0, 0))

    # Escribimos el título
    Config.screen.blit(Config.titleFontSurface, (Config.width // 20, Config.height // 20))

    # Selección en la pantalla:
    # 1 - Jugar, 2 - Dificultades, 3 - audio, 4 - Salir
    selection = 1

    # Dibujamos el botón para los créditos

    # Escribimos los controles
    Config.drawControls()

    # Dibujamos los botones:
    Config.drawButtons(credits=True)

    # Al inicio está seleccionado "Jugar"
    Config.drawSelectedButton(selection)

    while Config.running:
        # Control de eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Config.running = False
                break

            # Si se presiona una tecla, comprobar cuál es
            if event.type == pygame.KEYDOWN:
                """
                Si se presiona la flecha arriba, se sube (baja) de selección
                """
                if event.key == pygame.K_UP:
                    if selection > 1:
                        Config.drawUnselectedButton(selection)
                        selection -= 1
                        Config.drawSelectedButton(selection)

                """
                Si se presiona la flecha abajo, se baja (sube) de selección
                """
                if event.key == pygame.K_DOWN:
                    if selection < 4:
                        Config.drawUnselectedButton(selection)
                        selection += 1
                        Config.drawSelectedButton(selection)
                """
                Si se presiona <- y se está seleccionando la dificultad, se baja de dificultad
                Si se está seleccionando "Salir", se selecciona "Créditos".
                """
                if event.key == pygame.K_LEFT:
                    if selection == 2:
                        Config.decreaseDif()
                        Config.drawSelectedButton(selection)
                    elif selection == 4:
                        Config.drawUnselectedButton(selection)
                        selection = 5
                        Config.drawSelectedButton(selection)
                """
                Si se presiona -> y se está seleccionando la dificultad, se sube de dificultad
                Si se está seleccionando "Créditos", se vuelve a "Salir".
                """
                if event.key == pygame.K_RIGHT:
                    if selection == 2:
                        Config.increaseDif()
                        Config.drawSelectedButton(selection)
                    elif selection == 5:
                        Config.drawUnselectedButton(selection)
                        selection = 4
                        Config.drawSelectedButton(selection)
                """-------------------------------------------------------------------------"""
                """
                Si se presiona "z":
                    -y se está seleccionando "Jugar", se devuelve 1.
                    -y se está seleccionando "Audio", se activa/desactiva el audio.
                    -y se está seleccionando "Salir", se devuelve 0.
                """
                if event.key == pygame.K_z:
                    if selection == 1:
                        return 1
                    if selection == 3:
                        Config.audio = not Config.audio
                        if Config.audio:
                            pygame.mixer.music.unpause()
                        else:
                            pygame.mixer.music.pause()
                        Config.drawSelectedButton(selection)
                    if selection == 4:
                        return 0
                    if selection == 5:
                        CreditScreen.run()
                        redraw()

        Config.clock.tick(24)
        # No olvidemos actualizar el display en cada iteración
        pygame.display.update()