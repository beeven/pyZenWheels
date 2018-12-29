import pygame
import microcar

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

class TextPrint(object):
    def __init__(self):
        self.reset()
        self.font = pygame.font.Font(None, 20)

    def print(self, screen, textString):
        textBitmap = self.font.render(textString, True, BLACK)
        screen.blit(textBitmap, [self.x, self.y])
        self.y += self.line_height
    
    def reset(self):
        self.x = 10
        self.y = 10
        self.line_height = 15
    
    def indent(self):
        self.x += 10
    
    def unindent(self):
        self.x -= 10

pygame.init()

size = [500, 700]
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Controller")

done = False

clock = pygame.time.Clock()

pygame.joystick.init()

textPrint = TextPrint()

joystick = pygame.joystick.Joystick(0)
joystick.init()


car = microcar.Car('00:06:66:61:A3:EA')
car.init()


last_steer = 0
last_speed = 0
last_horn = 0
last_light = 0
last_left_sidelight = 0
last_right_sidelight = 0



while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.JOYBUTTONDOWN:
            if event.button == 4:
                car.toggle_left_sidelight()
            elif event.button == 5:
                car.toggle_right_sidelight()
            elif event.button == 0:
                car.toggle_light()


    screen.fill(WHITE)
    textPrint.reset()

    joystick_count = pygame.joystick.get_count()
    

    axes = joystick.get_numaxes()
    textPrint.print(screen, "number of axes: {}".format(axes))
    textPrint.indent()

    for i in range(axes):
        axis = joystick.get_axis(i)
        textPrint.print(screen, "Axis {} values: {:>6.3f}".format(i, axis))
    textPrint.unindent()

    buttons = joystick.get_numbuttons()
    textPrint.print(screen, "Number of buttons: {}".format(buttons) )
    textPrint.indent()

    for i in range( buttons ):
        button = joystick.get_button( i )
        textPrint.print(screen, "Button {:>2} value: {}".format(i,button) )
    textPrint.unindent()


    hats = joystick.get_numhats()
    textPrint.print(screen, "Number of hats: {}".format(hats) )
    textPrint.indent()

    for i in range( hats ):
        hat = joystick.get_hat( i )
        textPrint.print(screen, "Hat {} value: {}".format(i, str(hat)) )
    textPrint.unindent()


    steer = joystick.get_axis(0)
    if steer != last_steer:
        last_steer = steer
        car.steer(steer)

    speed = -1 * joystick.get_axis(2)
    if speed != last_speed:
        last_speed = speed
        car.drive(speed)
    
    horn = joystick.get_button(1)
    if last_horn != horn:
        last_horn = horn
        car.toggle_horn(horn)

    # light = joystick.get_button(1)
    # left_sidelight = joystick.get_button(5)
    # right_sidelight = joystick.get_button(6)


    pygame.display.flip()

    clock.tick(20)

pygame.quit()
