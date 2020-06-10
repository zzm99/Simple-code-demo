#-*- coding: UTF-8 -*-  
 
import imageio
 
def create_gif(image_list, gif_name):
 
    frames = []
    for image_name in image_list:
        frames.append(imageio.imread(image_name))
    # Save them as frames into a gif 
    imageio.mimsave(gif_name, frames, 'GIF', duration = 0.1)
 
    return
 
def main():
    image_list = ['8-0.png', '8-2.png', '8-4.png', 
                  '8-6.png', '8-8.png', '8-10.png']
    gif_name = '88.gif'
    create_gif(image_list, gif_name)
 
if __name__ == "__main__":
    main()
