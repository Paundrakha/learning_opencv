import cv2 as cv
import matplotlib.pyplot as plt

def main():
  print("Pemisahan dan penggabungan kanal warna pada citra warna")
  img=cv.imread("yoona2.jpg")
  img=cv.cvtColor(img,cv.COLOR_BGR2RGB)
  red,green,blue=cv.split(img)
  plt.subplot(2,2,1)
  plt.imshow(red)
  plt.xticks([]),plt.yticks([])
  plt.title("Kanal merah")

  plt.subplot(2,2,2)
  plt.imshow(green)
  plt.xticks([]),plt.yticks([])
  plt.title("Kanal hijau")

  plt.subplot(2,2,3)
  plt.imshow(blue)
  plt.xticks([]),plt.yticks([])
  plt.title("Kanal biru")

  imgRGB=cv.merge([red,green,blue])
  plt.subplot(2,2,4)
  plt.imshow(imgRGB)
  plt.xticks([]),plt.yticks([])
  plt.title("Kanal Gabungan RGB")
  plt.show()

if __name__ == "__main__":
  main()