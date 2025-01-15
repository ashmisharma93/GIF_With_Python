import imageio.v3 as iio
from PIL import Image

#Chill Cat

cat1 = Image.open('chill_cat.jpg')
cat2 = Image.open('chill_cat_side.jpg')
cat3 = Image.open('chill_cat_shushing.jpg')
cat4 = Image.open('chill_cat_pointing.jpg')
cat5 = Image.open('cat_with_fire.jpg')

size = (500,500)
cat1_resized = cat1.resize(size)
cat2_resized = cat2.resize(size)
cat3_resized = cat3.resize(size)
cat4_resized = cat4.resize(size)
cat5_resized = cat5.resize(size)

cat1_resized.save("cat1_resized.jpg")
cat2_resized.save("cat2_resized.jpg")
cat3_resized.save("cat3_resized.jpg")
cat4_resized.save("cat4_resized.jpg")
cat5_resized.save("cat5_resized.jpg")

filename = ['cat1_resized.jpg','cat2_resized.jpg','cat3_resized.jpg','cat4_resized.jpg','cat5_resized.jpg']
images= []

for i in filename:
    images.append(iio.imread(i))

iio.imwrite('cat_gif.gif',images, duration = 2000, loop=0)
