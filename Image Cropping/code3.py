import cv2 as cv

def main():
  print("SLICING IMAGE")
  img=cv.imread("yoona2.jpg")
  print("Resolusi oringinal image=", img.shape)
  #memotong image dan menyisakan 200 kolom pertama semua baris
  imgSlicing=img[:,:200]
  print("Resolusi slicing image=", imgSlicing.shape)
  cv.imshow("Original image", img)
  cv.imshow("Slicing Image", imgSlicing)
  cv.waitKey(0)
  cv.destroyAllWindows()

if __name__ == "__main__":
  main()