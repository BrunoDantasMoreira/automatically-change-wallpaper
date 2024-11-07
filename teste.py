string = [r'C:\Users\Dell\Pictures\WallPapers\data\frame1608.jpg', 
          r'C:\Users\Dell\Pictures\WallPapers\data\frame1609.jpg']
          

with open('prints.txt', 'a') as txt:

  for c in string:
    txt.write(c + '\n')
