import cv2 as cv

def main():
  print("Pemisahan kanal warna pada citra warna")
  img=cv.imread("yoona2.jpg")
  kanal=cv.split(img)
  blue=kanal[0]
  green=kanal[1]
  red=kanal[2]
  cv.imshow("Kanal biru", blue)
  cv.imshow("Kanal hijau",green)
  cv.imshow("Kanal merah", red)
  imgBGR=cv.merge([blue,green,red])
  cv.imshow("Pengabungan 3 kanal", imgBGR)
  cv.waitKey(0)
  cv.destroyAllWindows()


if __name__ == "__main__":
  main()