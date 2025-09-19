import cv2 as cv

def main():
  print("Menambahkan persegi pada citra")
  citra=cv.imread("yoona2.jpg")
  cv.rectangle(citra,pt1=(100,100),pt2=(400,200),color=(0,0,255),thickness=5)

  cv.imshow("Hasil Citra", citra)
  cv.waitKey(0)
  cv.destroyAllWindows()

if __name__ == "__main__":
  main()