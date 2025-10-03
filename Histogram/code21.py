import cv2 as cv

def main():
  print("Ekualisasi Histogram Citra Warna melalui LUV dengan CLAHE")
  img=cv.imread("yoona2.jpg")
  LUVImg=cv.cvtColor(img,cv.COLOR_BGR2LUV)

  L=LUVImg[:,:,0]
  U=LUVImg[:,:,1]
  V=LUVImg[:,:,2]

  clahe=cv.createCLAHE(clipLimit=10,tileGridSize=(4,4))
  equalizeL=clahe.apply(L)
  equalizedLUV=cv.merge([equalizeL,U,V])
  equalizeImage=cv.cvtColor(equalizedLUV,cv.COLOR_LUV2BGR)
  cv.imshow("Original Image", img)
  cv.imshow("Histogram Equalization", equalizeImage)
  cv.waitKey(0)
  cv.destroyAllWindows()

if __name__ == "__main__":
  main()