import pygame

pygame.init() #초기화 (반드시 필요)

#화면 크기 설정
screen_width = 480 #가로 크기
screen_height = 640 #세로 크기
pygame.display.set_mode((screen_width, screen_height)) ###

#화면 제목 설정
pygame.display.set_caption("지원 게임") ##3
#이벤트 루프
running = True #게임이 진행중인가?
while running:
    for event in pygame.event.get(): ###프로그램이 종료되지 않도록 계속 대기(파이게임에서 계속 써야함)
       if event.type == pygame.QUIT: # 창이 닫히는 이벤트가 발생하였는가 = 창 끄는 x를 눌렀는가?
        running = False

#pygame 종료
pygame.quit()