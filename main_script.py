import pyautogui
import numpy
import random
import time

voornaam = pyautogui.prompt('Wat is de voornaam van de student die je wilt blokkeren? ')
achternaam = pyautogui.prompt('Wat is de achternaam van de student die je wilt blokkeren? ')
school = pyautogui.prompt('Wat is de link van de Smartschool website van jou school? ')
conirmation = pyautogui.confirm('Ben je zeker dat je deze leerling wilt blokkeren? ')

while confirmation.lower() == 'ok':
    pyautogui.typewrite(['winleft'])
    time.sleep(0.1)
    pyautogui.typewrite('chrome', 0.1)
    time.sleep(0.1)
    pyautogui.typewrite(['enter'])
    time.sleep(0.5)
    pyautogui.typewrite(school, 0.01)
    time.sleep(0.2)
    pyautogui.typewrite(['enter'])
    time.sleep(3)
    antwoord = pyautogui.prompt('Staat Smartschool open? ')
    while antwoord.lower() == 'ja':
        pyautogui.typewrite(voornaam.lower(), 0.01)
        time.sleep(0.05)
        pyautogui.typewrite('.')
        time.sleep(0.05)
        pyautogui.typewrite(achternaam.lower(), 0.01)
        time.sleep(0.05)
        pyautogui.typewrite(['enter'])
        time.sleep(0.05)
        pyautogui.typewrite('qwertyuiop', 0.01)
        antwoord_2 = pyautogui.prompt('Staat de naam goed geschreven? ')
        while antwoord_2.lower():
            times = 0
            while (times <= 11):
                pyautogui.typewrite(['enter'])
                time.sleep(2.5)
             break
        break
    break
pyautogui.alert('Bye bye')
