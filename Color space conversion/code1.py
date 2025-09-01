import cv2 as cv

def main():
  print("konversi citra BGR to GRAY")
  gambar1 = cv.imread("yoona2.jpg")
  imgGray = cv.cvtColor(gambar1, cv.COLOR_BGR2GRAY)
  cv.imshow("ini gambar", gambar1)
  cv.imshow("gambar abu abu", imgGray)
  cv.waitKey(0)
  cv.destroyAllWindows()


if __name__ == "__main__":
  main()