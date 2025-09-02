import cv2 as cv

def main():
  print("Cara mengetahui nilai pixel pada citra abu abu")
  img=cv.imread("yoona2.jpg",cv.IMREAD_GRAYSCALE)
  nilaipixel=img[:10,:10]
  #nilai pixel baris dan kolom 10 baris pertama
  print("Nilai pixel=",nilaipixel)
  cv.imshow("Citra", img)
  cv.waitKey(0)
  cv.destroyAllWindows()

if __name__ == "__main__":
  main()