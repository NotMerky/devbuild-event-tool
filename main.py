import os
import hjson
import sys

def set_console_title():
    os.system("title Dev Build Event Tool by Merky")

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def pause_screen():
    os.system('pause' if os.name == 'nt' else 'Press Enter to continue...')

def get_file_path():
    try:
        dev_server_path = os.path.expandvars(r"%localappdata%\DBD.DevBuildLauncher\DevServerPath.sav")
        if not os.path.isfile(dev_server_path):
            print(f"Error: The DevServerPath.sav file does not exist at {dev_server_path}")
            return None
        with open(dev_server_path, "r") as file:
            dev_server_path_value = file.read().strip()
            return os.path.join(dev_server_path_value, "settings", "events.hjson")
    except Exception as e:
        print(f"Error reading DevServerPath.sav: {e}")
        return None

def get_user_choice(min_choice, max_choice):
    while True:
        try:
            choice = int(input("\nChoose An Option: "))
            if min_choice <= choice <= max_choice:
                return choice
            else:
                print("Invalid choice, please enter a number between", min_choice, "and", max_choice, ".")
        except ValueError:
            print("Invalid input, please enter a number.")

def display_active_event(data):
    active_event = next((event for event, status in data.items() if status), None)
    if active_event:
        print(f"Active Event: [{active_event}]")
    else:
        print("Active Event: [None]")

def display_event_options():
    print("\n[1] Enable \"Winter2017\" Event")
    print("[2] Enable \"Lunar\" Event")
    print("[3] Enable \"Summer\" Event")
    print("[4] Enable \"Halloween2018\" Event")
    print("[5] Enable \"Winter2018\" Event")
    print("[6] Enable \"Lunar2019\" Event")
    print("[7] Enable \"Anniversary2019\" Event")
    print("[8] Disable Event")
    print("[9] Quit Tool")

def activate_event(data, choice, file_path):
    for event in data:
        data[event] = False

    if choice < 8:
        event_list = list(data.keys())
        selected_event = event_list[choice - 1]
        data[selected_event] = True
        print(f"\nThe event '{selected_event}' has been enabled.")
    else:
        print("\nRestored Default Event Mode (All events disabled).")
    
    try:
        with open(file_path, "w") as file:
            hjson.dump(data, file)
        print(f"\nEvent Selection Updated Successfully.")
    except Exception as e:
        print(f"\nError writing to file: {e}")

def main():
    set_console_title()
    
    file_path = get_file_path()
    if not file_path:
        print("Error: This tool requires the Updated Developer Build Launcher by Smirkzzy to be setup. Exiting...")
        pause_screen()
        sys.exit()

    if not os.path.isfile(file_path):
        print(f"Error: The event file does not exist at {file_path}. Exiting.")
        sys.exit()

    try:
        with open(file_path, "r") as file:
            data = hjson.load(file)
    except Exception as e:
        print(f"Error reading events file: {e}")
        sys.exit()

    display_active_event(data)
    display_event_options()
    
    choice = get_user_choice(1, 9)
    
    if choice == 9:
        sys.exit()
    else:        
        activate_event(data, choice, file_path)
        pause_screen()
        clear_screen()

if __name__ == "__main__":
    while True:
        main()
