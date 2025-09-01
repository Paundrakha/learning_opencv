import cv2 as cv

def main():
  print("konversi citra BGR to YCrCb")
  gambar1 = cv.imread("yoona2.jpg")
  imgYCrCb = cv.cvtColor(gambar1, cv.COLOR_BGR2YCrCb)
  cv.imshow("img", gambar1)
  cv.imshow("YCrCb", imgYCrCb)
  cv.waitKey(0)
  cv.destroyAllWindows()

if __name__=="__main__":
  main()