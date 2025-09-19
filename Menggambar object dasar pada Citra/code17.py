import cv2 as cv
import numpy as np

def main():
  print("Menambahkan persegi pada citra")
  citra=255*np.ones(shape=(512,512,3),dtype=np.uint8)

  cv.rectangle(citra,pt1=(100,100),pt2=(200,200),color=(0,0,255),thickness=5)
  cv.rectangle(citra,pt1=(200,200),pt2=(300,300),color=(0,255,0),thickness=5)
  cv.rectangle(citra,pt1=(300,300),pt2=(400,400),color=(255,0,0),thickness=5)

  cv.imshow("Hasil Citra", citra)
  cv.waitKey(0)
  cv.destroyAllWindows()

if __name__ == "__main__":
  main()