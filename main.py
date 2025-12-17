import pyautogui, pyperclip, random, time
print("tool spam 1.0")
msg = input("nhap tin nhan can spam: ").split("|")
n =  int(input("nhap so lan can spam: "))
m = float(input("nhap time delay: "))

print("chuan bi")
for i in range(5, 0, -1):
    print(i,end="...",flush= True )
print("batdau")    

for i in range(n):
    pyperclip.copy(random.choice(msg))
    pyautogui.hotkey("ctrl", "v")
    pyautogui.press("enter")
    time.sleep(m)
    
#hoan thanhtri 
