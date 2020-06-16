from image_utils import *
from k_means import *

if __name__ == "__main__":
    file = input("image file> ")

    image = read_ppm(file)

    k=int(input("How many colors would you like to have in your image> "))

    output_name = input("name of output file> ")

    save_ppm(output_name + ".ppm", un_pack_image(image,k))

#images/image.ppm