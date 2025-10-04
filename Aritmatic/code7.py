import cv2 as cv

def main():
  print("Bitwise OR dengan binary image")
  img1=cv.imread("lena.jpg")
  img2=cv.imread("baboon.jpg")

  img1ORimg2=img1|img2
  cv.imshow("Bitwise OR", img1ORimg2)
  cv.waitKey(0)
  cv.destroyAllWindows()

if __name__ == "__main__":
  main()