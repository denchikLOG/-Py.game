import pygame
import sys
import math

pygame.init()

LAIUS,K�RGUS=800,600
ekraan=pygame.display.set_mode((LAIUS,K�RGUS))
pygame.display.set_caption("Lihtne aken")
font=pygame.font.SysFont("arial",50,bold=True)

SININE=(0,0,200)
ROHELINE=(0,255,0)
KOLLANE=(255,255,0)
HALL=(100,100,100)
ROOSA=(255,0,255)
TUMEROOSA=(150,0,150)
VALGE=(255,255,255)
TUMEROHELINE=(0,100,0)

bee_image=pygame.image.load("bee_image.png")
bee_image=pygame.transform.scale(bee_image,(100,100))

def joonista_p�ike():
    for nurk in range(0,360,5):
        l�pp_x=100+200*math.cos(math.radians(nurk))
        l�pp_y=100+200*math.sin(math.radians(nurk))
        pygame.draw.line(ekraan,KOLLANE,(100,100),(l�pp_x,l�pp_y),2)

def joonista_pilv():
    pygame.draw.circle(ekraan,HALL,(650,100),50)
    pygame.draw.circle(ekraan,HALL,(700,130),50)

def joonista_lill():
    for raadius in range(100,10,-10):
        v�rv=ROOSA if raadius%20==0 else TUMEROOSA
        pygame.draw.circle(ekraan,v�rv,(400,300),raadius,2)
    pygame.draw.rect(ekraan,TUMEROHELINE,(390,300,20,200))

def joonista_tekst():
    tekst=font.render("Tere tulemast!",True,VALGE)
    ekraan.blit(tekst,(300,50))

while True:
    for s�ndmus in pygame.event.get():
        if s�ndmus.type==pygame.QUIT:
            pygame.quit()
            sys.exit()

    ekraan.fill(SININE)
    pygame.draw.rect(ekraan,ROHELINE,(0,K�RGUS//2,LAIUS,K�RGUS//2))

    joonista_p�ike()
    joonista_pilv()
    joonista_lill()
    joonista_tekst()

    ekraan.blit(bee_image,(340,100))

    pygame.display.flip()
