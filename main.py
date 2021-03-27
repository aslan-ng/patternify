if __name__ == '__main__':
    import os
    ROOT = os.getcwd()
    path = os.path.join(ROOT, 'input')
    img_path = os.path.join(path, 'image.jpg')

    ''' linear filter '''
    from filters.linear import Pattern 
    X_crop = [50, 'count']
    Y_crop = [65, 'count']
    crop_options = [X_crop, Y_crop]
    pat = Pattern(img_path, crop_options)
    pat.save(mode='svg')
    pat.save(mode='txt')

    ''' circular filter '''
    from filters.circular import Pattern
    X_crop = [60, 'count']
    Y_crop = [65, 'count']
    crop_options = [X_crop, Y_crop]
    pat = Pattern(img_path, crop_options)
    pat.save(mode='svg')
    pat.save(mode='txt')