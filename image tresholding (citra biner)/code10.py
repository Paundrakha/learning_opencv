import cv2 as cv

def main():
  print("Global Image Thresholding dengan threshold truncated")
  img=cv.imread("yoona2.jpg")
  imgGrey=cv.cvtColor(img,cv.COLOR_BGR2GRAY)

  ambang,imgThreshold=cv.threshold(imgGrey,thresh=125,maxval=255,type=cv.THRESH_TRUNC)
  cv.imshow("Original Image", img)
  cv.imshow("Image Threshold", imgThreshold)
  cv.waitKey(0)
  cv.destroyAllWindows()

if __name__ == "__main__":
  main()