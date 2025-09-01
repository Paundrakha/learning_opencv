import cv2 as cv

def main():
  print("konversi citra BGR to LUV")
  gambar1 = cv.imread("yoona2.jpg")
  imgLUV = cv.cvtColor(gambar1, cv.COLOR_BGR2LUV)
  cv.imshow("img", gambar1)
  cv.imshow("LUV", imgLUV)
  cv.waitKey(0)
  cv.destroyAllWindows()

if __name__=="__main__":
  main()