from PIL import Image
im = Image.open("/home/entong/Pictures/life.jpg")
im.rotate(180).show()
im.save("life123.jpg")