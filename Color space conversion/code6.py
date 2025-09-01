import cv2 as cv

def main():
  print("konversi citra BGR to CIELAB")
  gambar1 = cv.imread("yoona2.jpg")
  imgCIELAB = cv.cvtColor(gambar1, cv.COLOR_BGR2Lab)
  cv.imshow("img", gambar1)
  cv.imshow("CIELAB", imgCIELAB)
  cv.waitKey(0)
  cv.destroyAllWindows()

if __name__=="__main__":
  main()