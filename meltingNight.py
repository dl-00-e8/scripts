import random
import pygame
from os import system

pygame.init()


# Setting Environment
pygame.disply.set_caption("�߰� ���̱�")

height = 640
width = 480
screen = pygame.display.set_mode((width, height))

clock = pygame.time.Clock()

background = pygame.image.load('���ȭ�� ���� ���')

gameFont = pygame.font.Font(None, 20)

white = (255, 255, 255)
black = (0, 0, 0)


# In Game Setting
startTime = pygame.time.get_ticks()

character = pygame.image.load('ĳ���� ���� ���')
characterSize = character.get_rect().size
characterWidth = characterSize[0]
characterHeight = characterSize[1]
characterXpos = (width / 2) - (characterWidth / 2)
characterYpos = height - characterHeight
characterSpeed = 0.3
toX = 0

enemy = pygame.image.load('�� ���� ���')
enemySize = character.get_rect().size
enemyWidth = characterSize[0]
enemyHeight = characterSize[1]
enemyXpos = (width / 2) - (enemyWidth / 2)
enemyYpos = 100
enemySpeed = 10

randomNumberX = 30
randomNumberY = 30
nowScore = 0


# Main
done = False
while not done:
    dt = clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    
    # ��, �� �̵�
    keyEvent = pygame.key.get_pressed()
    if keyEvent[pygame.K_LEFT]:
        characterXpos -= 18
    if keyEvent[pygame.K_RIGHT]:
        characterXpos += 18
    
    # ��� ó��
    if characterXpos < 0:
        characterXpos = 0
    elif characterXpos > width - characterWidth:
        characterXpos = widt - characterWidth
    
    # ���� ������
    randomNumberX = random.randrange(1, 440)
    randomNumberY = random.randrange(1, 100)

    if enemyYpos > 640:
        enemyXpos = randomNumberX
        enemyYpos = randomNumberY
        enemySpeed += 0.5
        nowScore += 1
    
    enemyYpos += enemySpeed

    # �浹 ó��
    characterRect = character.get_rect()
    characterRect.left = characterXpos
    characterRect.top = characterYpos

    enemyRect = enemy.get_rect()
    enemyRect.left = enemyXpos
    enemyRect.top = enemyYpos

    if characterRect.colliderect(enemyRect):
        nowTime = (pygame.time.get_ticks() - startTime) // 1000
        print("Game Over : " + str(int(nowTime)) + "��, ���� : " + str(nowScore) + "��")
        done = True

    # ȭ�� ���� ä���
    screen.blit(background, [0, 0])

    # ĳ����, �� �̹��� �ε�
    screen.blit(character, (characterXpos, characterYpos))
    screen.blit(enemy, (enemyXpos, enemyYpos))

    # Ÿ�̸� ���
    nowTime = (pygame.time.get_ticks() - startTime) // 1000
    timer = gameFont.render("Timer : " + str(int(nowTime)), True, white)
    screen.blit(timer, [10, 10])

    # ���ھ� ���
    score = gameFont.render("Score : " + str(nowScore), True, white)
    screen.blit(score, [410, 10])

    # ȭ�� ������Ʈ�ϱ�
    pygame.display.update()


pygame.quit()