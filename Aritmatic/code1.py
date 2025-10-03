import cv2 as cv

def main():
  print("Image Addition")
  img1=cv.imread("baboon.jpg")
  img2=cv.imread("lena.jpg")

  gabung=cv.add(src1=img1,src2=img2)
  cv.imshow("Hasil", gabung)
  cv.waitKey(0)
  cv.destroyAllWindows()

if __name__ == "__main__":
  main()