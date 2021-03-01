# coding=UTF8
# width - это длина а len - ширина
def clear():
    global WindowWidth
    global WindowLen
    screen.fill((255, 255, 255))
    for i in range(20, WindowWidth * 20, 20):
        pygame.draw.line(screen, (200, 200, 200), (i, 0), (i, WindowLen * 20))
    for i in range(20, WindowLen * 20, 20):
        pygame.draw.line(screen, (200, 200, 200), (0, i), (WindowWidth * 20, i))


def info():
    messagebox.showinfo("Информация", "Левая кнопка мыши - рисование\nПравая кнопка мыши - заливка\nНажатие на колесико - взятие цвета\nS (Ы) - сохранение файла\nС - очищение экрана\nX (Ч) - выбор цвета\nПробел - эта справка")


import pygame
import time
import random
import tkinter
from tkinter import messagebox
from tkinter import simpledialog
from tkinter import colorchooser

pygame.init()
parent = tkinter.Tk()
A = simpledialog.askinteger(" ", "Введите ширину окна в клетках\n1 клетка - 20 пикселей")
if A == None:
    WindowWidth = 50
if A != None:
    WindowWidth = A
A = simpledialog.askinteger(" ", "Введите высоту окна в клетках\n1 клетка - 20 пикселей")
if A == None:
    WindowLen = 25
if A != None:
    WindowLen = A
screen = pygame.display.set_mode((WindowWidth * 20, WindowLen * 20))
clear()
SetedColorExist = False
info()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if SetedColorExist:
                    ActiveColor = SetColor
                    SetedColorExist = False
                else:
                    ActiveColor = (random.randint(20, 220), random.randint(20, 220), random.randint(20, 220))
                pygame.draw.rect(screen, ActiveColor, (event.pos[0] // 20 * 20, event.pos[1] // 20 * 20, 20, 20))
            if event.button == 3:
                if SetedColorExist:
                    ActiveColor = SetColor
                    SetedColorExist = False
                else:
                    ActiveColor = (random.randint(20, 220), random.randint(20, 220), random.randint(20, 220))
                pos = pygame.mouse.get_pos()
                ToAdd = [(pos[0] - 20, pos[1]), (pos[0] + 20, pos[1]), (pos[0], pos[1] - 20), (pos[0], pos[1] + 20)]
                Added = [1]
                StartColor = screen.get_at(pos)
                while len(Added) != 0:
                    Added = []
                    for poses in ToAdd:
                        if 0 < poses[0] < WindowWidth * 20 and 0 < poses[1] < WindowLen * 20:
                            if screen.get_at(poses) == StartColor:
                                Added.append(poses)
                                pygame.draw.rect(screen, ActiveColor, (poses[0] // 20 * 20, poses[1] // 20 * 20, 20, 20))
                    ToAdd = []
                    for p in Added:
                        ToAdd.append((p[0] - 20, p[1]))
                        ToAdd.append((p[0] + 20, p[1]))
                        ToAdd.append((p[0], p[1] - 20))
                        ToAdd.append((p[0], p[1] + 20))
            if event.button == 2:
                pos = pygame.mouse.get_pos()
                SetColor = screen.get_at(pos)
                SetedColorExist = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                info()
            if event.key == pygame.K_s:
                FileName = simpledialog.askstring(" ", "Введите имя файла")
                if FileName != None:
                    pygame.image.save(screen, FileName + ".png")
            if event.key == pygame.K_x:
                SetColor = colorchooser.askcolor()[0]
                SetedColorExist = True
            if event.key == pygame.K_c:
                clear()

    pressed = pygame.mouse.get_pressed()
    if pressed[0]:
        pygame.draw.rect(screen, ActiveColor, (pygame.mouse.get_pos()[0] // 20 * 20, pygame.mouse.get_pos()[1] // 20 * 20, 20, 20))
    pygame.display.update()
