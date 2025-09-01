import cv2 as cv
import matplotlib.pyplot as plt

def main():
    print("baca dan menampilkan gambar")
    img = cv.imread("yoona2.jpg")
    img2 = cv.imread("yoona.jpg")
    img=cv.cvtColor(img,cv.COLOR_BGR2RGB)
    img2=cv.cvtColor(img2,cv.COLOR_BGR2RGB)
    plt.subplot(1,2,1)
    plt.imshow(img)
    plt.xticks([])
    plt.yticks([])
    plt.title("kolom 1")
    plt.subplot(1,2,2)
    plt.imshow(img2)
    plt.xticks([])
    plt.yticks([])
    plt.title("kolom 2")
    plt.show()

if __name__ == "__main__":
    main()