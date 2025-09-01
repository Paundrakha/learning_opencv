import cv2 as cv

def main():
  print("konversi citra BGR to HSV")
  gambar1 = cv.imread("yoona2.jpg")
  imgHSV = cv.cvtColor(gambar1, cv.COLOR_BGR2HSV)
  cv.imshow("img", gambar1)
  cv.imshow("HSV", imgHSV)
  cv.waitKey(0)
  cv.destroyAllWindows()

if __name__=="__main__":
  main()