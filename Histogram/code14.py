import cv2 as cv

def main():
  print("Ekualisasi Histogram Citra Warna melalui LAB")
  img=cv.imread("yoona2.jpg")
  #konversi BGR to HSV
  labImg=cv.cvtColor(img,cv.COLOR_BGR2LAB)
  #Split ke masing" komponen
  L=labImg[:,:,0]
  A=labImg[:,:,1]
  B=labImg[:,:,2]
  #lakukan ekualisasi histogram hanya pada komponen value yang memuat informasi intensitas cahaya
  equalizeL=cv.equalizeHist(L)
  equalHiz=cv.merge([equalizeL,A,B])
  equalizeImage=cv.cvtColor(equalHiz,cv.COLOR_LAB2BGR)
  cv.imshow("Original Image", img)
  cv.imshow("Histogram Equalization", equalizeImage)
  cv.waitKey(0)
  cv.destroyAllWindows()

if __name__ == "__main__":
  main() 