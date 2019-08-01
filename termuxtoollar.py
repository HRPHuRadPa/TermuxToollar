#Created by Hüseyin
import subprocess 
import os
import sys
charset="utf-8"

print("	   Termux İçin Oluşturuldu")
print("	        Hoşgeldiniz")
print("	   ")
print("	   --------------------------")
print("	   İnstagram : huseyin.138 - hrp_huradpa_")
print("	   WhatsApp Grubu : https://chat.whatsapp.com/Gb42jFj3R3K3aYvjsSKVMd")
print("	   --------------------------")
print("")
print("	[01] lootboty")
print("	[02] TBomb-SMS Bombası ")
print("	[03] TermuxArch ")
print("	[04] Bombers ")
print("	[05] Metasploit_Termux ")
print("	[06] Red_Hawk ")
print("	[07] SocialBox-Termux ")
print("	[08] Android_Aircrack ")
print("	[09] Android_Wireless_Tools ")
print("	[10] Android_Reaver_WPS ")
print("")
print("	[11] Programı Kapat ")



user_input = input("  Seçiniz :  ")

if user_input == "1" or user_input == "1":
	print("lootboty Hack Toolu Şuanki Konumunuza İndiriliyor...")
	subprocess.call(["git","clone","https://github.com/wi-fi-analyzer/lootboty.git"])

elif user_input == "2" or user_input == "2":
	print("TBomb Hack Toolu Şuanki Konumunuza İndiriliyor...")
	subprocess.call(["git","clone","https://github.com/TheSpeedX/TBomb.git"])

elif user_input == "3" or user_input == "03":
	print("TermuxArch Hack Toolu Şuanki Konumunuza İndiriliyor...")
	subprocess.call(["git","clone","https://github.com/SDRausty/TermuxArch.git"])

elif user_input == "4" or user_input == "04":
	print("Bomber Hack Toolu Şuanki Konumunuza İndiriliyor...")
	subprocess.call(["git","clone","https://github.com/bhattsameer/Bombers.git"])

elif user_input == "5" or user_input == "05":
	print("Metasploit_termux Hack Toolu Şuanki Konumunuza İndiriliyor...")
	subprocess.call(["git","clone","https://github.com/Hax4us/Metasploit_termux.git"])

elif user_input == "6" or user_input == "06":
	print("Red_Hawk Hack Toolu Şuanki Konumunuza İndiriliyor...")
	subprocess.call(["git","clone","https://github.com/Tuhinshubhra/RED_HAWK.git"])

elif user_input == "7" or user_input == "07":
	print("SocialBox-Termux Hack Toolu Şuanki Konumunuza İndiriliyor...")
	subprocess.call(["git","clone","https://github.com/samsesh/SocialBox-Termux.git"])

elif user_input == "8" or user_input == "08":
	print("Android_Aircrack Hack Toolu Şuanki Konumunuza İndiriliyor...")
	subprocess.call(["git","clone","https://github.com/kriswebdev/android_aircrack.git"])

elif user_input == "9" or user_input == "09":
	print("Android_Wireless_Tools Hack Toolu Şuanki Konumunuza İndiriliyor...")
	subprocess.call(["git","clone","https://github.com/kriswebdev/android_wireless_tools.git"])

elif user_input == "10":
	print("Android_Reaver-WPS Hack Toolu Şuanki Konumunuza İndiriliyor...")
	subprocess.call(["git","clone","https://github.com/kriswebdev/android_reaver-wps.git"])

elif user_input=="11":
	print(user_input,"Seçtiniz. Program Kapanıyor")
	sys.exit() 

else:
	print("Hatalı Giriş")
