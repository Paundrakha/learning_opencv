import cv2 as cv
import matplotlib.pyplot as plt

def main():
  citra=cv.imread("yoona2.jpg")
  plt.hist(citra[:,:,1].ravel(),bins=256,range=[0,256])
  plt.title("Histogram untuk citra warna kanal hijau")
  plt.xlabel("Nilai pixel")
  plt.ylabel("Frekuensi")
  plt.xlim([0,256])
  plt.show()

if __name__ == "__main__":
  main()