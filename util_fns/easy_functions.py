import matplotlib.pyplot as plt


## show any image with given size
def show_image(img, size=(8,8)):
    plt.figure(figsize=size)
    
    if len(img.shape) == 3:
        plt.imshow(img[:, :, ::-1])
    else:
        plt.imshow(img, cmap='gray')
        
    plt.show()
