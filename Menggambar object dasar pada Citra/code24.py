import cv2 as cv

def main():
  print("Menambahkan text pada citra")
  citra=cv.imread("yoona2.jpg")

  cv.putText(citra,text="apa inii",org=(175,256),fontFace=cv.FONT_HERSHEY_SIMPLEX,fontScale=1,color=(0,255,255),thickness=5)
  cv.imshow("citra",citra)
  cv.waitKey(0)
  cv.destroyAllWindows()

if __name__ == "__main__":
  main()