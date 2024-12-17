import pgzrun
import random
import time

WIDTH = 800
HEIGHT = 600

satellites = []

lines = []

next_satellite = 0
num_of_satellites = 8

def create_satellites():
    for i in range(0,num_of_satellites):
        satellite = Actor("satellite")
        satellite.pos = random.randint(40,WIDTH-40),random.randint(40,HEIGHT-40)
        satellites.append(satellite)
        
def draw():
    screen.blit("bg_sat",(0,0))
    number = 1
    for i in satellites:
        screen.draw.text(str(number),(i.pos[0],i.pos[1]+20))
        i.draw()
        number = number + 1
    for j in lines:    
        screen.draw.line(j[0],j[1],(255,255,255))
        
def on_mouse_down(pos):
    global next_satellite,lines
    if next_satellite < num_of_satellites:
        if satellites[next_satellite].collidepoint(pos):
            if next_satellite:
                lines.append((satellites[next_satellite-1].pos,satellites[next_satellite].pos))
                
            next_satellite = next_satellite + 1



 
 
 
        
create_satellites()        

pgzrun.go()    