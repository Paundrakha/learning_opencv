import cv2 as cv

def main():
  print("Image Properties citra abu")
  img=cv.imread("yoona2.jpg",cv.IMREAD_GRAYSCALE)
  print("Nilai pixel baris dan kolom 100 baris pertama sebelum diubah=",img[:100,:100])
  img[:100,:100]=0
  print("Nilai pixel baris dan kolom 100 baris pertama setelah diubah=",img[:100,:100])
  cv.imshow("Citra", img)
  cv.waitKey(0)
  cv.destroyAllWindows()

if __name__ == "__main__":
  main()