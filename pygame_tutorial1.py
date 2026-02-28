import random, pygame, sys, os, time 
from pygame.locals import *



class ScrollingBackground:
    def __init__(self, screenheight, imagefile):
        self.img=pygame.image.load(os.path.join("./",imagefile))
        self.coord=[0,0]
        self.coord2=[0, -screenheight]
        self.y_original=self.coord[1]
        self.y2_original=self.coord2[1]

    def Show(self, surface):
        surface.blit(self.img, self.coord)
        surface.blit(self.img, self.coord2)

    def UpdateCoords(self, speed_y, time1):
        distance_y=speed_y * time1
        self.coord[1]+=distance_y
        self.coord2[1]+=distance_y
        if self.coord2[1]>=0:
            self.coord[1]=self.y_original
            self.coord2[1]=self.y2_original

# Create player's spaceship
class playerspaceship(pygame.sprite.Sprite):
    def __init__(self, imagefile,centerx, bottom):
        super().__init__()
        self.img=pygame.image.load(os.path.join("./", imagefile))
        pygame.display.set_icon(self.img)
        self.img=pygame.transform.scale(self.img,(80,80))
        self.rect=self.img.get_rect(centerx=centerx, bottom=bottom)
        self.bulletfired=False
        self.updateFiredBulletText=False
    def Show(self, surface):
        surface.blit(self.img, self.rect)
    def Crash(self):
        objcrashed=Explosion(random.choice(list_of_explosion),self)
        objcrashed.Show()
        #pygame.mixer.Sound.play(explosion_sound2) #========== Temporary turn off
        self.kill()
    def FireBullet(self, list_of_bulletObj): 
        self.bulletfired=True
        self.updateFiredBulletText=True
        if bullets_allowed==0:
            pass
        elif bullets_allowed<=10:
            bulletObj=Bullet(self)
            list_of_bulletObj.add(bulletObj)
    

# Create asteroid in position X
class AsteroidXpos(pygame.sprite.Sprite):
        def __init__(self, imageasteroid):
            super().__init__()
            self.img=pygame.image.load(os.path.join("./", imageasteroid))
            self.img=pygame.transform.scale(self.img,(random.randint(50,90),random.randint(50,90)))
            self.rect=self.img.get_rect()
            self.rect.x=random.randint(0,400)
            self.rect.y=random.randint(-3500,-100)
            self.followtext=None  #--get amended
        def Show(self, surface):
            surface.blit(self.img, (self.rect))
        def UpdateCoords(self, speed, time1, paragetHit=False):
            getHitBefore=False
            distance=speed * time1
            self.rect.move_ip(0,distance)
            if self.rect.y>660:
                self.rect.x=random.randint(0, 480)
                self.rect.y=random.randint(-10,-2)
            if paragetHit:
                Value, getHitBefore=self.followtext.updateValue()
                print(Value, getHitBefore)
                paragetHit=False
            if getHitBefore:
                self.followtext=followText(self.img, self.rect, Value, getHitBefore)
                self.followtext.Show()
            else:
                self.followtext=followText(self.img, self.rect) #--get amended
                self.followtext.Show() #--get amended
        def Crash(self):
            objcrashed=Explosion(random.choice(list_of_explosion),self)
            objcrashed.Show()
            #pygame.mixer.Sound.play(explosion_sound1) #============ Temporary turn off
            self.kill()
        
            
               
# Create asteroid in position left Y
class AsteroidYleftpos(pygame.sprite.Sprite):
        def __init__(self, imageasteroid):
            super().__init__()
            self.img=pygame.image.load(os.path.join("./", imageasteroid))
            self.img=pygame.transform.scale(self.img,(random.randint(50,90),random.randint(50,90)))
            self.rect=self.img.get_rect()
            self.rect.x=random.randint(-1000,-120)
            self.rect.y=random.randint(5,510)
            self.followtext=None # --get amended
        def Show(self, surface):
            surface.blit(self.img, (self.rect))
        def UpdateCoords(self, speed, time1, paragetHit=False):
            getHitBefore=False
            distance=speed * time1
            self.rect.move_ip(distance,distance)
            if self.rect.x>480:
                self.rect.x=random.randint(-50,-20)
                self.rect.y=random.randint(5,790)
            if paragetHit:
                Value, getHitBefore=self.followtext.updateValue()
                print(Value, getHitBefore)
                paragetHit=False
            if getHitBefore:
                self.followtext=followText(self.img, self.rect, Value, getHitBefore)
                self.followtext.Show()
            else:
                self.followtext=followText(self.img, self.rect)
                self.followtext.Show()
        def Crash(self):
            objcrashed=Explosion(random.choice(list_of_explosion),self)
            objcrashed.Show()
            #pygame.mixer.Sound.play(explosion_sound1) #=========== Temporary turn off
            self.kill()
        
            
        
# Create asteroid in position right Y 
class AsteroidYrightpos(pygame.sprite.Sprite):
        def __init__(self, imageasteroid):
            super().__init__()
            self.img=pygame.image.load(os.path.join("./", imageasteroid))
            self.img=pygame.transform.scale(self.img,(random.randint(50,90),random.randint(50,90)))
            self.rect=self.img.get_rect()
            self.rect.x=random.randint(480,3480)
            self.rect.y=random.randint(5,510)
            self.followtext=None #--get amended
        def Show(self, surface):
            surface.blit(self.img, (self.rect))
        def UpdateCoords(self, speed, time1, paragetHit=False):
            getHitBefore=False
            distance=speed * time1
            self.rect.move_ip(-distance,-distance)
            if self.rect.x<-50:
                self.rect.x=random.randint(500,600)
                self.rect.y=random.randint(5,790)
            if paragetHit:
                Value, getHitBefore=self.followtext.updateValue()
                print(Value, getHitBefore)
                paragetHit=False
            if getHitBefore:
                self.followtext=followText(self.img, self.rect, Value, getHitBefore)
                self.followtext.Show()
            else:
                self.followtext=followText(self.img,self.rect)
                self.followtext.Show()
        def Crash(self):
            objcrashed=Explosion(random.choice(list_of_explosion),self)
            objcrashed.Show()
            #pygame.mixer.Sound.play(explosion_sound1) #========= Temporary turn off
            self.kill()
        
            
# Create explosion to be used by crashed objects        
class Explosion(pygame.sprite.Sprite):
    def __init__(self, imagexplosion, objCrashed):
        super().__init__()
        self.img=pygame.image.load(os.path.join("./", imagexplosion))
        self.img=pygame.transform.scale(self.img, (110, 110))
        self.rect=self.img.get_rect()
        self.rect.x=objCrashed.rect.x
        self.rect.y=objCrashed.rect.y
    def Show(self):
        screen.blit(self.img, (self.rect))

# Create bullet class for shooting asteroids    
class Bullet(pygame.sprite.Sprite):
    def __init__(self, ship):
        super().__init__()
        self.bullet_speed_factor=20
        self.bullet_width=3
        self.bullet_height=15
        self.bullet_color=(255,140,0)
        self.rect=pygame.Rect(0, 0, self.bullet_width, self.bullet_height)
        self.rect.centerx=ship.rect.centerx
        self.rect.top=ship.rect.top
        self.y=float(self.rect.y)
    def UpdateCoords(self):
        # Move bullet up
        self.y-=self.bullet_speed_factor
        self.rect.y=self.y
        if self.rect.bottom<0:
            self.kill()
    def Show(self, surface):
        pygame.draw.rect(surface, self.bullet_color, self.rect)
    def Crash(self):
        self.kill()
        
    def update_bullet(self, parabullets_allowed):
        global bullets_allowed
        if parabullets_allowed<10:
            parabullets_allowed+=1
            bullets_allowed=parabullets_allowed
            
    def bullet_fireout(self, parabullets_allowed):
        global bullets_allowed
        if parabullets_allowed>0:
            parabullets_allowed-=1
            bullets_allowed=parabullets_allowed
            
            
# Create follow number on the asteroid's body
class followText(pygame.sprite.Sprite):
    def __init__(self, targetImg, targetRect, value=0, gethitBefore=False):
        super().__init__()
        self.target=targetImg
        self.targetrect=targetRect
        self.value=value
        self.getHitBefore=gethitBefore
        if (self.target.get_width()*self.target.get_height())>=2500 and \
           (self.target.get_width()*self.target.get_height())<4600:
            if self.getHitBefore:
                self.value
                print(self.value)
            else:
                self.value=5
                
        elif (self.target.get_width()*self.target.get_height())>=4600 and \
             (self.target.get_width()*self.target.get_height())<=6400:
            if self.getHitBefore:
                self.value
                print(self.value)
            else:
                self.value=8
                
        elif (self.target.get_width()*self.target.get_height())>6400 and \
             (self.target.get_width()*self.target.get_height())<=8100:
            if self.getHitBefore:
                self.value
                print(self.value)
            else:
                self.value=10
                
            
    def updateValue(self):
        self.value-=1
        print(self.value)
        self.getHitBefore=True
        return (self.value, self.getHitBefore)

        
    def Show(self):
        pygame.font.init()
        font=pygame.font.SysFont('Comic San MS', 40)
        followtext=font.render(str(self.value), False, (255,0,0))
        followtextRect=followtext.get_rect()
        screen.blit(followtext,(self.targetrect.centerx-followtextRect.centerx, self.targetrect.centery-followtextRect.centery))
    
        
        
        
#------------Begin Settings---------------
pygame.init()

list_of_explosion=[]
list_of_explosion.append("explosion1.png")
list_of_explosion.append("explosion2.png")
list_of_explosion.append("explosion3.png")
bullets_allowed=10  

# Render sound effect
pygame.mixer.init()
pygame.mixer.music.load('bensound-scifi.wav') #===== Temporary turn off
pygame.mixer.music.play(-1, 0.0) #===== Temporary turn off
explosion_sound1=pygame.mixer.Sound('explosion-01.wav') #===== Temporary turn off
explosion_sound2=pygame.mixer.Sound('explosion-02.wav') #===== Temporary turn off

# Render text message
level=1
pygame.font.init()
crashedMsg=pygame.font.SysFont('Comic San MS', 70) # render crashed message
textsurface=crashedMsg.render("GAME OVER!!!", False, (255,0,0))
levelMsg=pygame.font.SysFont('Comic San MS', 40) # render level message
levelsurface=levelMsg.render("Level "+ str(level), False, (170,20,20))
levelsurface.set_alpha(197)



# Setting pygame screen
screenwidth, screenheight=(480,640)

keys=[False, False, False, False]
screen=pygame.display.set_mode((screenwidth, screenheight))
screenRect=screen.get_rect()
clock=pygame.time.Clock()
FPS=60
bg_speed=100

pygame.display.set_caption("Kuiper Belt Challenger")
StarField=ScrollingBackground(screenheight, "galaxy.jpg")

# Initialized asteroids group objects
list_of_Asteroidsprite=pygame.sprite.Group()
dictAsteroidCls={0:AsteroidXpos, 1:AsteroidYleftpos, 2:AsteroidYrightpos}
dictAsteroidpng={1:"asteroid1.png", 2:"asteroid2.png", 3:"asteroid3.png", 4:"asteroid4.png", 5:"asteroid5.png", 6: "asteroid6.png", 7: "asteroid7.png"}
for i in range(25):
    list_of_Asteroidsprite.add(dictAsteroidCls[random.choice(list(dictAsteroidCls.keys()))](dictAsteroidpng[random.choice(list(dictAsteroidpng.keys()))]))

# Initialized spaceship object
spaceRectcenterx=screenRect.centerx  # Set spaceship in initial position X center 
spaceRectbottom=screenRect.bottom-80 # Set spaceship in initial position bottom
spaceship=playerspaceship("spaceship.png", spaceRectcenterx, spaceRectbottom)
list_spaceshipsprite=pygame.sprite.Group()
list_spaceshipsprite.add(spaceship)
spaceships=list_spaceshipsprite.sprites()

# sprite.Group bullets   
list_of_bulletObj=pygame.sprite.Group()
loopbulletsprite=None

# load bullet image on screen
bulletbalance=0
bulletImg=pygame.image.load('Bullet.png') # load bullet image
bulletImg=pygame.transform.scale(bulletImg,(20,30))
bulletImg.set_alpha(197)
bulletBalance=pygame.font.SysFont('Comic San MS', 35) # render balance of bullet left

# Create custom event
UPDATE_BULLETS=pygame.USEREVENT+1
pygame.time.set_timer(UPDATE_BULLETS, 5000)

running=True
speedasteroid=1600

# ------------------ End Settings ----------------------

while running:
        clock.tick(FPS)
        bulletbalance=bullets_allowed
        bulletsurface=bulletBalance.render("x " + str(bulletbalance), False, (170,20,20))
        bulletsurface.set_alpha(197)
        time1=clock.tick(FPS)/speedasteroid
        StarField.UpdateCoords(bg_speed, time1)
        StarField.Show(screen)
        spaceships[0].Show(screen)
        
        if spaceships[0].bulletfired:
            for bulletsprite in list_of_bulletObj.sprites():
                bulletsprite.Show(screen)
                bulletsprite.UpdateCoords()
                loopbulletsprite=bulletsprite
                if spaceships[0].updateFiredBulletText:
                    bulletsprite.bullet_fireout(bullets_allowed)
                    spaceships[0].updateFiredBulletText=False
        if not loopbulletsprite is None:
            if loopbulletsprite.rect.bottom<0:
                loopbulletsprite.Crash()
                list_of_bulletObj.remove(loopbulletsprite)
        
                
        screen.blit(levelsurface, (5,5))
        screen.blit(bulletImg, (120,10))
        screen.blit(bulletsurface, (150, 10))
        for asteroidobj in list_of_Asteroidsprite.sprites():
            asteroidobj.Show(screen)
            asteroidobj.UpdateCoords(random.randint(50,500),time1)
            
            for i in list_of_Asteroidsprite.sprites():
                if not loopbulletsprite is None:
                    if i.rect.collidepoint(loopbulletsprite.rect.center):
                        if i.followtext.value==0:
                            list_of_Asteroidsprite.remove(i)
                            i.Crash()
                            loopbulletsprite.Crash()
                            list_of_bulletObj.remove(loopbulletsprite)
                            loopbulletsprite.rect.x=1000
                            loopbulletsprite.rect.y=1000
                        else:
                            loopbulletsprite.Crash()
                            list_of_bulletObj.remove(loopbulletsprite)
                            loopbulletsprite.rect.x=1000
                            loopbulletsprite.rect.y=1000
                            
                            i.UpdateCoords(random.randint(50,500), time1, True)
                            
                            
                        
                              
                if spaceships[0].rect.collidepoint(i.rect.center) or i.rect.collidepoint(spaceships[0].rect.center):
                      list_of_Asteroidsprite.remove(i)
                      spaceships[0].Crash()
                      i.Crash()
                      screen.blit(textsurface,(70,350))
                      pygame.mixer.music.stop()
                      running=False
                         
            
        for event in pygame.event.get():
                if event.type==QUIT:
                        pygame.quit()
                        sys.exit()
                # detecting if mouse was in motion
                elif event.type==pygame.MOUSEMOTION:
                        pygame.mouse.set_visible(1)
                        x,_=pygame.mouse.get_pos()
                        if x>screenwidth-80:
                                spaceships[0].rect.centerx=screenwidth-80
                        elif x<screenwidth:
                                spaceships[0].rect.centerx=x
                # detecting if keyboard keys were pressed
                elif event.type==pygame.KEYDOWN:
                        if event.key==pygame.K_UP:
                            keys[0]=True
                        elif event.key==pygame.K_LEFT:
                            keys[1]=True
                        elif event.key==pygame.K_DOWN:
                            keys[2]=True
                        elif event.key==pygame.K_RIGHT:
                            keys[3]=True
                        elif event.key==pygame.K_SPACE:
                            if not bullets_allowed==0:
                                spaceships[0].FireBullet(list_of_bulletObj)
                                
                            
                            
                            
                elif event.type==pygame.KEYUP:
                        if event.key==pygame.K_UP:
                                keys[0]=False
                        elif event.key==pygame.K_LEFT:
                                keys[1]=False
                        elif event.key==pygame.K_DOWN:
                                keys[2]=False
                        elif event.key==pygame.K_RIGHT:
                                keys[3]=False
                elif event.type==UPDATE_BULLETS:
                    if spaceships[0].bulletfired:
                        bulletsprite.update_bullet(bullets_allowed)
                    

        # Update keyboard key up - down position
        if keys[0]:
                if spaceships[0].rect.bottom>0:
                    spaceships[0].rect.bottom-=7
                    if spaceships[0].rect.top<0:
                        spaceships[0].rect.top=0
                               
        elif keys[2]:
                if spaceships[0].rect.bottom<screenheight: 
                    spaceships[0].rect.bottom+=7
                elif spaceships[0].rect.bottom>screenheight:
                    spaceships[0].rect.bottom=640
              

        # Update keyboard key left - right position
        if keys[1]:
                if spaceships[0].rect.centerx>0:
                        spaceships[0].rect.centerx-=7
                        if spaceships[0].rect.left<0:
                            spaceships[0].rect.left=0
                                        
        elif keys[3]:
                if spaceships[0].rect.right<screenwidth:
                        spaceships[0].rect.right+=7
                        if spaceships[0].rect.right>screenwidth+80:
                            spaceships[0].rect.right=screenwidth+80
   
        pygame.display.update()
