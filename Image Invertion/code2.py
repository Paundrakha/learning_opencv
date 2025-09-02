import cv2 as cv 

def main():
  print("Image Inversion pada citra abu-abu")
  img=cv.imread("yoona2.jpg")
  imgAbu=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
  imgResult=255-imgAbu
  cv.imshow("Grey Image", imgAbu)
  cv.imshow("Image Inversion", imgResult)
  cv.waitKey(0)
  cv.destroyAllWindows()

if __name__ == "__main__":
  main()