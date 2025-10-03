import cv2 as cv

def main():
  print("Ekualisasi Histogram Citra Warna melalui YCrCb")
  img=cv.imread("yoona2.jpg")
  #konversi BGR to HSV
  ycrcbImg=cv.cvtColor(img,cv.COLOR_BGR2YCrCb)
  #Split ke masing" komponen
  y=ycrcbImg[:,:,0]
  cr=ycrcbImg[:,:,1]
  cb=ycrcbImg[:,:,2]
  #lakukan ekualisasi histogram hanya pada komponen value yang memuat informasi intensitas cahaya
  equalizeY=cv.equalizeHist(y)
  equalHiz=cv.merge([equalizeY,cr,cb])
  equalizeImage=cv.cvtColor(equalHiz,cv.COLOR_YCrCb2BGR)
  cv.imshow("Original Image", img)
  cv.imshow("Histogram Equalization", equalizeImage)
  cv.waitKey(0)
  cv.destroyAllWindows()

if __name__ == "__main__":
  main() 