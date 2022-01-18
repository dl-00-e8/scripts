import random
import pygame
from os import system

pygame.init()


# Setting Environment
pygame.disply.set_caption("야간 녹이기")

height = 640
width = 480
screen = pygame.display.set_mode((width, height))

clock = pygame.time.Clock()

background = pygame.image.load('배경화면 파일 경로')

gameFont = pygame.font.Font(None, 20)

white = (255, 255, 255)
black = (0, 0, 0)


# In Game Setting
startTime = pygame.time.get_ticks()

character = pygame.image.load('캐릭터 파일 경로')
characterSize = character.get_rect().size
characterWidth = characterSize[0]
characterHeight = characterSize[1]
characterXpos = (width / 2) - (characterWidth / 2)
characterYpos = height - characterHeight
characterSpeed = 0.3
toX = 0

enemy = pygame.image.load('적 파일 경로')
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
    
    # 좌, 우 이동
    keyEvent = pygame.key.get_pressed()
    if keyEvent[pygame.K_LEFT]:
        characterXpos -= 18
    if keyEvent[pygame.K_RIGHT]:
        characterXpos += 18
    
    # 경계 처리
    if characterXpos < 0:
        characterXpos = 0
    elif characterXpos > width - characterWidth:
        characterXpos = widt - characterWidth
    
    # 적이 내려옴
    randomNumberX = random.randrange(1, 440)
    randomNumberY = random.randrange(1, 100)

    if enemyYpos > 640:
        enemyXpos = randomNumberX
        enemyYpos = randomNumberY
        enemySpeed += 0.5
        nowScore += 1
    
    enemyYpos += enemySpeed

    # 충돌 처리
    characterRect = character.get_rect()
    characterRect.left = characterXpos
    characterRect.top = characterYpos

    enemyRect = enemy.get_rect()
    enemyRect.left = enemyXpos
    enemyRect.top = enemyYpos

    if characterRect.colliderect(enemyRect):
        nowTime = (pygame.time.get_ticks() - startTime) // 1000
        print("Game Over : " + str(int(nowTime)) + "초, 점수 : " + str(nowScore) + "점")
        done = True

    # 화면 바탕 채우기
    screen.blit(background, [0, 0])

    # 캐릭터, 적 이미지 로드
    screen.blit(character, (characterXpos, characterYpos))
    screen.blit(enemy, (enemyXpos, enemyYpos))

    # 타이머 출력
    nowTime = (pygame.time.get_ticks() - startTime) // 1000
    timer = gameFont.render("Timer : " + str(int(nowTime)), True, white)
    screen.blit(timer, [10, 10])

    # 스코어 출력
    score = gameFont.render("Score : " + str(nowScore), True, white)
    screen.blit(score, [410, 10])

    # 화면 업데이트하기
    pygame.display.update()


pygame.quit()