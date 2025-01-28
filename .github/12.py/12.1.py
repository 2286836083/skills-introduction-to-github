import pygame
import sys
from role import Role

class Sky:
    def __init__ (self):
        pygame.init()
        self.clock=pygame.time.Clock()
        self.screen=pygame.display.set_mode((1200,800))
        pygame.display.set_caption("made by 李睿恒")
        self.bg_color=(135,206,250)
        self.role=Role(self)

    def run_game(self):
        while True:
            self._check_events()
            self.role.update()   
            self._update_screen() 
                   
            self.clock.tick(60)
     
    def _check_events(self):
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                sys.exit()
            elif event.type==pygame.KEYDOWN:
                if event.key==pygame.K_RIGHT:
                    self.role.moving_right=True
                elif event.key==pygame.K_LEFT:
                    self.role.moving_left=True
                elif event.key==pygame.K_UP:
                    self.role.moving_up=True
                elif event.key==pygame.K_DOWN:
                    self.role.moving_down=True
            elif event.type==pygame.KEYUP:
                if event.key==pygame.K_RIGHT:
                        self.role.moving_right=False
                elif event.key==pygame.K_LEFT:
                        self.role.moving_left=False
                elif event.key==pygame.K_UP:
                        self.role.moving_up=False
                elif event.key==pygame.K_DOWN:
                        self.role.moving_down=False
                  
    
    def _update_screen(self):
        self.screen.fill(self.bg_color)
        self.role.blitme()
        pygame.display.flip()

if __name__=='__main__':
    sky=Sky()
    sky.run_game()
