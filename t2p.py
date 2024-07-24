import csv
from PIL import Image, ImageDraw, ImageFont


def steam2image():
    """
    从CSV文件读取文本并将其添加到图片上。


    """
    # 加载图片
    image = Image.open('steambg.png')
    draw = ImageDraw.Draw(image)

    # 使用Pillow默认字体
    font70 = ImageFont.truetype('方正像素12.TTF', 65)
    font55 = ImageFont.truetype('DejaVuSerif-Bold.ttf', 55)
    font50 = ImageFont.truetype('DejaVuSerif-Bold.ttf', 50)
    font40 = ImageFont.truetype('DejaVuSerif.ttf', 40)
    font30 = ImageFont.truetype('方正像素12.TTF', 35)

    # 读取CSV文件并在图片上添加文本
    with open("SteamDsc.csv", newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile)
        i = 0
        for row in csvreader:
            game, tag, price, price_1, discount = row[0], row[1], row[2].strip(), row[3].strip(), row[4]
            if len(game) > 25:
                game = game[:25]+'...'
            draw.text((80, 80+i), f'{game}', font=font70, fill=(195, 206, 227), font_size=200)
            draw.text((80, 160+i), f'{tag}', font=font30, fill=(195, 206, 227), font_size=150)
            draw.text((80, 220+i), f'{price}', font=font40, fill=(169, 72, 44), font_size=150)
            draw.text((350, 210+i), f'{price_1}', font=font55, fill=(98, 151, 85), font_size=150)
            draw.text((750, 210+i), f'{discount}', font=font55, fill=(181, 189, 104), font_size=150)
            i += 235

    # 保存图片
    image.save('/tmp/steamdata.png')


# 示例用法


