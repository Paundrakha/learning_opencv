import cv2 as cv
import numpy as np

def main():
  print("Image Inversion pada citra abu abu")
  img=cv.imread("yoona2.jpg")
  imgAbu=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
  jmlBaris=imgAbu.shape[0]
  jmlKolom=imgAbu.shape[1]

  B=img[:,:,0]
  G=img[:,:,1]
  R=img[:,:,2]

  imgResult1=np.zeros(shape=(jmlBaris,jmlKolom),dtype=np.uint8)
  imgResult2=np.zeros(shape=(jmlBaris,jmlKolom),dtype=np.uint8)
  imgResult3=np.zeros(shape=(jmlBaris,jmlKolom),dtype=np.uint8)
  for i in range(jmlBaris):
    for j in range(jmlKolom):
      imgResult1[i,j]=255-B[i,j]
      imgResult2[i,j]=255-G[i,j]
      imgResult3[i,j]=255-R[i,j]

  imgInverse=cv.merge([imgResult1,imgResult2,imgResult3])
  cv.imshow("Gambar Abu-abu", imgAbu)
  cv.imshow("Image Inversion", imgInverse)
  cv.waitKey(0)
  cv.destroyAllWindows()


if __name__ == "__main__":
  main()