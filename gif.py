# GIF in Python
import imageio.v3 as iio
import os

filenames = ['dino1.png','dino2.png','dino3.png','dino4.png']
images = [iio.imread(filename) for filename in filenames ]

iio.imwrite('team.gif', images, duration = 500, loop = 0)

if os.path.exists("team.gif"):
    print("GIF created successfully: team.gif")