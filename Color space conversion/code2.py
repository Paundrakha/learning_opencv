import cv2 as cv

def main():
  print("konversi citra BGR to RGB")
  gambar1 = cv.imread("yoona2.jpg")
  imgRGB = cv.cvtColor(gambar1, cv.COLOR_BGR2RGB)
  cv.imshow("gambar", gambar1)
  cv.imshow("gambar RGB", imgRGB)
  cv.waitKey(0)
  cv.destroyAllWindows()


if __name__=="__main__":
  main()