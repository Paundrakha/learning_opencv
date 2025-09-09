import cv2 as cv

def main():
  print("Pemisahan dan penggabungan kanal warna pada citra warna")
  img=cv.imread("yoona2.jpg")
  img=cv.cvtColor(img,cv.COLOR_BGR2LAB)
  lightness,A,B=cv.split(img)
  cv.imshow("Kanal lightness", lightness)
  cv.imshow("Kanal A", A)
  cv.imshow("Kanal B", B)
  imgLAB=cv.merge([lightness,A,B])
  cv.imshow("Pengabungan 3 kanal", imgLAB)
  cv.waitKey(0)
  cv.destroyAllWindows()


if __name__ == "__main__":
  main()