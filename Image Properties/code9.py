import cv2 as cv

def main():
  print("Image Properties citra warna")
  img=cv.imread("yoona2.jpg")
  nilaipixel=img[0,0]
  print("Nilai pixel=",nilaipixel)
  cv.imshow("Citra", img)
  cv.waitKey(0)
  cv.destroyAllWindows()

if __name__ == "__main__":
  main()