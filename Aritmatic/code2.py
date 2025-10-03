import cv2 as cv
import numpy as np

def main():
  print("Image Addition")
  spaceman=cv.imread("baboon.jpg",cv.IMREAD_UNCHANGED)
  jmlBaris=spaceman.shape[0]
  jmlKolom=spaceman.shape[1]
  img=np.zeros(shape=(512,512,3), dtype=np.uint8)
  img[0:jmlBaris,0:jmlKolom,:]=spaceman[:,:,:3]
  img2=cv.imread("lena.jpg")

  gabung=cv.add(src1=img,src2=img2)
  cv.imshow("Hasil",gabung)
  cv.waitKey(0)
  cv.destroyALlWindows()

if __name__ == "__main__":
  main()