from PIL import Image


def get_image_resize(img, height_new):    
    width, height = img.size  # исходные размеры рисунка
    width_new = width // (height//height_new)
    img_new = img.resize((width_new, height_new), Image.ANTIALIAS)
    return img_new


symbols = ' .-:;+$#'  # тут добавить больше градаций яркости и подобрать свои символы
symbols = symbols[::-1]

name_image = 'ждун.jpeg'
img = Image.open(name_image)
img_new = get_image_resize(img, 50)  # привести к размеру 50 пикселей

print(img_new.size)
img_new.save('_' + name_image)


def get_image_symbols(symbols):
    count = len(symbols)
    full = 256 + 256 + 256  # максимальное значение
    segment = full // count  # длина сегмента

    result = ''
    width, height = img_new.size
    for y in range(height):
        for x in range(width):
            r, g, b = img_new.getpixel((x, y))
            color = r + g + b
            pos = color // segment
            result += symbols[pos] * 2
        result += '\n'
    return result


name_txt = name_image + '.txt'
f = open(name_txt, 'w')
f.write(get_image_symbols(symbols))
f.close()




def get_color_invert(color):
    '''
    инвертировать цвет пикселя
    '''
    r, g, b = color
    r = 255 - r
    g = 255 - g
    b = 255 - b
    return (r, g, b)


name_image = 'белка.jpg'
img = Image.open(name_image)
width, height = img.size

for y in range(height):
    for x in range(width):
        color = img.getpixel((x, y))
        img.putpixel((x, y), get_color_invert(color)) #инверт. цвета
img_new = get_image_resize(img, 50)
name_txt ='invert_color_' + name_image + '.txt'
f = open(name_txt, 'w')
f.write(get_image_symbols(symbols))
f.close()


name_image = 'белка.jpg'
img = Image.open(name_image)
img = img.transpose(Image.FLIP_LEFT_RIGHT) #инверт. лево-право
img_new = get_image_resize(img, 50)
name_txt ='FLIP_LEFT_RIGHT_' + name_image + '.txt'
f = open(name_txt, 'w')
f.write(get_image_symbols(symbols))
f.close()


name_image = 'белка.jpg'
img = Image.open(name_image)
img =  img.transpose(Image.FLIP_TOP_BOTTOM) #инверт. низ-верх
img_new = get_image_resize(img, 50)
name_txt ='FLIP_TOP_BOTTOM_' + name_image + '.txt'
f = open(name_txt, 'w')
f.write(get_image_symbols(symbols))
f.close()


