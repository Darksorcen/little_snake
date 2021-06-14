import pygame, sys
from snake_player import Snake
import random

class Game:

    def __init__(self, screen):
        self.screen = screen
        self.running = True
        self.on_menu = True
        self.clock = pygame.time.Clock()
        self.snake = Snake(400, 300, 30, 30)
        self.area_down = pygame.Rect(0, 710, 1080, 10)
        self.area_up = pygame.Rect(0, 0, 1080, 10)
        self.area_right = pygame.Rect(1070, 0, 10, 720)
        self.area_left = pygame.Rect(0, 0, 10, 720)
        self.point = Snake(random.randint(50, 1000), random.randint(50, 650), 20, 20)
        self.area_list = [self.area_down, self.area_up, self.area_right, self.area_left]
        self.rect_menu = pygame.Rect(440, 260, 200, 100)
        self.music_background = pygame.mixer.Sound("electro_chill_music.ogg")

    def save_score(self):
        with open("score.txt", "r") as file_score:
            best_score = int(file_score.readline(1))
        if best_score >= self.snake.score:
            self.snake.best_score = best_score
        elif best_score < self.snake.score:
            with open("score.txt", "w") as file_score:
                file_score.write(str(self.snake.score))
                self.snake.best_score = self.snake.score
    def launch_music(self):
        self.music_background.play(-1, 0)
        self.music_background.set_volume(0.7)
        pygame.display.flip()

    def menu(self):
        while self.on_menu:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.on_menu = False
                    self.running = False    
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.on_menu = False

            pygame.draw.rect(self.screen, (255, 255, 255), self.rect_menu, 3)
            pixel_font_120 = pygame.font.Font("PixelOperator.ttf", 120)
            title_text = pixel_font_120.render("Snake", True, (255, 255, 255))
            pixel_font_45 = pygame.font.Font("PixelOperator.ttf", 45)
            text_menu = pixel_font_45.render("Snake", True, (255, 255, 255))
            pixel_font_25 = pygame.font.Font("PixelOperator.ttf", 25)
            press_space_to_play = pixel_font_25.render("Press 'space' to play", True, (255, 255, 255))
            self.screen.blit(title_text, (415, 100))
            self.screen.blit(text_menu, (493.5, 285.5))
            self.screen.blit(press_space_to_play, (435, 360))
            pygame.display.flip()

    def handling_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.snake.velocity[0] = -1
            self.snake.velocity[1] = 0
        elif keys[pygame.K_RIGHT]:
            self.snake.velocity[0] = 1
            self.snake.velocity[1] = 0
        else:
            pass
        if keys[pygame.K_UP]:
            self.snake.velocity[1] = -1
            self.snake.velocity[0] = 0
        elif keys[pygame.K_DOWN]:
            self.snake.velocity[1] = 1
            self.snake.velocity[0] = 0
        else:
            pass

    def update(self):
        self.snake.move()
        for area in self.area_list:
            if area.colliderect(self.snake):
                self.save_score()
                self.screen.fill((0, 0, 0))
                pixel_font_60 = pygame.font.Font("PixelOperator.ttf", 60)
                lose_text = pixel_font_60.render("You lost", True, (255, 255, 255))
                score = pixel_font_60.render(f"Score : {self.snake.score}", True, (255, 255, 255))
                best_score_text = pixel_font_60.render(f"Best score : {self.snake.best_score}", True, (255, 255, 255))
                self.screen.blit(lose_text, (400, 230))
                self.screen.blit(score, (400, 290))
                self.screen.blit(best_score_text, (400, 350))
                pygame.display.flip()
                self.running = False
                pygame.time.delay(3000)
                sys.exit()
            
        if self.point.rect.colliderect(self.snake):
            self.snake.score_up()
            self.point.go_to(random.randint(30, 1050), random.randint(30, 690))

    def display(self):
        self.screen.fill((0, 0, 0))
        for area in self.area_list:
            pygame.draw.rect(self.screen, (50, 150, 25), area)
        pygame.draw.rect(self.screen, (50, 150, 25), self.snake.rect)
        pygame.draw.rect(self.screen, (255, 0, 0), self.point)
        pygame.display.flip()
    def run(self):
        self.launch_music()
        self.menu()
        while self.running:                 
            self.handling_events()
            self.update()
            self.display()
            self.clock.tick(60)

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((1080, 720))
pygame.display.set_caption("Snake")

game = Game(screen)

game.run()

pygame.quit()