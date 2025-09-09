import cv2 as cv

def main():
  print("Pemisahan dan penggabungan kanal warna pada citra warna")
  img=cv.imread("yoona2.jpg")
  img=cv.cvtColor(img,cv.COLOR_BGR2Lab)
  lightness,a,b=cv.split(img)
  cv.imshow("Kanal lightness", lightness)
  cv.imshow("Kanal a", a)
  cv.imshow("Kanal b", b)
  imgLab=cv.merge([lightness,a,b])
  cv.imshow("Pengabungan 3 kanal", imgLab)
  cv.waitKey(0)
  cv.destroyAllWindows()


if __name__ == "__main__":
  main()