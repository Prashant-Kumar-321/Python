import keyboard

def on_shortcut(): 
    print("ctrl+shift+p was pressed") 

keyboard.add_hotkey("Ctrl+Shift+P", on_shortcut) 

keyboard.wait('ESC') 