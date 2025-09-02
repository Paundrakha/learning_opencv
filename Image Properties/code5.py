import cv2 as cv

def main():
  print("Menentukan jenis citra berdasarkan image properties")
  img=cv.imread("yoona2.jpg")
  imgProperties=img.shape
  if len(imgProperties)==2:
    print("citra abu abu")
  else:
    print("citra warna")


if __name__ == "__main__":
  main()