import cv2 as cv

def main():
  print("Pemisahan kanal warna pada citra warna")
  img=cv.imread("yoona2.jpg")
  blue,green,red=cv.split(img)
  cv.imshow("Original Image", img)
  cv.imshow("Kanal biru", blue)
  cv.imshow("Kanal hijau",green)
  cv.imshow("Kanal merah", red)
  cv.waitKey(0)
  cv.destroyAllWindows()


if __name__ == "__main__":
  main()