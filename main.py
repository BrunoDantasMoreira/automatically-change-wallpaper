import save_frame as sf
import change_backgroud as cb
#import sys 

prints_file_path = r'D:\Codes\Python\automatically-change-wallpaper\prints.txt'

# Caminho base dos arquivos de imagem
base_path = r"C:\Users\Dell\Pictures\WallPapers\data\frame"

with open(r'D:\Codes\Python\automatically-change-wallpaper\current.txt', 'r') as txt:
    chosen_frame = int(txt.read())

#print(sys.argv)
#if len(sys.argv) > 1:
    #if sys.argv[1].lower() == 'next':
chosen_frame += 1
with open(r'D:\Codes\Python\automatically-change-wallpaper\current.txt', 'w') as txt:
    txt.write(str(chosen_frame))


with open(prints_file_path, 'r') as txt:
  prints = txt.readlines()

video = r'C:\Users\Dell\Videos\Arcane\ArcaneS1E2.mp4'
img = fr"{prints[chosen_frame].strip()}"

#prints = sf.screenshot(video)

cb.set_wallpaper(str(img))
