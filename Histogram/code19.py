import cv2 as cv

def main():
  print("Ekualisasi Histogram Citra Warna melalui YCrCb dengan CLAHE")
  img=cv.imread("yoona2.jpg")
  ycrcbImg=cv.cvtColor(img,cv.COLOR_BGR2YCrCb)

  y=ycrcbImg[:,:,0]
  cr=ycrcbImg[:,:,1]
  cb=ycrcbImg[:,:,2]

  clahe=cv.createCLAHE(clipLimit=10,tileGridSize=(5,5))
  equalizeY=clahe.apply(y)
  equalizedYCrCb=cv.merge([equalizeY,cr,cb])
  equalizeImage=cv.cvtColor(equalizedYCrCb,cv.COLOR_YCrCb2BGR)
  cv.imshow("Original Image", img)
  cv.imshow("Histogram Equalization", equalizeImage)
  cv.waitKey(0)
  cv.destroyAllWindows()

if __name__ == "__main__":
  main()