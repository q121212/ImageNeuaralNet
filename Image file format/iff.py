#!/usr/bin/python
# -*- coding: utf-8 -*-
          
#my own image format file

# Чтобы наглядно можно было работать с нейронной сетью нужно уметь обрабатывать изображения. Но даже первое обращение к BMP, JPG, GIF, показывает, что хранение данных в этих форматах сделано непросто, или так описано, что понять это сложно. Чтобы нормально работать с ихображениями - попробую сам создать свой формат изображений (который в дальнейшем может быть) преобразован в формат медиа-файлов в целом.


# Model
# HEADER + Descriptions
# CONTAINER + Archivation

#Also - need have a viewer of my own image file format

# a simple ver - Contentent is array (list) of pixel +  their colors:
# a first variation is black\white variation. If Black is 1, White is 0 then image data is a simle array. but need define a width and height of Image: Its can be resolved via using nested array (array of arrays), the nested arrays is a horisontal lines in pictures
# image = \
# [[0,0,0,0,0,0,0,0,0,0],
# [0,0,0,0,0,0,0,0,0,0],
# [0,0,0,0,0,0,0,0,0,0],
# [1,1,1,1,1,1,1,1,1,1],
# [1,1,1,1,1,1,1,1,1,1],
# [1,1,1,1,1,1,1,1,1,1],
# [1,1,1,1,1,1,1,1,1,1],
# [0,0,0,0,0,0,0,0,0,0],
# [0,0,0,0,0,0,0,0,0,0],
# [0,0,0,0,0,0,0,0,0,0]]

# Lybraries import part
from tkinter import *

# a function do transponse from single-order list to double-order list
def transponse(data, width):
  count = 0
  new_data_line = []
  new_data = []
  for i in data:
    if count < width:
      new_data_line.append(int(i))
      count+=1
    else:
      new_data.append(new_data_line)
      new_data_line = []
      new_data_line.append(int(i))
      count=1
    
  new_data.append(new_data_line)
  return new_data

      
def openimagefile(filename, width):
  with open(filename, 'r') as f:
    data = f.read()


  data=data.split(',')
  new_data = transponse(data, width)
  print('A file: ' + filename + ' was opened.')
  print('Image width:  {0}, height: {1}'.format(width, str(len(new_data))))
  print('Image size: ' + str(len(data)))
  return new_data


def generate_empty_image(width, height):
  image = []
  for i in range(height):
    for j in range(width):
      image.append(0)
  
  data = image
  new_data = transponse(data, width)
  print('Image with demensions: {0} x {1} (width x height) was generated'.format(width, height))
  print('Image size: ' + str(len(image)))
  return new_data
  
def save_image(image, filename):
  with open(filename, 'w') as f:
    for i in range(len(image)):
      for j in range(len(image[i])):
        if i == len(image)-1 and j == len(image[i])-1:
          f.write(str(image[i][j]))
        else:
          f.write(str(image[i][j])+',')
  print('A file was written as: ' + filename)

def image_view(image):
  pass
  
  
def draw_image_file(filename, image_width, canvas_width = 500, canvas_height = 500):
  master = Tk()
  w = Canvas(master, 
             width=canvas_width, 
             height=canvas_height)
  w.pack()
  image = openimagefile(filename, image_width)
  for i in range(len(image)):
    for j in range(len(image[i])):
      if image[i][j] == 1:
        w.create_oval(j,i,j,i)
  mainloop()    

 
def main():
  openimagefile('image.txt', 10)
  save_image(generate_empty_image(50, 20), 'image2.txt')
  save_image(openimagefile('image2.txt', 50), 'image3.txt')
  draw_image_file('image4.txt', 500, 650, 650)

if __name__ == '__main__':
  main()