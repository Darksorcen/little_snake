import pygame 
class Snake:
    def __init__(self, x, y, width, height):
        self.speed = 4
        self.rect = pygame.Rect(x, y, width, height)
        self.velocity = [-1, 0]
        self.score = 0
        self.best_score = None

    def move(self):
        self.rect.move_ip(self.speed * self.velocity[0], self.speed * self.velocity[1])
    
    def score_up(self):
        self.rect = pygame.Rect(self.rect.x, self.rect.y, self.rect.width+3, self.rect.height+3)
        self.score += 1
    
    def go_to(self, x, y):
        self.rect.x = x
        self.rect.y = y

