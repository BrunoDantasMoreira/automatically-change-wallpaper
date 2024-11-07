import save_frame as sf
import change_background as cb
import sys 
import time

prints_file_path = r'../output/prints.txt'
base_path = r'../output/data'
status = r'../assets/current.txt'

with open(prints_file_path, 'r') as txt:
    prints = txt.readlines()
with open(status, 'r') as txt:
    chosen_frame = int(txt.read())
img = fr"{prints[chosen_frame].strip()}"


def show_intro():
    print("-" * 60)
    print("      Video Wallpaper CLI Tool      ")
    print("-" * 60)
    print("Welcome! This program allows you to:")
    print("1. Capture frames from a video and save them as images.")
    print("2. Set your wallpaper to a frame from a video sequence.")
    print("Enjoy creating unique wallpapers from any video of your choice!")
    print("-" * 60)
    time.sleep(2)  # Wait 2 seconds before showing the menu

def capture_frames(video_path, interval):
    print(f"Capturing frames from {video_path} every {interval} frames...")
    default_video = r'../assets/Arcane Season 2 .mp4'
    sf.screenshot(video_path)

while True:

    if len(sys.argv) > 1:
        if sys.argv[1].lower() == 'next':
            chosen_frame += 1
            cb.set_wallpaper(str(img))
            with open(r'D:\Codes\Python\automatically-change-wallpaper\current.txt', 'w') as txt:
                txt.write(str(chosen_frame))
            break

    show_intro()
    print("-" * 60)
    print("           MAIN MENU           ")
    print("-" * 60)
    print("1 - Capture frames from video")
    print("2 - Change wallpaper to next frame")
    print("3 - Exit")
    print("-" * 60)
    
    choice = input("Your option: ")

    if choice == "1":
        video_path = input("Enter the path to the video file: ")
        interval  = int(input("Enter frame interval (in sec): [default 3] "))
        capture_frames(fr'{video_path}', interval)

    elif choice == "2":
        chosen_frame += 1
        cb.set_wallpaper(str(img))
        with open(r'D:\Codes\Python\automatically-change-wallpaper\current.txt', 'w') as txt:
            txt.write(str(chosen_frame))
        input("Wallpaper changed. Press Enter to continue...")

    elif choice == "3":
        print("Exiting...")
        time.sleep(1)
        break

    else:
        print("Invalid option. Please try again.")
        time.sleep(1)

    


