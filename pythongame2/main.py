import pygame as pg
import random
from pygame.sprite import Sprite
from typing import List,Tuple





pg.init()

window=pg.display.set_mode((800,600))

pg.display.set_caption("猜拳游戏！")

clock=pg.time.Clock()




rock_img=pg.image.load("猜拳手势/1778078996074.png").convert_alpha()
scissors_img=pg.image.load("猜拳手势/1778078992389.png").convert_alpha()
paper_img=pg.image.load("猜拳手势/1778078531040.png").convert_alpha()


rock_img=pg.transform.scale(rock_img,(100,100))
scissors_img=pg.transform.scale(scissors_img,(100,100))
paper_img=pg.transform.scale(paper_img,(100,100))


rock_img.set_colorkey('white')
scissors_img.set_colorkey('white')
paper_img.set_colorkey('white')


rect=rock_img.get_rect()
rect=scissors_img.get_rect()
rect=paper_img.get_rect()
# rect.center=window.get_rect().center


rock_rect=rock_img.get_rect(topleft=(50,350))#topleft获取左上角坐标
scissors_rect=scissors_img.get_rect(topleft=(350,350))
paper_rect=paper_img.get_rect(topleft=(650,350))



font=pg.font.Font("fonts/STKAITI.TTF",36)#显示中文需要中文字体，不能默认字体


player_choice=None
computer_rect=None
computer_display_img=None
computer=None
hand=None
isRunning=True
result="请出拳！"

while isRunning:
    for ev in pg.event.get():
        if ev.type==pg.QUIT:
            isRunning=False
            break

        elif ev.type==pg.MOUSEBUTTONDOWN:#打印鼠标点击区域
            x,y=ev.pos
            if rock_rect.collidepoint(x,y):
                print("你点了拳头！")
                hand = "你点了拳头！"
                player_choice="rock"
            elif scissors_rect.collidepoint(x,y):
                print("你点了剪刀！")
                hand="你点了剪刀！"
                player_choice="scissors"
            elif paper_rect.collidepoint(x,y):
                print("你点了布！")
                hand="你点了布！"
                player_choice="paper"

            computer_choice = random.choice(["rock", "scissors", "paper"])

            if player_choice==computer_choice:
                result="平局！"
            elif (player_choice=="rock" and computer_choice=="scissors")\
                or (player_choice=="scissors" and computer_choice=="paper")\
                or (player_choice=="paper" and computer_choice=="rock"):
                result="你赢了！"
            else:
                result="你输了！"

            if computer_choice=="rock":
                computer_display_img=rock_img
                computer="对方出了拳头！"
            elif computer_choice=="scissors":
                computer_display_img=scissors_img
                computer = "对方出了剪刀！"
            elif computer_choice=="paper":
                computer_display_img=paper_img
                computer = "对方出了布！"

            if computer_choice:
                computer_rect=computer_display_img.get_rect(topleft=(350,50))








    text_img = font.render(result, True, 'black','white')
    hand_img = font.render(hand, True, 'black','white')
    computer_img = font.render(computer, True, 'black','white')



    window.fill(pg.Color(255,255,255))


    window.blit(text_img,(335,230))
    window.blit(hand_img,(320,300))
    window.blit(computer_img,(320,150))


    if computer_display_img is not None and computer_rect is not None:
        window.blit(computer_display_img, computer_rect)


    window.blit(rock_img,rock_rect)
    window.blit(scissors_img,scissors_rect)
    window.blit(paper_img,paper_rect)








    pg.display.update()
    clock.tick(60)



pg.quit()
