import cv2 as cv

def main():
  print("Otsu Image Thresholding dengan tipe threshold binary")
  img=cv.imread("yoona2.jpg")
  imgGrey=cv.cvtColor(img,cv.COLOR_BGR2GRAY)

  ambang,imgThresh=cv.threshold(imgGrey,thresh=0,maxval=255,type=cv.THRESH_BINARY+cv.THRESH_OTSU)
  cv.imshow("Original image", img)
  cv.imshow("Image Thresholding", imgThresh)
  cv.waitKey(0)
  cv.destroyAllWindows()

if __name__=="__main__":
  main()