import cv2 as cv

def main():
  print("Menambahkan text pada citra")
  citra=cv.imread("yoona2.jpg")

  cv.putText(citra,text="Paundrakha Bajra Denta",org=(175,256),fontFace=cv.FONT_HERSHEY_SCRIPT_COMPLEX+cv.FONT_ITALIC,fontScale=1,color=(0,0,255), thickness=5)
  cv.imshow("Hasil Citra",citra)
  cv.waitKey(0)
  cv.destroyAllWindows()

if __name__ == "__main__":
  main()