import cv2 as cv
import numpy as np

def main():
  print("Image cropping with bitwise operation")
  img=cv.imread("yoona2.jpg")
  jmlBaris=img.shape[0]
  jmlKolom=img.shape[1]
  xTengah=jmlKolom//2
  yTengah=jmlBaris//2
  mask=np.zeros(shape=(jmlBaris,jmlKolom),dtype=np.uint8)

  cv.circle(mask,center=(xTengah,yTengah),radius=100,color=(255,255,255),thickness=cv.FILLED)
  hasil=cv.bitwise_and(src1=img,src2=img,mask=mask)
  cv.imshow("Original image",img)
  cv.imshow("Masker",mask)
  cv.imshow("Hasil",hasil)
  cv.waitKey(0)
  cv.destroyAllWindows()

if __name__ == "__main__":
  main()