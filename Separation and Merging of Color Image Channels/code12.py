import cv2 as cv

def main():
  print("Pemisahan dan penggabungan kanal warna pada citra warna")
  img=cv.imread("yoona2.jpg")
  img=cv.cvtColor(img,cv.COLOR_BGR2Luv)
  lightness,u,v=cv.split(img)
  cv.imshow("Kanal lightness", lightness)
  cv.imshow("Kanal u", u)
  cv.imshow("Kanal v", v)
  imgLuv=cv.merge([lightness,u,v])
  cv.imshow("Pengabungan 3 kanal", imgLuv)
  cv.waitKey(0)
  cv.destroyAllWindows()


if __name__ == "__main__":
  main()