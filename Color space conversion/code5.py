import cv2 as cv

def main():
  print("konversi citra BGR to LAB")
  gambar1 = cv.imread("yoona2.jpg")
  imgLAB = cv.cvtColor(gambar1, cv.COLOR_BGR2LAB)
  cv.imshow("img", gambar1)
  cv.imshow("LAB", imgLAB)
  cv.waitKey(0)
  cv.destroyAllWindows()

if __name__=="__main__":
  main()