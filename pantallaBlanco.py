# importo el modulo
import pygame 

class Cursor(pygame.Rect):
    """
    This class is used to see what the mouse does inside the window.
    """
    def __init__(self):
        pygame.Rect.__init__(self,0,0,1,1)

    def update(self):
        self.left,self.top= pygame.mouse.get_pos()
        pass

class Boton(pygame.sprite.Sprite):
    """docstring for [object Object]."""
    def __init__(self,imagen1,imagen2,x=200,y=200):
        self.imagen_normal= imagen1
        self.imagen_selection= imagen2
        self.imagen_actual= self.imagen_normal
        self.rect= self.imagen_actual.get_rect()
        self.rect.left,self.rect.top= (x,y)

    def update(self,screen,cursor):
        if cursor.colliderect(self.rect):
            self.imagen_actual= self.imagen_selection
        else:
            self.imagen_actual= self.imagen_normal
        screen.blit(self.imagen_actual,self.rect)

#funcion main
def main():
    pygame.init() # inicializo el modulo
    
    # fijo las dimensiones de la pantalla a 300,300 y creo una superficie que va ser la principal
    pantalla=pygame.display.set_mode((300,300))
    
    pygame.display.set_caption("Mi Ventana") # Titulo de la Ventana
    #creo un reloj para controlar los fps
    reloj1=pygame.time.Clock()
    
    asteroideCayendo1= pygame.image.load("fallingAsteroid1.png")
    asteroideCayendo2= pygame.image.load("fallingAsteroid2.png")

    boton= Boton(asteroideCayendo1,asteroideCayendo2)
    cursor= Cursor()

    blanco=(255,255,255) # color blanco en RGB
    
    salir=False
    #LOOP PRINCIPAL
    while salir!=True:
        #recorro todos los eventos producidos
        #en realidad es una lista
        for event in pygame.event.get():
            # si el evento es del tipo 
            # pygame.QUIT( cruz de la ventana)
            if event.type == pygame.QUIT:
                salir=True
        
        reloj1.tick(20)#operacion para que todo corra a 20fps
        pantalla.fill(blanco) # pinto la superficie de blanco
        cursor.update()
        boton.update(pantalla,cursor)
        
        pygame.display.update() #actualizo el display
        
    pygame.quit()
    
main() 