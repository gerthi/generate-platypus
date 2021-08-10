# Built with python 3, dependencies installed with pip
# library to generate images - Pillow
# https://pillow.readthedocs.io/en/stable/installation.html
from PIL import Image

# library to work with arrays
# https://numpy.org/
import numpy as np

# library to interact with the operating system
import os

# library to generate random integer values
from random import seed
from random import randint

# library to manipulate colors
import colormath
from colormath.color_conversions import convert_color
from colormath.color_diff import delta_e_cie1976


# library to match RGB values to the nearest named color
import webcolors
# lor color matching
from webcolors import CSS3_HEX_TO_NAMES


# gets path to be used in image creation mechanism, using os
dirname = os.path.dirname(__file__)

# sets final image dimensions as 480x480 pixels
# the original 24x24 pixel image will be expanded to these dimensions
dimensions = 480, 480


def closest_colour(requested_colour):
    min_colours = {}
    for key, name in webcolors.CSS3_HEX_TO_NAMES.items():
        r_c, g_c, b_c = webcolors.hex_to_rgb(key)
        rd = (r_c - requested_colour[0]) ** 2
        gd = (g_c - requested_colour[1]) ** 2
        bd = (b_c - requested_colour[2]) ** 2
        min_colours[(rd + gd + bd)] = name
    return min_colours[min(min_colours.keys())]
            
def get_colour_name(requested_colour):
    try:
        closest_name = webcolors.rgb_to_name(requested_colour)
    except ValueError:
        closest_name = closest_colour(requested_colour)
    return closest_name


collection = []


for x in range(0, 4):

    # using ETH block number as starting random number seed
    b=11981207
    seed(x+b)

    delta_bo = 10
    delta_be = 10
    delta_h = 10

    # background color
    bg = (randint(0, 255), randint(0, 255), randint(0, 255))
    
    # background color converted
    bg_color = convert_color(colormath.color_objects.sRGBColor(bg[0], bg[1], bg[2], is_upscaled=True), colormath.color_objects.LabColor)
    bg_closest_name = get_colour_name(bg)

    while delta_bo <= 100 and delta_be <= 100:
        delta_bo = 10
        delta_be = 10
        # body color
        bo = (randint(0, 220), randint(0, 220), randint(0, 220))
        # beak color
        be = (255, 167, 78)
        # body & beak colors converted
        bo_color = convert_color(colormath.color_objects.sRGBColor(bo[0], bo[1], bo[2], is_upscaled=True), colormath.color_objects.LabColor)
        be_color = convert_color(colormath.color_objects.sRGBColor(be[0], be[1], be[2], is_upscaled=True), colormath.color_objects.LabColor)
        # if body color is too close to background color or beak color, regenerate
        delta_bo = delta_e_cie1976(bg_color, bo_color)
        delta_be = delta_e_cie1976(bg_color, be_color)
    

    bo_closest_name = get_colour_name(bo)

    # generating another random seed
    c=randint(0,500)
    seed(c)

    # belly color - lighter body color
    sh = ((bo[0]+30), (bo[1]+30), (bo[2]+30))

    # generating another random seed
    d = randint(0,100)
    seed(d)

    # eye "white" color
    # if random number between 1-100 is 5 or less - Crazy Eyes!
    if d > 5:
        # normal eyes are always the same color
        ey = (240,248,255)
        ei = (0, 0, 0)
    else:
        # crazy eyes have the same (154, 0, 0) pupil and a random 'eye white' color
        ei = (randint(0, 256), randint(0, 256), randint(0, 256))
        ey = (154, 0, 0)
    ei_closest_name = get_colour_name(ei)


    # generating another random seed
    e = randint(0,1000)
    seed(e)

    # beak color
    f = randint(0, 1000)
    if f > 47:
        # if random number is 20-100 >> orange beak
        be = (255, 167, 78)
    elif 47 >= f > 5:
        # 48-500 >> white beak
        be = (250, 250, 250)
        ei = (0,0,0)
        ey = (1, 239, 255)
    else:
        # random number is 5 or less >> black beak
        be = (0, 0, 51)
    be_closest_name = get_colour_name(be)

    # outline color
    ol = (0, 0, 0)

    # hair color
    ha = (0, 0, 0)

    # hat colors
    while delta_h <= 100:
        h2 = (randint(0, 220), randint(0, 220), randint(0, 220))
        hat_color = convert_color(colormath.color_objects.sRGBColor(h2[0], h2[1], h2[2], is_upscaled=True), colormath.color_objects.LabColor)
        delta_h = delta_e_cie1976(hat_color, bo_color)
    
    hat_closest_name = get_colour_name(h2)

    h3 = ((h2[0]+30), (h2[1]+30), (h2[2]+30))

    ni = (255, 0, 0) # ninja 
    go = (255, 240, 16) # gold chain
    hc = (121, 66, 12) # adventurer hat
    cl = (192, 192, 192) # clope
    ce = (106, 21, 21) # clope
    hb = (0, 0, 0) # adventurer black


    hair = [
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg],
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg],
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg],
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg],
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,ha,bg,ha,bg,bg,bg,bg,bg,bg,bg,bg],
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,ha,ha,bg,bg,bg,bg,bg,bg,bg,bg,bg],
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bo,bo,bo,bo,bo,bo,bg,bg,bg,bg,bg,bg,bg],
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bo,bo,bo,bo,bo,bo,bo,bo,bg,bg,bg,bg,bg,bg],
    ]

    eyes = [
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bo,bo,bo,bo,bo,bo,bo,bo,bg,bg,bg,bg,bg,bg],
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bo,bo,ey,ey,bo,ey,ey,bo,bg,bg,bg,bg,bg,bg],
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bo,bo,ey,ei,bo,ey,ei,bo,bg,bg,bg,bg,bg,bg],
        [bg,bg,bg,bg,bg,be,be,be,bg,bg,bo,bo,bo,be,be,be,bo,bo,bg,bg,bg,bg,bg,bg],
    ]

    mouth = [
        [bg,bg,bg,bg,be,be,be,be,bg,bg,bo,bo,bo,be,be,be,be,be,be,be,bg,bg,bg,bg],
        [bg,bg,bg,bg,be,be,be,be,be,bg,bo,bo,be,be,be,be,be,be,be,be,bg,bg,bg,bg],
    ]

    body = [
        [bg,bg,bg,bg,be,be,be,be,be,bo,bo,bo,bo,bo,bo,bo,bg,bg,bg,bg,bg,bg,bg,bg],
        [bg,bg,bg,bg,bg,be,be,be,bo,be,bo,sh,sh,sh,sh,bo,bo,bg,bg,bg,bg,bg,bg,bg],
        [bg,bg,bg,bg,bg,bg,be,be,bo,be,bo,sh,sh,sh,sh,bo,bo,bo,bg,bg,bg,bg,bg,bg],
        [bg,bg,bg,bg,bg,bg,bg,be,be,bo,bo,sh,sh,sh,sh,bo,bg,bo,bg,bg,bg,bg,bg,bg],
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,be,bo,bo,sh,sh,bo,bo,bg,bg,bg,bg,bg,bg,bg,bg],
    ]

    bottom = [
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bo,bo,bo,bo,bo,bo,bo,bo,bg,bg,bg,bg,bg,bg,bg],
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bo,bo,bg,bg,bg,bg,bo,bo,bg,bg,bg,bg,bg,bg,bg],
        [bg,bg,bg,bg,bg,bg,bg,bg,be,be,be,bg,bg,bg,bg,be,be,be,bg,bg,bg,bg,bg,bg],
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg],
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg]
    ]

    casquette = [
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg],
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg],
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg],
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,h2,h2,h2,bg,bg,bg,bg,bg,bg,bg,bg,bg],
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,h2,h2,h2,h3,h2,h2,bg,bg,bg,bg,bg,bg,bg],
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,h2,h2,h2,h2,h2,h3,h2,bg,bg,bg,bg,bg,bg,bg],
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,h2,h2,h2,h2,h2,h2,h2,h2,h2,h2,bg,bg,bg,bg],
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bo,bo,bo,bo,bo,bo,bo,bo,bg,bg,bg,bg,bg,bg],
    ]

    rev_casquette = [
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg],
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg],
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg],
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,h2,h2,h2,bg,bg,bg,bg,bg,bg,bg,bg],
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,h2,h2,h2,h2,h3,h2,bg,bg,bg,bg,bg,bg,bg],
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,h2,h2,h2,h2,h2,h3,h2,bg,bg,bg,bg,bg,bg],
        [bg,bg,bg,bg,bg,bg,bg,bg,h2,h2,h2,h2,h2,h2,h2,h2,h2,h2,bg,bg,bg,bg,bg,bg],
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bo,bo,bo,bo,bo,bo,bo,bo,bg,bg,bg,bg,bg,bg],
    ]

    ninja = [
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg],
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg],
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg],
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg],
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,ol,bg,ol,bg,bg,bg,bg,bg,bg,bg,bg],
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,ol,ol,bg,bg,bg,bg,bg,bg,bg,bg,bg],
        [bg,bg,bg,bg,bg,bg,bg,bg,ni,bg,bg,bo,bo,bo,bo,bo,bo,bg,bg,bg,bg,bg,bg,bg],
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,ni,ni,ni,ni,ni,ni,ni,ni,ni,bg,bg,bg,bg,bg,bg],
    ]

    adventurer = [
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg],
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg],
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg],
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,hc,hc,hc,hc,hc,bg,bg,bg,bg,bg,bg,bg,bg],
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,hc,hc,hc,hc,hc,hc,hc,bg,bg,bg,bg,bg,bg,bg],
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,hc,hb,hb,hb,hb,hb,hb,bg,bg,bg,bg,bg,bg,bg],
        [bg,bg,bg,bg,bg,bg,bg,bg,hc,hc,hc,hc,hc,hc,hc,hc,hc,hc,hc,bg,bg,bg,bg,bg],
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,hc,hc,bo,bo,bo,bo,bo,bo,bo,bg,bg,bg,bg,bg,bg],
    ]

    sunglasses = [
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bo,bo,ol,ol,bo,ol,ol,bo,bg,bg,bg,bg,bg,bg],
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,ol,ol,ol,ol,ol,ol,ol,ol,bg,bg,bg,bg,bg,bg],
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bo,bo,ol,ol,be,ol,ol,bo,bg,bg,bg,bg,bg,bg],
        [bg,bg,bg,bg,bg,be,be,be,bg,bg,bo,bo,bo,be,be,be,bo,bo,bg,bg,bg,bg,bg,bg],
    ]

    cigarette = [
        [bg,bg,bg,bg,be,be,be,be,bg,bg,bo,bo,bo,be,be,be,be,be,be,be,bg,bg,bg,bg],
        [bg,bg,bg,bg,be,be,be,be,be,bg,bo,bo,be,be,be,be,be,be,be,cl,cl,cl,ce,bg],
    ]

    gold_chain = [
        [bg,bg,bg,bg,be,be,be,be,be,bo,bo,go,bo,bo,bo,bo,go,bg,bg,bg,bg,bg,bg,bg],
        [bg,bg,bg,bg,bg,be,be,be,bo,be,bo,sh,go,sh,sh,go,bo,bg,bg,bg,bg,bg,bg,bg],
        [bg,bg,bg,bg,bg,bg,be,be,bo,be,bo,sh,sh,go,go,bo,bo,bo,bg,bg,bg,bg,bg,bg],
        [bg,bg,bg,bg,bg,bg,bg,be,be,bo,bo,sh,sh,go,go,bo,bg,bo,bg,bg,bg,bg,bg,bg],
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,be,bo,bo,sh,sh,bo,bo,bg,bg,bg,bg,bg,bg,bg,bg],
    ]


    ## ACCESSORIES 

    # hat variation
    h = randint(0,100)
    seed(h)

    if h > 35:
        hat = casquette
        hat_type = 'casquette'
    elif 35 >= h > 15:
        hat = rev_casquette
        hat_type = 'reversal casquette'
    elif 5 >= h > 1:
        hat = ninja
        hat_type = 'ninja'
    elif h == 1:
        hat = adventurer
        hat_type = 'adventurer'
    else:
        hat = hair
        hat_type = 'none'

    # sunglasses
    i = randint(0, 100)
    if i > 20:
        eyes = eyes
        glasses = 'none'
    else:
        eyes = sunglasses
        glasses = 'sunglasses'

    # mouth
    j = randint(0, 100)
    if j > 15:
        mouth = mouth
        mouth_type = 'none'
    else: 
        mouth = cigarette
        mouth_type = 'cigarette'

    # neck
    k = randint(0, 100)
    if k > 5:
        body = body
        body_decoration = 'none'
    else: 
        body = gold_chain
        body_decoration = 'gold chain'


    pixels = hat + eyes + mouth + body + bottom
    
    attributes = {
        'body_color': bo_closest_name,
        'eye_color': ei_closest_name,
        'beak_color': be_closest_name,
        'background': bg_closest_name,
        'hat': hat_type,
        'hat_color': hat_closest_name,
        'glasses': glasses,
        'mouth': mouth_type,
        'body_decoration': body_decoration,
    }

    if attributes not in collection:
        # convert the pixels into an array using numpy
        array = np.array(pixels, dtype=np.uint8)

        # use PIL to create an image from the new array of pixels
        new_image = Image.fromarray(array)
        new_image = new_image.resize(dimensions, resample=0)
        imgname = dirname + '/platypus_images/' + 'Platypus_Erectus_' + (str(x)) + '.png'
        new_image.save(imgname)
