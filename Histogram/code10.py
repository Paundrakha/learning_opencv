import cv2 as cv

def main():
  print("Ekualisasi Histogram Citra Abu-abu")
  img=cv.imread("yoona2.jpg",cv.IMREAD_GRAYSCALE)
  histEqual=cv.equalizeHist(img)
  cv.imshow("Original Image", img)
  cv.imshow("Histogram Equlization",histEqual)
  cv.waitKey(0)
  cv.destroyAllWindows()

if __name__ == "__main__":
  main()