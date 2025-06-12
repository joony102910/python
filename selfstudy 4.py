from tkinter import *
from tkinter import messagebox

def keyEvent(event):
    shift_pressed = event.state & 0x0001 
    keycode = event.keycode

    direction = ""
    if shift_pressed:
        if keycode == 37:
            direction = "왼쪽 화살표"
        elif keycode == 38:
            direction = "위쪽 화살표"
        elif keycode == 39:
            direction = "오른쪽 화살표"
        elif keycode == 40:
            direction = "아래쪽 화살표"
        
        if direction:
            messagebox.showinfo("키보드 이벤트", f"눌린 키: Shift + {direction}")
        else:
            messagebox.showinfo("키보드 이벤트", "Shift + 방향키 외의 키")
    else:
        messagebox.showinfo("키보드 이벤트", "눌린 키: " + chr(event.keycode))

window = Tk()
window.bind("<Key>", keyEvent)
window.mainloop()
