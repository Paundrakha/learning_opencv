import cv2 as cv

def main():
  print("Image Properties citra abu")
  img=cv.imread("yoona2.jpg",cv.IMREAD_GRAYSCALE)
  print("Nilai pixel koordinat (0,0) sebelum diubah=",img[0,0])
  img[0,0]=222
  print("Nilai pixel koordinat (0,0) sesudah diubah=",img[0,0])
  cv.imshow("Citra", img)
  cv.waitKey(0)
  cv.destroyAllWindows()

if __name__ == "__main__":
  main()