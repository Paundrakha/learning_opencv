import cv2 as cv 

def main():
  print("Local Image Thresholding dengan thresholding binary")
  img=cv.imread("yoona2.jpg")

  imgGrey=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
  imgThresh=cv.adaptiveThreshold(imgGrey,maxValue=255,adaptiveMethod=cv.ADAPTIVE_THRESH_GAUSSIAN_C,thresholdType=cv.THRESH_BINARY,blockSize=5,C=2)
  cv.imshow("Original image", img)
  cv.imshow("Image Thresholding", imgThresh)
  cv.waitKey(0)
  cv.destroyAllWindows()

if __name__=="__main__":
  main()