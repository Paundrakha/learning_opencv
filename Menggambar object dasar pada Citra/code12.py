import cv2 as cv
import numpy as np

def main():
  print("Menambahkan gambar garis,lingkaran, dan ellips pada citra warna putih")
  citra=255*np.ones(shape=(256,256,3),dtype=np.uint8)
  jmlBaris=citra.shape[0]
  jmlKolom=citra.shape[1]
  xTengah=jmlKolom//2
  yTengah=jmlBaris//2
  cv.line(citra,pt1=(xTengah,0),pt2=(xTengah,jmlBaris-1),color=(0,0,255),thickness=5)
  cv.line(citra,pt1=(0,yTengah),pt2=(jmlKolom-1,yTengah),color=(0,255,0),thickness=5)

  cv.circle(citra,center=(xTengah,yTengah),radius=10,color=(0,0,0),thickness=cv.FILLED)
  cv.ellipse(citra,center=(xTengah,yTengah),axes=(100,50),angle=0,startAngle=0,endAngle=360,color=(255,0,0),thickness=5)
  cv.ellipse(citra,center=(xTengah,yTengah),axes=(100,50),angle=90,startAngle=0,endAngle=360,color=(255,0,0),thickness=5)

  cv.imshow("citra",citra)
  cv.waitKey(0)
  cv.destroyAllWindows()

if __name__ == "__main__":
  main()

