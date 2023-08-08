import PIL
from PIL import Image
import urllib.request
import io, sys, os, random
import tkinter as tk
from PIL import Image, ImageTk  # Place this at the end (to avoid any conflicts/errors)

def choose_random_means(k, img, pix):
    means = []
    for i in range(k):
        x = img.size[0]
        y = img.size[1]
        randx = random.randint(0, x-1)
        randy = random.randint(0, y-1)
        r = pix[randx, randy][0]
        g = pix[randx, randy][1]
        b = pix[randx, randy][2]
        tuple = (r,g,b)
        means.append(tuple)
    return means

# goal test: no hopping
def check_move_count(mc):
    for i in range(len(mc)):
        if mc[i] > 0:
            return False
    return True

# calculate distance with the current color with each mean
# return the index of means
def dist(col, means):
    minIndex, dist_sum = 0, 255**2+255**2+255**2
    indexCount = 0
    for meanTuple in means:
        d = (meanTuple[0]-col[0])*(meanTuple[0]-col[0]) + (meanTuple[1]-col[1])*(meanTuple[1]-col[1]) + (meanTuple[2]-col[2])*(meanTuple[2]-col[2])
        if d < dist_sum:
            dist_sum = d
            minIndex = indexCount
        indexCount+=1
    return minIndex 

def clustering(img, pix, cb, mc, means, count):
    temp_pb, temp_mc, temp_m = [[] for x in means], [], []
    temp_cb = [0 for x in means]
    x = img.size[0]
    y = img.size[1]
    # Puts each color in a bucket with the mean that it is closest to
    for i in range(x):
        for j in range(y):
            color = pix[i, j]
            minIndex = dist(color, means)
            curr_mean = temp_pb[minIndex]
            curr_mean.append(list(color))
            temp_cb[minIndex] = temp_cb[minIndex] + 1

    # Takes the average and rebuckets
    means = update_means(temp_pb, means)
    print("Meeeeans:", means)
    temp_m = means
    temp_mc = [ (a-b) for a, b in zip(temp_cb, cb)]
    print ('diff', count, ':', temp_mc)
    return temp_cb, temp_mc, temp_m

def update_means(oldBuckets, means):
    newMeans = []
    for i in range(len(means)):
        mean = means[i]
        points = oldBuckets[i]
        r = []
        g = []
        b = []
        for point in points:
            r.append(point[0])
            g.append(point[1])
            b.append(point[2])
        avgR = sum(r) // len(r)
        avgG = sum(g) // len(g)
        avgB = sum(b) // len(b)
        newMeans.append((avgR, avgG, avgB))
    return newMeans
    


def update_picture(img, pix, means):
    region_dict = {}
    x = img.size[0]
    y = img.size[1]
    for i in range(x):
        for j in range(y):
            color = pix[i, j]
            minIndex = dist(color, means)
            pix[i,j] = means[minIndex]
    return pix, region_dict
   
def distinct_pix_count(img, pix):
    cols = {}
    max_col, max_count = pix[0, 0], 0
    for x in range(img.size[0]):
        for y in range(img.size[1]):
            color = pix[x,y]
            if color in cols:
                cols[color] += 1
            else:
                cols[color] = 1
            if cols[color] > max_count:
                max_count = cols[color]
                max_col = color
    return len(cols.keys()), max_col, max_count

def count_regions(img, region_dict, pix, means):
   region_count = [0 for x in means]
   return region_count

 
def main():
    k = int(sys.argv[1])
    file = sys.argv[2]
    if not os.path.isfile(file):
        file = io.BytesIO(urllib.request.urlopen(file).read())

    window = tk.Tk() #create an window object

    img = Image.open(file)

    img_tk = ImageTk.PhotoImage(img)
    lbl = tk.Label(window, image = img_tk).pack()  # display the image at window

    pix = img.load()   # pix[0, 0] : (r, g, b) 
    print ('Size:', img.size[0], 'x', img.size[1])
    print ('Pixels:', img.size[0]*img.size[1])
    d_count, m_col, m_count = distinct_pix_count(img, pix)
    print ('Distinct pixel count:', d_count)
    print ('Most common pixel:', m_col, '=>', m_count)

    count_buckets = [0 for x in range(k)]
    move_count = [10 for x in range(k)]
    means = choose_random_means(k, img, pix)
    print ('random means:', means)
    count = 1
    while not check_move_count(move_count):
        count += 1
        count_buckets, move_count, means = clustering(img, pix, count_buckets, move_count, means, count)
        if count == 2:
            print ('first means:', means)
            print ('starting sizes:', count_buckets)
    pix, region_dict = update_picture(img, pix, means)  # region_dict can be an empty dictionary
    print ('Final sizes:', count_buckets)
    print ('Final means:')
    for i in range(len(means)):
        print (i+1, ':', means[i], '=>', count_buckets[i])
        
    img_tk = ImageTk.PhotoImage(img)
    lbl = tk.Label(window, image = img_tk).pack()  # display the image at window

    img.save('kmeans/2024pelavart.png', 'PNG')  # change to your own filename
    
    img.show()
    window.mainloop()
   
if __name__ == '__main__': 
   main()

# Pranav Elavarthi, 5, 2024