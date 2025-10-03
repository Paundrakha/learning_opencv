import cv2 as cv

def main():
  print("Ekualisasi Histogram Citra Warna melalalui HSV")
  img=cv.imread("yoona2.jpg")
  hsvImg=cv.cvtColor(img,cv.COLOR_BGR2HSV)

  hue,saturation,value = cv.split(hsvImg)
  equalizeValue=cv.equalizeHist(value)
  equalizeHsv=cv.merge([hue,saturation,equalizeValue])
  equalizeImg=cv.cvtColor(equalizeHsv,cv.COLOR_HSV2BGR)
  cv.imshow("Original Image", img)
  cv.imshow("Histogram Equalization", equalizeImg)
  cv.waitKey(0)
  cv.destroyAllWindows()

if __name__ == "__main__":
  main()