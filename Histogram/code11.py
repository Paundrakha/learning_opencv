import cv2 as cv

def main():
  print("Ekualisasi Histogram Citra Warna melalui HSV")
  img=cv.imread("yoona2.jpg")
  #konversi BGR to HSV
  hsvImg=cv.cvtColor(img,cv.COLOR_BGR2HSV)
  #Split ke masing" komponen
  hue=hsvImg[:,:,0]
  saturation=hsvImg[:,:,1]
  value=hsvImg[:,:,2]
  #lakukan ekualisasi histogram hanya pada komponen value yang memuat informasi intensitas cahaya
  equalizeValue=cv.equalizeHist(value)
  equalHiz=cv.merge([hue,saturation,equalizeValue])
  equalizeImage=cv.cvtColor(equalHiz,cv.COLOR_HSV2BGR)
  cv.imshow("Original Image", img)
  cv.imshow("Histogram Equalization", equalizeImage)
  cv.waitKey(0)
  cv.destroyAllWindows()

if __name__ == "__main__":
  main() 