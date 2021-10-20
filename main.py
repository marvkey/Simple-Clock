import sys, pygame
import core,timer,AlarmClock


background_colour = (255,255,255)
(width, height) = (300, 200)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('clock app')
screen.fill(background_colour)
pygame.display.flip()
running = True
Gui = AlarmClock.AlarmClock()
def main():
    while True:
        Gui.onupdate()
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                sys.exit()
        pygame.display.update()
    
        for temp in core.allButton:
            temp.Render(screen)
        
        for alarmClock in AlarmClock.allAlarm:
            alarmClock.CheckAlarm()
    pygame.quit()

if __name__ == "__main__":
    main()
      
