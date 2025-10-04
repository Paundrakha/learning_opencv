import cv2 as cv

def main():
  print("Bitwise XOR dengan binary image")
  img1=cv.imread("lena.jpg")
  img2=cv.imread("baboon.jpg")

  img1XORimg2=img1^img2
  cv.imshow("Bitwise XOR", img1XORimg2)
  cv.waitKey(0)
  cv.destroyAllWindows()

if __name__ == "__main__":
  main()