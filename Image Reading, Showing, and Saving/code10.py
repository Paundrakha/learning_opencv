import cv2 as cv
import matplotlib.pyplot as plt

def main():
    print("baca dan menampilkan gambar")
    img = cv.imread("yoona2.jpg")
    img=cv.cvtColor(img,cv.COLOR_BGR2RGB)
    plt.imshow(img)
    plt.xticks([])
    plt.yticks([])
    plt.show()

if __name__ == "__main__":
    main()