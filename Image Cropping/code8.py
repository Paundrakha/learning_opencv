import cv2 as cv

def main():
  print("SLICING IMAGE")
  img=cv.imread("yoona2.jpg")
  print("Resolusi oringinal image=", img.shape)
  img[0:100,100:]=(0,0,255)
  cv.imshow("Original image", img)
  cv.waitKey(0)
  cv.destroyAllWindows()

if __name__ == "__main__":
  main()