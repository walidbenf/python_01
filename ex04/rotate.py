import numpy as np
from load_image import ft_load
import matplotlib.pyplot as plt

def manual_transpose(arr):
    # arr shape: (400, 400, 1) ou (400, 400)
    h, w = arr.shape[0], arr.shape[1]
    transposed = np.zeros((w, h), dtype=arr.dtype)
    for i in range(h):
        for j in range(w):
            transposed[j, i] = arr[i, j] if arr.ndim == 2 else arr[i, j, 0]
    return transposed

def main():
    try:
        arr = ft_load("animal.jpeg")
        # Découpe centrale 400x400, canal rouge
        h, w = arr.shape[0], arr.shape[1]
        startx = w//2 - 200
        starty = h//2 - 200
        square = arr[starty:starty+400, startx:startx+400, 0:1]
        print(f"The shape of image is: {square.shape}")
        print(square)

        # Transpose manuelle
        transposed = manual_transpose(square)
        print(f"New shape after Transpose: {transposed.shape}")
        print(transposed)

        # Affichage
        plt.imshow(transposed, cmap='gray')
        plt.title("Transposed image")
        plt.xlabel("X axis (pixels)")
        plt.ylabel("Y axis (pixels)")
        plt.colorbar(label="Pixel value")
        plt.show()

    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()