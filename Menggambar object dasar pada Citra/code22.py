import cv2 as cv
import numpy as np

def main():
  print("Menambahkan polygon tertutup pada citra dengan fungsi polylines")
  citra=np.zeros(shape=(256,256,3),dtype=np.uint8)
  titik=np.array([[10,128],[200,10],[180,120],[240,240]])

  cv.polylines(citra,pts=[titik],isClosed=True,color=(255,255,255),thickness=5)
  cv.fillPoly(citra,pts=[titik],color=(0,255,255))
  cv.imshow("Hasil citra",citra)
  cv.waitKey(0)
  cv.destroyAllWindows()

if __name__ == "__main__":
  main()