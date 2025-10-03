import cv2 as cv
import matplotlib.pyplot as plt

def main():
  citra=cv.imread("yoona2.jpg")
  warna=('b','g','r')
  jmlKanal=3
  for i in range(jmlKanal):
    histogram=cv.calcHist(images=[citra],channels=[i], mask=None,histSize=[256],ranges=[0,256])
    plt.plot(histogram,color=warna[i])
    plt.xlim([0,256])
    plt.title("Histogram citra warna semua kanal")
    plt.xlabel("Nilai pixel")
    plt.ylabel("Frekuensi")
    plt.show()

if __name__ == "__main__":
  main() 