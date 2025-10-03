import cv2 as cv

def main():
  print("Ekualisasi Histogram Citra Abu abu dengan CLAHE")
  img=cv.imread("yoona2.jpg",cv.IMREAD_GRAYSCALE)
  clahe=cv.createCLAHE(clipLimit=12,tileGridSize=(4,4))
  histEqual=clahe.apply(img)
  cv.imshow("Original Image", img)
  cv.imshow("Histogram Equalization",histEqual)
  cv.waitKey(0)
  cv.destroyAllWindows()

if __name__ == "__main__":
  main()