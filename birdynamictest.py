#coding=gbk
# 导入pygame
import pygame

# 导入随机函数
import random

# 导入pygame坐标系
from pygame.locals import *

import time

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.image = pygame.image.load('airplane.png').convert()
        self.image.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.image.get_rect()
	#定义飞机操作动作
    def update(self, pressed_keys):
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -5)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 5)
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-5, 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(5, 0)

        # 确保飞机在屏幕内
        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > 1500:
            self.rect.right = 1500
        if self.rect.top <= 0:
            self.rect.top = 0
        elif self.rect.bottom >= 1000:
            self.rect.bottom = 1000

#定义斑翅山鹑，沙百灵，云雀
class Banchishanchun(pygame.sprite.Sprite):
    def __init__(self):
        super(Banchishanchun, self).__init__()
        self.image = pygame.image.load('banchishanchun.png').convert()
        self.image.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.image.get_rect(
            #定义出生点的生成区域
            center=(random.randint(820, 1600), random.randint(500, 700)))
        #设定鸟类飞行速度
        self.speed = random.randint(1, 5)

    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()

class Shabailing(pygame.sprite.Sprite):
    def __init__(self):
        super(Shabailing, self).__init__()
        self.image = pygame.image.load('shabailing.png').convert()
        self.image.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.image.get_rect(
            center=(random.randint(820, 1600), random.randint(0, 200)))
        self.speed = random.randint(2, 10)

    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()

class Yunque(pygame.sprite.Sprite):
    def __init__(self):
        super(Yunque, self).__init__()
        self.image = pygame.image.load('yunque.png').convert()
        self.image.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.image.get_rect(
            center=(random.randint(820, 1600), random.randint(300, 500)))
        self.speed = random.randint(5, 20)

    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()

#定义云朵
class Cloud(pygame.sprite.Sprite):
    def __init__(self):
        super(Cloud, self).__init__()
        self.image = pygame.image.load('cloud.png').convert()
        self.image.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.image.get_rect(center=(
            random.randint(820, 1600), random.randint(0, 400))
        )

    def update(self):
        self.rect.move_ip(-5, 0)
        if self.rect.right < 0:
            self.kill()

# 初始化pygame
pygame.init()

# 生产1500,1000的屏幕界面
screen = pygame.display.set_mode((1500, 1000))

# 设定增加鸟类和云朵的时间.可以控制生成频率
ADDBANCHISHANCHUN = pygame.USEREVENT + 1
pygame.time.set_timer(ADDBANCHISHANCHUN, 5000)
ADDCLOUD = pygame.USEREVENT + 2
pygame.time.set_timer(ADDCLOUD, 6000)
ADDSHABAILING = pygame.USEREVENT + 3
pygame.time.set_timer(ADDSHABAILING, 5000)
ADDYUNQUE = pygame.USEREVENT + 4
pygame.time.set_timer(ADDYUNQUE, 5000)

# 生成飞机
player = Player()
#设定背景
background = pygame.Surface(screen.get_size())
background = pygame.image.load('background.png')

birds = pygame.sprite.Group()
clouds = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)
#运行主循环
running = True

while running:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
        elif event.type == QUIT:
            running = False
        elif event.type == ADDYUNQUE:
            new_enemy = Yunque()
            birds.add(new_enemy)
            all_sprites.add(new_enemy)
        elif event.type == ADDBANCHISHANCHUN:
            new_enemy = Banchishanchun()
            birds.add(new_enemy)
            all_sprites.add(new_enemy)
        elif event.type == ADDSHABAILING:
            new_enemy = Shabailing()
            birds.add(new_enemy)
            all_sprites.add(new_enemy)
        elif event.type == ADDCLOUD:
            new_cloud = Cloud()
            all_sprites.add(new_cloud)
            clouds.add(new_cloud)
    screen.blit(background, (0, 0))
    pressed_keys = pygame.key.get_pressed()
    player.update(pressed_keys)
    birds.update()
    clouds.update()
    for entity in all_sprites:
        screen.blit(entity.image, entity.rect)

    if pygame.sprite.spritecollideany(player, birds):
        background = pygame.image.load('you lose.png')
        player.image = pygame.image.load('hit.png').convert()
        player.image.set_colorkey((255, 255, 255), RLEACCEL)
    if pressed_keys[K_g]:
     player.rect.move_ip(10,6)
     if player.rect.bottom > 580:
        player.rect.move_ip(0,-6)        
    if pressed_keys[K_SPACE]:
        background = pygame.image.load('background.png')
        player.image = pygame.image.load('airplane.png').convert()
        player.image.set_colorkey((255, 255, 255), RLEACCEL)
        player.rect = player.image.get_rect()
    pygame.display.flip()
