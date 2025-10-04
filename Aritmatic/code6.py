import cv2 as cv

def main():
  print("Bitwise AND dengan binary image")
  img1=cv.imread("lena.jpg")
  img2=cv.imread("baboon.jpg")

  img1ANDimg2=cv.bitwise_and(src1=img1,src2=img2,mask=None)
  cv.imshow("Bitwise AND", img1ANDimg2)
  cv.waitKey(0)
  cv.destroyAllWindows()

if __name__ == "__main__":
  main()