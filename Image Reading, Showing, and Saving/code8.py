import cv2 as cv
import numpy as np
import sys
def main():
    print("READING AND SHOWING IMAGE")
    gambar1 = cv.imread("yoona2.jpg")
    gambar2 = cv.imread("gambar.png")

    if (gambar1.shape == gambar2.shape):
        print("bisa ditumpuk karna ukuran resolusi sama")
        tumpukan = np.vstack((gambar1, gambar2))
        cv.imshow("tumpukan", tumpukan)
    else:
        print("bedaa resolusi")
        sys.exit(1)

    cv.waitKey(0)
    cv.destroyAllWindows()

if __name__ == "__main__":
    main()