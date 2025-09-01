import cv2 as cv

def main():
    gambar1 = cv.imread("yoona2.jpg")
    cv.imshow("ini gambar", gambar1)
    cv.waitKey(0)
    cv.destroyAllWindows()

if __name__ == "__main__":
    main()