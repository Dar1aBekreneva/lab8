def q1():
    from PIL import Image
    filename = "otkr.jpg"
    with Image.open(filename) as img:
        img.load()

    cropped_img = img.crop((200, 850, 500, 1050))
    cropped_img.save("cropp_otkr.jpg")
    cropped_img.show()

def q2():
    from PIL import Image
    d = {1: "ng.jpg", 2: "dr.jpg", 3: "may.jpg", 4: "apple.jpg"}
    print("1 - Новый год", "2 - День рождения", "3 - 1 мая", "4 - Яблочный спас")
    c = int(input("введите число - номер прадника: "))

    filename = d[c]
    with Image.open(filename) as img:
        img.load()
    img.show()

def q3():
    from PIL import Image, ImageDraw, ImageFont
    name = input("имя получателя: ")
    filename = "otkr.jpg"

    with Image.open(filename) as img:
        img.load()
    font = ImageFont.truetype("bahnschrift.ttf", 70)
    draw_text = ImageDraw.Draw(img)
    draw_text.text((img.width // 2 - 250, 20),name + ", поздравляю!",  font=font, fill=('#BE2738'))

    img.save(name + "otkr.png")
    img.show()

q1()
