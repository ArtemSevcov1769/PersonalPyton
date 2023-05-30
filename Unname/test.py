import pygame, random, math

pygame.init()

window_width = 700
window_height = 500
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('Сквозь вселенную')

background = pygame.transform.scale(pygame.image.load('black.png'), (window_width, window_height))

red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
purple = (139, 0, 139)
yellow = (255, 255, 0)

class GameSprite(pygame.sprite.Sprite):
    def __init__(self, player_x, player_y, size_x, size_y, speed, surface):
        super().__init__()
        colors = [red, green, blue, purple, yellow]
        self.image = pygame.Surface((size_x, size_y))
        self.image.fill(random.choice(colors))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.surface = surface

class Enemy(GameSprite):
    def __init__(self, player_x, player_y, size_x, size_y, speed, surface):
        super().__init__(player_x, player_y, size_x, size_y, speed, surface)
        self.angle = random.uniform(0, 360)

    def update(self):
        x = math.cos(math.radians(self.angle)) * self.speed
        y = math.sin(math.radians(self.angle)) * self.speed
        self.rect.x += x
        self.rect.y += y
        if self.rect.left < 0 or self.rect.right > window_width or self.rect.top < 0 or self.rect.bottom > window_height:
            self.rect.x = random.randint(349, 351)
            self.rect.y = random.randint(249, 251)
            self.angle = random.uniform(0, 360)

enemy_size = 2
enemy_speed = 2
enemies = pygame.sprite.Group()
for i in range(80):
    enemy = Enemy(random.randint(349, 351), random.randint(249, 251), enemy_size, enemy_size, enemy_speed, window)
    enemies.add(enemy)

clock = pygame.time.Clock()

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    window.blit(background, (0, 0))

    enemies.update()
    enemies.draw(window)

    pygame.display.update()

    clock.tick(60)

pygame.quit()