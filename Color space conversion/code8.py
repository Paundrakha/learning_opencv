import cv2 as cv

def main():
  print("konversi citra BGR to CIELUV")
  gambar1 = cv.imread("yoona2.jpg")
  imgCIELUV = cv.cvtColor(gambar1, cv.COLOR_BGR2Luv)
  cv.imshow("img", gambar1)
  cv.imshow("CIELUV", imgCIELUV)
  cv.waitKey(0)
  cv.destroyAllWindows()

if __name__=="__main__":
  main()