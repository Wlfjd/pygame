import pygame
from random import *
pygame.init() # 초기화
 #스크린 설정
screen_wid = 480
screen_hei = 640
screen = pygame.display.set_mode((screen_wid, screen_hei))
#화면 제목 설정
pygame.display.set_caption("지원이의 똥피하기 게임")

####################################################

#배경 이미지
background = pygame.image.load("C:/Users/jwmam/Desktop/PythonWorkspace/pygmae_basic/background.png")
#캐릭터 이미지
a= pygame.image.load("C:\\Users\\jwmam\\Desktop\\PythonWorkspace\\pygmae_basic\\character.png")
b= pygame.image.load("C:\\Users\\jwmam\\Desktop\\PythonWorkspace\\pygmae_basic\\enemy.png")
a_size=a.get_rect().size
a_w = a_size[0]
a_h = a_size[1]
a_x = screen_wid/2 - a_w/2 
a_y = screen_hei - a_h
a_speed = 10

b_size=b.get_rect().size
b_h = b_size[0]
b_w = b_size[1]
b_x = randint(0, screen_wid - b_w)
b_y = 0 
b_speed = 10


to_x=0
to_y=0

fps = pygame.time.Clock()

running = True
while running:
    f= fps.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                to_x += a_speed
            elif event.key == pygame.K_LEFT:
                to_x -= a_speed

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                to_x = 0
  
    b_y += b_speed   # 위에서부터 10,20,30 ...점점 내려오는 효과
    #a,b 위치 정보 업데이트        
    a_x += to_x 
    # a_y += to_y 
    
    if b_y > screen_hei:
        b_y =  0 # 다시 똥을 위로 올린다 
        b_x = randint(0, screen_wid - b_w)        

    if a_x < 0:
        a_x = 0
    if a_x > screen_wid - a_w:
        a_x = screen_wid - a_w

    #충돌 처리
    a_rect = a.get_rect()
    a_rect.left = a_x
    a_rect.top = a_y

    b_rect = b.get_rect()
    b_rect.left = b_x
    b_rect.top = b_y

    if a_rect.colliderect(b_rect):
        print("충돌했어요 . Game Over")
        running = False

        
    screen.blit(background,(0,0))
    screen.blit(a,(a_x,a_y))
    screen.blit(b,(b_x,b_y))
    pygame.display.update()
   
pygame.quit()
     