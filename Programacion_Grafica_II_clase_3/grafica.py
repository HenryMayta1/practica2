from vpython import *
import asyncio

scene = canvas(title="Cilindros y Conos en VPython", width=800, height=600)


cono1 = cone(pos=vector(-3, 0, 0), axis=vector(0, 1.4, 0), radius=0.6, color=color.yellow)
cono2 = cone(pos=vector(-2, 0, 0), axis=vector(0, 1.2, 0), radius=0.6, color=color.yellow)
cono3 = cone(pos=vector(-1, 0, 0), axis=vector(0, 1, 0), radius=0.6, color=color.yellow)

cono4 = cone(pos=vector(-3, 0, 0), axis=vector(0, 1.4, 0), radius=0.6, color=color.purple)

cilindro1 = cylinder(pos=vector(0, 0, 0), axis=vector(0, 1, 0), radius=0.4, color=color.yellow)

cilindros = []
for i in range(5):
    radio = 0.5 - (i * 0.1)
    cilindro = cylinder(pos=vector(0, i * 1.4, 0), axis=vector(0, 1, 0), radius=radio, color=color.purple)
    cilindros.append(cilindro)


colores = [color.red, color.green, color.blue, color.yellow, color.cyan, color.magenta, color.orange, color.purple, color.white, color.black]
color_index_cono = 0
color_index_cilindro = 1

def reiniciar_posiciones(evt):
    global color_index_cono, color_index_cilindro
    if evt.key == 'c' or evt.key == 'C':  
        cono4.pos = vector(-3, 0, 0)
        cilindro1.pos = vector(0, 0, 0)  
    if evt.key == 'r' or evt.key == 'R':  
      
        cono4.color = colores[color_index_cono]
        cilindro1.color = colores[color_index_cilindro]
        
        color_index_cono = (color_index_cono + 1) % len(colores)
        color_index_cilindro = (color_index_cilindro + 1) % len(colores)

scene.bind('keydown', reiniciar_posiciones)

async def mover_objetos():
    while True:
    
        cono4.pos.x += 0.1
        cilindro1.pos.x += 0.1

        if cono4.pos.x > 6:
            cono4.pos.x = -3 
        if cilindro1.pos.x > 6:
            cilindro1.pos.x = 0
        
        await asyncio.sleep(0.1)

async def main():
    await mover_objetos()

asyncio.run(main())
