import cv2 as cv

def main():
  print("Bitwise NOT dengan binary image")
  img1=cv.imread("lena.jpg")
  img2=cv.imread("baboon.jpg")

  img1NOT=cv.bitwise_not(src=img1,mask=None)
  img2NOT=cv.bitwise_not(src=img2,mask=None)
  cv.imshow("Bitwise Not image 1",img1NOT)
  cv.imshow("Bitwise Not image 2",img2NOT)
  cv.waitKey(0)
  cv.destroyAllWindows()

if __name__ == "__main__":
  main()