from PIL import Image, ImageFont, ImageDraw
import sys
# These files must exist in the working directory:
# townshipmap_compressed.PNG, Aileron-Regular.otf

PATH = sys.path[0] + '/'

def generate(datetime, overlay):
    sgmap = Image.open(PATH + 'townshipmap_compressed.PNG')
    overlay = Image.open(overlay)
    legend = Image.open(PATH + 'legend.png')
    
    overlay_pao = overlay.load()
    for x in range(overlay.size[0]):
        for y in range(overlay.size[1]):
            overlay_pao[x, y] = (
                    overlay_pao[x, y][0],
                    overlay_pao[x, y][1],
                    overlay_pao[x, y][2],
                    int(overlay_pao[x, y][3] / 2))

    overlay = overlay.resize((sgmap.size[0], sgmap.size[1]), Image.ANTIALIAS)
    sgmap.paste(overlay, (0, 0), overlay)

    sgmap.paste(legend, (1050, 750))

    font = ImageFont.truetype(font=PATH + 'Aileron-Regular.otf', size=30)
    draw_image = ImageDraw.Draw(sgmap)
    draw_image.text((20, 20), datetime, font=font, fill=(0, 0, 0, 255))

    sgmap.save(PATH + 'overlaid_map.png', optimise=True, quality=95)
