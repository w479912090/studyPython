from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random
def rndChar():
    return chr(random.randint(65, 90))
def rndColor():
    return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))
def rndColor1():
    return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))

width, height = 60*4, 60
image = Image.new('RGB', (width, height), (255, 255, 255))
font = ImageFont.truetype('arial.ttf', 36)
draw = ImageDraw.Draw(image)
for x in range(width):
    for y in range(height):
        draw.point((x, y), fill=rndColor())
for t in range(4):
    draw.text((60*t + 10, 10), rndChar(), font=font, fill=rndColor1())
image = image.filter(ImageFilter.BLUR)
image.save('code.jpg', 'jpeg')