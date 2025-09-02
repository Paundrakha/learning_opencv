import cv2 as cv
import numpy as np

def main():
  print("Image Inversion pada citra abu abu")
  img=cv.imread("yoona2.jpg")
  imgAbu=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
  jmlBaris=imgAbu.shape[0]
  jmlKolom=imgAbu.shape[1]

  imgResult=np.zeros(shape=(jmlBaris,jmlKolom),dtype=np.uint8)
  for i in range(jmlBaris):
    for j in range(jmlKolom):
      imgResult[i,j]=255-imgAbu[i,j]
  cv.imshow("Gambar Abu-abu", imgAbu)
  cv.imshow("Image Inversion", imgResult)
  cv.waitKey(0)
  cv.destroyAllWindows()


if __name__ == "__main__":
  main()