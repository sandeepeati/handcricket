import pygame, sys, time, random

checkErrors = pygame.init()

if checkErrors[1] > 0:
    print("(!) Had {0} initializing errors,exiting.....".format(checkErrors[1]))
    sys.exit(-1)
else:
    print("(+) pygame successfully initialized")

# game logic

def game():
    """
    Hand cricket...press keys from 1 to 6 and if the bowler(computer) chooses the same
    number...You will be declared OUT!
    """
    playsurface = pygame.display.set_mode((700,390))
    pygame.display.set_caption('Hand Cricket by SandeepEti')

    # colors
    red = pygame.Color(255, 0, 0)   # if batsman out
    black = pygame.Color(0, 0, 0)  # score
    white = pygame.Color(255, 255, 255)

    # fps controller

    fpsController = pygame.time.Clock()

    # background image
    bg = pygame.image.load("cp.jpg")
    bgRect = bg.get_rect()

    runs = 0

    def out(r):
        myFont = pygame.font.SysFont('monaco', 72)
        Osurf = myFont.render('OUT', True, red)
        Orect = Osurf.get_rect()
        Orect.midtop = (350, 15)
        playsurface.blit(Osurf, Orect)
        showscore(runs)
        pygame.display.flip()
        time.sleep(5)
        game()

    def showscore(r):
        sFont = pygame.font.SysFont('monaco', 40)
        ssurf = sFont.render('Runs: {0}'.format(r), True, black)
        srect = ssurf.get_rect()
        srect.midtop = (350,250)
        playsurface.blit(ssurf, srect)

    def batsmen(r):
        sFont = pygame.font.SysFont('monaco', 70)
        ssurf = sFont.render('Batsman: {0}'.format(r), True, black)
        srect = ssurf.get_rect()
        srect.midtop = (150,50)
        playsurface.blit(ssurf, srect)

    def bowler(r):
        sFont = pygame.font.SysFont('monaco', 70)
        ssurf = sFont.render('Bowler: {0}'.format(r), True, black)
        srect = ssurf.get_rect()
        srect.midtop = (550,50)
        playsurface.blit(ssurf, srect)

    bowl = 0
    k = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                bowl = random.randrange(1,7)
                if event.key == pygame.K_1:
                    if bowl == 1:
                        out(runs)
                    else:
                        runs = runs + 1
                        k = 1
                        
                if event.key == pygame.K_2:
                    if bowl == 2:
                        out(runs)
                    else:
                        runs += 2
                        k = 2
                        
                if event.key == pygame.K_3:
                    if bowl == 3:
                        out(runs)
                    else:
                        runs += 3
                        k = 3
                        
                if event.key == pygame.K_4:
                    if bowl == 4:
                        out(runs)
                    else:
                        runs += 4
                        k = 4
                        
                if event.key == pygame.K_5:
                    if bowl == 5:
                        out(runs)
                    else:
                        runs += 5
                        k = 5
                        
                if event.key == pygame.K_6:
                    if bowl == 6:
                        out(runs)
                    else:
                        runs += 6
                        k = 6
                        
                if event.key == pygame.K_ESCAPE:
                    pygame.event.post(pygame.event.Event(pygame.QUIT))

        # drawing

        playsurface.fill(white)
        playsurface.blit(bg,bgRect)
        batsmen(k)
        bowler(bowl)
        showscore(runs)
        pygame.display.flip()
        fpsController.tick(23)

game()

