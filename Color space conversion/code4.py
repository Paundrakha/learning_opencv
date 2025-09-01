import cv2 as cv

def main():
  print("konversi citra BGR to HLS")
  gambar1 = cv.imread("yoona2.jpg")
  imgHLS = cv.cvtColor(gambar1, cv.COLOR_BGR2HLS)
  cv.imshow("img", gambar1)
  cv.imshow("HLS", imgHLS)
  cv.waitKey(0)
  cv.destroyAllWindows()

if __name__=="__main__":
  main()