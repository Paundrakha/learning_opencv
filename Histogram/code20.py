import cv2 as cv

def main():
  print("Ekualisasi Histogram Citra Warna melalui LAB dengan CLAHE")
  img=cv.imread("yoona2.jpg")
  LABImg=cv.cvtColor(img,cv.COLOR_BGR2LAB)

  L=LABImg[:,:,0]
  A=LABImg[:,:,1]
  B=LABImg[:,:,2]

  clahe=cv.createCLAHE(clipLimit=10,tileGridSize=(8,8))
  equalizeL=clahe.apply(L)
  equalizedLAB=cv.merge([equalizeL,A,B])
  equalizeImage=cv.cvtColor(equalizedLAB,cv.COLOR_LAB2BGR)
  cv.imshow("Original Image", img)
  cv.imshow("Histogram Equalization", equalizeImage)
  cv.waitKey(0)
  cv.destroyAllWindows()

if __name__ == "__main__":
  main()