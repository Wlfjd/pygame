import pygame

pygame.init() #초기화 (반드시 필요)

#화면 크기 설정
screen_width = 480 #가로 크기
screen_height = 640 #세로 크기
screen = pygame.display.set_mode((screen_width, screen_height)) ### 스크린 정의

#화면 제목 설정
pygame.display.set_caption("지원 게임") ###

#FPS
clock = pygame.time.Clock()

#배경 이미지 불러오기
background = pygame.image.load("C:/Users/jwmam/Desktop/PythonWorkspace/pygmae_basic/background.png")

#캐릭터(스프라이트) 불러오기
character = pygame.image.load("C:/Users/jwmam/Desktop/PythonWorkspace/pygmae_basic/character.png")
character_size= character.get_rect().size #이미지 크기를 구해옴, rectangle
character_width = character_size[0] #캐릭터 가로 크기
character_height = character_size[1] #캐릭터 세로 크기
character_x_pos = screen_width/2 - character_width/2 #화면 가로의 절반 크기에 해당하는 곳에 위치
character_y_pos = screen_height - character_height#화면 세로 크기 가장 아래에 해당하는 곳에 위치
 
#이동할 좌표
to_x = 0
to_y = 0

#이동속도
speed = 0.5

#적 ennemy 캐릭터 불러오기
enemy = pygame.image.load("C:/Users/jwmam/Desktop/PythonWorkspace/pygmae_basic/enemy.png")
enemy_size= enemy.get_rect().size #이미지 크기를 구해옴, rectangle
enemy_width = enemy_size[0] #캐릭터 가로 크기
enemy_height = enemy_size[1] #캐릭터 세로 크기
enemy_x_pos = screen_width/2 - enemy_width/2 #화면 가로의 절반 크기에 해당하는 곳에 위치
enemy_y_pos = screen_height/2 - enemy_height/2#화면 세로 크기 가장 아래에 해당하는 곳에 위치

#폰트 정의
game_font = pygame.font.Font(None, 40) #폰트객체 생성(폰트 넌 = 디폴트 , 크기)
#총 시간
total_time = 10
#시작 시간 정보
start_ticks = pygame.time.get_ticks() #현재 tick을 받아옴




#이벤트 루프 
running = True #게임이 진행중인가?
while running:
    delta = clock.tick(200) #게임화면 초당 프레임 수를 설정 , 숫자가 클수록 움직임이 부드러워짐(버벅임이 덜해짐)

    for event in pygame.event.get(): ###프로그램이 종료되지 않도록 계속 대기(파이게임에서 계속 써야함)
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트가 발생하였는가 = 창 끄는 x를 눌렀는가?
            running = False

        if event.type == pygame.KEYDOWN: #키가 눌러졌는지 확인
            if event.key == pygame.K_LEFT: #캐릭터를 왼쪽으로
                to_x -= speed
            elif event.key == pygame.K_RIGHT:
                to_x += speed 
            elif event.key == pygame.K_UP:
                to_y -= speed 
            elif event.key == pygame.K_DOWN:
                to_y += speed 

        if event.type == pygame.KEYUP: #방향키를 떼면 멈춤
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0
                
    character_x_pos += to_x * delta #캐릭터 위치 변경
    character_y_pos += to_y * delta

    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    if character_y_pos < 0:
        character_y_pos = 0
    elif character_y_pos > screen_height - character_height:
        character_y_pos = screen_height - character_height

    #충돌처리를 위한 rect 정보 업데이트
    character_rect=character.get_rect() #캐릭터가 가지고 있는 렉텡글 정도 가져옴
    character_rect.left = character_x_pos #캐릭터가 가지고 있는 렉텡글 정도 업데이트(렉텡클에 x,y 포지션을 반영해줘야함)
    character_rect.top = character_y_pos

    enemy_rect=enemy.get_rect() #캐릭터가 가지고 있는 렉텡글 정도 가져옴
    enemy_rect.left = enemy_x_pos #캐릭터가 가지고 있는 렉텡글 정도 업데이트
    enemy_rect.top = enemy_y_pos

    #충돌체크
    if character_rect.colliderect(enemy_rect): #사각형을 기준으로 충돌이 있었는지 확인(캐릭터와 에너미가 충돌)
        print("충돌했어요")
        running = False

    screen.blit(background,(0, 0))  # 배경 그리기
    screen.blit(character,(character_x_pos,character_y_pos)) # 캐릭터 그리기
    screen.blit(enemy,(enemy_x_pos,enemy_y_pos)) # enemy 그리기

    #타이머 집어넣기
    #경과시간 계산
    elapsed_time = (pygame.time.get_ticks()-start_ticks) / 1000 #경과시간(ms)을 1000으로 나누어 초단위로 표시

    timer = game_font.render(str(int(total_time - elapsed_time)), True, (255,255,255)) #render: 실제로 글자를 그리는 작업
    # render(출력할 글자, True, 글자색상 )
    screen.blit(timer,(10,10))

    #만약 시간이 0이하이면 게임 종료
    if total_time - elapsed_time <= 0:
        print("타임아웃")
        running = False

    pygame.display.update() ###게임 화면 다시 그리기


#잠시 대기
pygame.time.delay(2000) #2초 정도 대기

#pygame 종료
pygame.quit()