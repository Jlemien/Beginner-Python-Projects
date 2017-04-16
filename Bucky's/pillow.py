from PIL import Image
from PIL import ImageFilter

baby = Image.open("JosephNewYork.jpg")
blur = baby.filter(ImageFilter.BLUR)
detail = baby.filter(ImageFilter.DETAIL)
edges = baby.filter(ImageFilter.FIND_EDGES)
edges.show()

#square_baby = baby.resize((250, 250))
#flip_baby = baby.transpose(Image.FLIP_TOP_BOTTOM)
#spin_baby = baby.transpose(Image.ROTATE_90)
#black_white = baby.convert("L")
#spin_baby.show()

#sister = Image.open("JosephNewYork.jpg")
#bucky = Image.open("LindaNassau.jpg")
#r1, g1, b1 = sister.split()
#r2, g2, b2 = bucky.split()
#r.show()
#g.show()
#b.show()
#new_img = Image.merge("RGB", (r2, g1, b2))
#new_img.show()


#sister = Image.open("JosephNewYork.jpg")
#girl = Image.open("LindaNassau.jpg")
#area = (100,100,1060,1380)
#sister.paste(girl,area)
#sister.show()


#img = Image.open("JosephNewYork.jpg")
#print(img.format)
#print(img.size)
#area = (100, 100, 300, 375)
#new_image = img.crop(area)
#new_image.show()
