import cv2 as cv

def main():
  print("Ekualisasi Histogram Citra Warna melalui HSV dengan CLAHE")
  img=cv.imread("yoona2.jpg")
  hsvImg=cv.cvtColor(img,cv.COLOR_BGR2HSV)

  hue=hsvImg[:,:,0]
  saturation=hsvImg[:,:,1]
  value=hsvImg[:,:,2]

  clahe=cv.createCLAHE(clipLimit=10,tileGridSize=(4,4))
  equalizeValue=clahe.apply(value)
  equalizedHSV=cv.merge([hue,saturation,equalizeValue])
  equalizeImage=cv.cvtColor(equalizedHSV,cv.COLOR_HSV2BGR)
  cv.imshow("Original Image", img)
  cv.imshow("Histogram Equalization", equalizeImage)
  cv.waitKey(0)
  cv.destroyAllWindows()

if __name__ == "__main__":
  main()