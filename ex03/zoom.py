import numpy as np
import matplotlib.pyplot as plt
from load_image import ft_load

def main():
    try:
        arr = ft_load("animal.jpeg")
        print(f"The shape of image is: {arr.shape}")
        print(arr)

        # Zoom: slice central 400x400, 1 canal (par exemple canal rouge)
        h, w = arr.shape[0], arr.shape[1]
        startx = w//2 - 200
        starty = h//2 - 200
        zoomed = arr[starty:starty+400, startx:startx+400, 0:1]
        print(f"New shape after slicing: {zoomed.shape}")
        print(zoomed)

        # Affichage avec échelle
        plt.imshow(zoomed.squeeze(), cmap='gray')
        plt.xlabel("X axis (pixels)")
        plt.ylabel("Y axis (pixels)")
        plt.title("Zoomed image")
        plt.colorbar(label="Pixel value")
        plt.show()

    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()