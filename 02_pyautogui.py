import pyautogui
import time

# Mover o mouse para a posição (100, 100) em 1 segundo
pyautogui.moveTo(100, 100, duration=1)

# Clicar na posição atual
pyautogui.click()

# Escrever texto
pyautogui.write("Olá mundo!", interval=0.1)
