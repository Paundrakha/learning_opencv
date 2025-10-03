import cv2 as cv
import matplotlib.pyplot as plt

def main():
  citra=cv.imread("yoona2.jpg")
  citra=cv.cvtColor(citra,cv.COLOR_BGR2GRAY)

  histogram=cv.calcHist(images=[citra],channels=[0],mask=None,histSize=[256],ranges=[0,256])
  plt.plot(histogram)
  plt.title("Histogram untuk citra abu abu")
  plt.xlabel("Nilai pixel")
  plt.ylabel("Frekuensi")
  plt.xlim([0,256])
  plt.show()

if __name__ == "__main__":
  main()