import pyautogui
import webbrowser
import time

message = input("Masukan Pesan Anda!! (Kosong = Kodingan ini akan disalin)  ")
repeats = int(input("Banyaknya pesan yang akan dikirim?  "))
delay = int(input("Jarak pengiriman pesan (dalam milliseconds) ?  "))

isLoaded = input("Tekan Enter untuk mengirim Pesan.")



print("You have five seconds to refocus the text input area of your messaging app")

time.sleep(5)


for i in range(0,repeats):         #Message sending loop
	if message != "":
		pyautogui.typewrite(message)     
		pyautogui.press("enter")
	else:
		pyautogui.hotkey('ctrl', 'v')      
		pyautogui.press("enter")

	time.sleep(delay/1000)


print("Done\n")