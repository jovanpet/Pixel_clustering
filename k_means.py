import random
import  math


def un_pack_image(image,k):
    """
        Changes the the original image to the ones assigned in the assignement list
        :param k: the number of colors in the photo
        :param image: The image data, should be a width x height list-of-lists with each element
                    being a 3-tuple of red,green,blue values each of which should be between 0 and 255.
        :return: image with changed tuples to the ones where pixels are clustering
        """
    mean, assigment= k_means(image,k)

    for x in range(len(assigment)):
        for y in range(len(assigment[0])):
            image[x][y]=mean[assigment[x][y]]
    return image

def k_means(image,k):
    """
        Writes an image in ppm format (specifically "plain" ppm format P3)
        :param k: the number of colors in the photo
        :param image: The image data, should be a width x height list-of-lists with each element
                    being a 3-tuple of red,green,blue values each of which should be between 0 and 255.
        :return: tuple of list of list assgment of assfned pixels and mean list of colors.
        """
    mean=inital_guess_means_list(k)
    assigment=intial_assigment(len(image), len(image[0]))

    for i in range(10): #I put here some adequit number of reaptes
        update_assigment(image,mean,assigment)
        update_means(image,assigment,mean)

    return (mean,assigment)

def inital_guess_means_list(k):
    """
            Creates a random list of colors for the initial mean lsit values
            :param k: the number of colors in the photo
            :return: list of random colors lenght k
            """
    mean=[]
    for i in range(k):
        mean.append((random.randint(0,255),random.randint(0,255),random.randint(0,255)))

    return mean

def update_assigment(image, mean, assignment):
    """
            Updates the assignement for the new values of mean lisr
            :param assignment- list of lists of assigned colors from mean
            :param mean- colors that the pixels are colustering to
            :param image: The image data, should be a width x height list-of-lists with each element
                        being a 3-tuple of red,green,blue values each of which should be between 0 and 255.
            :return:Nothing.
            """

    for i in range(len(image)):
        for j in range(len(image[0])):
            assignment[i][j] = label_color(image[i][j],mean)


def intial_assigment(width,height):
    """
              Creates an empty initial assigment list of lists
               :param width- width of the original image
               :param mean- height of the original image

               :return:assignment.
               """
    assignmetn=[]

    for columnNum in range(width):
        row = [0] * height
        assignmetn.append(row)

    return assignmetn


def update_means(image, assigment, mean):
    """
               Updates the assignement for the new values of mean lisr
               :param assignment- list of lists of assigned colors from mean
               :param mean- colors that the pixels are colustering to
               :param image: The image data, should be a width x height list-of-lists with each element
                           being a 3-tuple of red,green,blue values each of which should be between 0 and 255.
               :return:Nothing.
               """
    for i in range(len(mean)):
        list_color_label=[]
        for  x in range(len(assigment)):
            for y in range(len(assigment[0])):
                if assigment[x][y]==i:
                    list_color_label.append(image[x][y])
        mean[i]=avg_color_list(list_color_label)

def distance_between_color (color1,color2):
    """
               Comapraes how close/similar colors are
               :param color1- color 1 we are comparing
               :param color2- color 2 we are comparing

               :return:distance/siliarity of colors.
               """
    r1,g1,b1=color1
    r2,g2,b2=color2

    r = (r1 - r2) * (r1 - r2)
    g = (g1 - g2) * (g1 - g2)
    b = (b1 - b2) * (b1 - b2)

    distance= r + g + b

    return math.sqrt(distance)

def label_color(color,mean):
    """
                   Labels a color to the one it is closest too in the mean
                   :param color- color tuple
                   :param mean- list of colors we are looking accumulation arounf

                   :return: index of color in mean it is closest to.
                   """

    best=0
    best_distance=distance_between_color(color,mean[0])
    for i in range(1,len(mean)):
        if distance_between_color(color,mean[i]) < best_distance:
            best=i

    return best

def avg_color_list(list_color):
    """
                   Determerns the average color of list of colors
                   :param list_color: lsit of colors

                   :return:average of that list.
                   """
    r=0
    g=0
    b=0
    for r1,g1,b1 in list_color:
        r+=r1
        g+=g1
        b+=b1
    if r != 0:
        r = r/len(list_color)
    if g != 0:
        g = g / len(list_color)
    if b != 0:
        b = b / len(list_color)
    return (r,g,b)
