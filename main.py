import pygame
from pygame import Vector2
pygame.init()
size = width, height = 800,600
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

class Ball():
    def __init__(self,width,height):
        self.width = width
        self.height = height
        self.image = pygame.transform.scale(pygame.image.load('ball.png'),(100,100))
        self.rect = self.image.get_rect(center = (width/2,height/2))
        self.gravity = 0.2
        self.velocity = Vector2(10,25)

    def update(self):
        screen.blit(self.image,self.rect)
    
    def movement(self):
        self.velocity.y += self.gravity
        self.rect = self.rect.move(self.velocity)
        if self.rect.bottom >= self.height:
            self.rect.bottom = self.height
            self.velocity.y = - self.velocity.y * 0.9
            self.velocity.x = self.velocity.x * 0.99
        if self.rect.top <= 0:
            self.velocity.y = -self.velocity.y

        if self.rect.left <= 0 or self.rect.right >= self.width:
            self.velocity.x = -self.velocity.x
        ...
ball = Ball(width,height)    

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    screen.fill('black')
    ball.movement()
    ball.update()


    pygame.display.update()
    clock.tick(60)