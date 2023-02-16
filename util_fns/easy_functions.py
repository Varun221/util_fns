import matplotlib.pyplot as plt


## show any image with given size
def show_image(img, size=(8,8)):
    plt.figure(figsize=size)
    
    while img.shape[0] == 1:
        img = img[0]
    
    if len(img.shape) == 3:
        plt.imshow(img[:, :, ::-1])
    elif (len(img.shape) == 2) or (img.shape[-1] == 1):
        plt.imshow(img, cmap='gray')
        
    plt.show()
