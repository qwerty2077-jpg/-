import os
from PIL import Image
vk = (1400,1000)
instagram = (1080,1080)
facebook = (1200,628)
for number in range(5):
    file_path = f"photo_end_{number+1}"
    if not os.path.isdir(file_path):
        os.mkdir(file_path)
    image = Image.open(f'photo_{number+1}.jpg')
    image_vk = image.resize(vk)
    image_inst = image.resize(instagram)
    image_fb = image.resize(facebook)
    image_inst.crop((10,0, image_inst.width-10, image_inst.height))
    image_vk.save(f'{file_path}/image_vk.png','png')
    image_inst.save(f'{file_path}/image_inst.png','png')
    image_fb.save(f'{file_path}/image_fb.png','png')