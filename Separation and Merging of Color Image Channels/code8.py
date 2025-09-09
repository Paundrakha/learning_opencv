import cv2 as cv

def main():
  print("Pemisahan dan penggabungan kanal warna pada citra warna")
  img=cv.imread("yoona2.jpg")
  img=cv.cvtColor(img,cv.COLOR_BGR2HLS)
  hue,lightness,saturation=cv.split(img)
  cv.imshow("Kanal hue", hue)
  cv.imshow("Kanal lightness", lightness)
  cv.imshow("Kanal saturation",saturation)
  imgHLS=cv.merge([hue,lightness,saturation])
  cv.imshow("Pengabungan 3 kanal", imgHLS)
  cv.waitKey(0)
  cv.destroyAllWindows()


if __name__ == "__main__":
  main()