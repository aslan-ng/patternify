from filters.linear_filter import Cell, Pattern 


if __name__ == '__main__':
    import os
    ROOT = os.getcwd()
    path = os.path.join(ROOT, 'input')
    img_path = os.path.join(path, 'image.jpg')

    X_crop = [50, 'count']
    Y_crop = [65, 'count']
    options = [X_crop, Y_crop]
    pat = Pattern(img_path, options)
    pat.save(mode='svg')
    pat.save(mode='txt')