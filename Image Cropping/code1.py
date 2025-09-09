import cv2 as cv

def main():
  print("SLICING IMAGE")
  img=cv.imread("yoona2.jpg")
  print("Resolusi oringinal image=", img.shape)
  #memotong image dan menyisakan baris 100 sd 400 dan kolom 100 sd 400
  imgSlicing=img[100:400,100:400]
  print("Resolusi slicing image=", imgSlicing.shape)
  cv.imshow("Original image", img)
  cv.imshow("Slicing Image", imgSlicing)
  cv.waitKey(0)
  cv.destroyAllWindows()

if __name__ == "__main__":
  main()