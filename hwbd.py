import pygame,sys
import time
pygame.init()
screen= pygame.display.set_mode((600,600))
pygame.display.set_caption("Mothersday Slideshow(^_^)")
screen.fill("white")
img=pygame.image.load("m1.jpg")
image1=pygame.transform.scale(img,(600,600))

pygame.display.update()
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
    screen.blit(image1,(0,0))
    font=pygame.font.SysFont("comicsansms",70)
    pygame.display.update()
    time.sleep(2)
    
    img1=pygame.image.load("m2.jpg")
    image2=pygame.transform.scale(img1,(600,600))
    screen.blit(image2,(0,0))
    font2=pygame.font.SysFont("comicsansms",20)
    
    pygame.display.update()
    time.sleep(2)

    img2=pygame.image.load("m3.jpg")
    image3=pygame.transform.scale(img2,(600,600))
    screen.blit(image3,(0,0))
    pygame.display.update()
    time.sleep(2)
