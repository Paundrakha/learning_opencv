import cv2 as cv

def main():
    print("READING AND SHOWING IMAGE")
    gambar1 = cv.imread("yoona2.jpg",cv.IMREAD_COLOR)
    cv.imshow("ini gambar", gambar1)
    cv.waitKey(0)
    cv.destroyAllWindows()

if __name__ == "__main__":
    main()