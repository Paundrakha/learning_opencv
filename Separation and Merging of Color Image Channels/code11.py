import cv2 as cv

def main():
  print("Pemisahan dan penggabungan kanal warna pada citra warna")
  img=cv.imread("yoona2.jpg")
  img=cv.cvtColor(img,cv.COLOR_BGR2LUV)
  lightness,U,V=cv.split(img)
  cv.imshow("Kanal lightness", lightness)
  cv.imshow("Kanal U", U)
  cv.imshow("Kanal V", V)
  imgLUV=cv.merge([lightness,U,V])
  cv.imshow("Pengabungan 3 kanal", imgLUV)
  cv.waitKey(0)
  cv.destroyAllWindows()


if __name__ == "__main__":
  main()