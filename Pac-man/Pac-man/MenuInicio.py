import pygame, sys
import Imagen
import Imagenes
import Juego
import PantallaCarga
import Nodo
import Jugador
import Niveles
class MenuInicio(object):
    def Menu():    
        j = Juego.Juego
        
        lista_botones = []
        pygame.init()

        size = width, height = 820, 720
        white = 255, 255, 255

        screen = pygame.display.set_mode(size)

        fondo = pygame.image.load("recursos/fondos/fondo.jpg")
        pygame.display.set_caption("juego ball")

        fondo = pygame.transform.scale(fondo,(820,720))
        logorect = fondo.get_rect()

        pacmanicono = pygame.image.load("recursos/fondos/pacmancarga.png").convert_alpha()

        pacmanicono = pygame.transform.scale(pacmanicono,(300,199))
        pacmanicono_pos_x = 260
        pacmanicono_pos_y = 450
        imagenes = Imagenes.Imagenes()
        btn_Nueva_Partida = Imagen.Imagen(imagenes.obtener_imagen_boton("NuevaPartida",200,50), 320, 200, 200, 50)
        lista_botones.append(btn_Nueva_Partida)
        btn_Cargar_Partida = Imagen.Imagen(imagenes.obtener_imagen_boton("CargarPartida",200,50), 320, 300, 200, 50)
        configuracion_juego= Imagen.Imagen(imagenes.obtener_imagen_boton("configuracionJ",40,40), 760, 20, 40, 40)
        lista_botones.append(btn_Cargar_Partida)
        cur_Mouse = []
        run=True
        while run:
            var = True
            for event in pygame.event.get():
                if event.type == pygame.QUIT: 
                    run = False
                    
                if pygame.mouse.get_pressed(3)==(1,0,0):
                    x1, y1 = pygame.mouse.get_pos()
                    if(btn_Nueva_Partida.comparar_cord(x1,y1)):
                        n = Niveles.Niveles
                        n.Nivel(0)
                        var = False
                        run = False
                    if(btn_Cargar_Partida.comparar_cord(x1,y1)):
                        p = PantallaCarga.PantallaCarga
                        p.pantalla(p,'C',0,0)
                        var = False
                        run = False
                    
            if var:
                screen.fill(white)
                screen.blit(fondo, (0,0))
                screen.blit(pacmanicono, (pacmanicono_pos_x, pacmanicono_pos_y))
                screen.blit(lista_botones[0].imagen, (lista_botones[0].i, lista_botones[0].j))
                screen.blit(btn_Cargar_Partida.imagen, (btn_Cargar_Partida.i, btn_Cargar_Partida.j))
                screen.blit(configuracion_juego.imagen, (configuracion_juego.i, configuracion_juego.j))
                pygame.display.flip()
        pygame.quit()
