import cv2 as cv

def main():
  print("SLICING IMAGE")
  img=cv.imread("yoona2.jpg")
  print("Resolusi oringinal image=", img.shape)
  img[:100,:100]=(255,0,0)
  cv.imshow("Original image", img)
  cv.waitKey(0)
  cv.destroyAllWindows()

if __name__ == "__main__":
  main()