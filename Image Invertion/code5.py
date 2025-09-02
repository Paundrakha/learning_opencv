import cv2 as cv

def main():
  print("Image Inversion pada citra warna")
  img=cv.imread("yoona2.jpg")
  B,G,R =cv.split(img)
  imgResult1=255-B
  imgResult2=255-G
  imgResult3=255-R

  imgInverse=cv.merge([imgResult1,imgResult2,imgResult3])
  cv.imshow("Gambar Warna", img)
  cv.imshow("Image Inversion", imgInverse)
  cv.waitKey(0)
  cv.destroyAllWindows()


if __name__ == "__main__":
  main()