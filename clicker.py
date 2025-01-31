import pyautogui
import time
import keyboard
click_interval = 0.1
running = False
print("Нажите 'a' для запуска автокликера и 's' для остановки.")
while True:
    if running:
        pyautogui.click()
        time.sleep(click_interval)
    if keyboard.is_pressed('a'):
        running = True
    elif keyboard.is_pressed('s'):
        running = False
    elif keyboard.is_pressed('q'):
        print('Выход из программы')
        break