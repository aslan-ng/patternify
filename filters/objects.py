import cv2
import os
import numpy


class CellObject:
    def __init__(self, crop, center=[0, 0]):
        ''' crop: array of cropped image '''
        self.data = crop
        self.Y_length = len(self.data)
        self.X_length = len(self.data[0])

        ''' center: coordinate of center of cell in [X, Y, Z] format '''
        self.center = center
        self.output_points = None

    def show(self):
        ''' showing image contained in cell '''
        cv2.imshow('cell', self.data)


class PatternObject:
    def __init__(self, path, options):
        ''' options: size of cells, example:
            [[X_value, X_unit], [Y_value, Y_unit]] '''
        self.image = cv2.imread(path, 0)
        #self.image = cv2.imread("abc.tiff", mode='RGB')
        self.X_length = len(self.image[0])
        self.Y_length = len(self.image)

        self.crops = list() # list of all crops of image, like mosaic
        self.X_0 = 0
        self.cell_X_length = None
        self.cell_X_count = None
        self.Y_0 = 0
        self.cell_Y_length = None
        self.cell_Y_count = None
        
        self.analyse(self.image, options)
        self.cropper()
        self.spline_points = self.row_points()

    def row_points(self):
        return None

    def show(self):
        cv2.imshow('image', self.image)

    def analyse(self, image, options):
        ''' X calculations '''
        X_val = options[0][0]
        X_unit = options[0][1]
        if X_unit == 'count':
            self.cell_X_length = self.X_length / X_val
            self.cell_X_count = X_val
        elif X_unit == 'pixel':
            self.cell_X_length = X_val
            self.cell_X_count = int(self.X_length / X_val)
            self.X_0 = (self.X_length - self.cell_X_count * X_val) / 2

        ''' Y calculations '''
        Y_val = options[1][0]
        Y_unit = options[1][1]
        if Y_unit == 'count':
            self.cell_Y_length = self.Y_length / Y_val
            self.cell_Y_count = Y_val
        elif Y_unit == 'pixel':
            self.cell_Y_length = Y_val
            self.cell_Y_count = int(self.Y_length / Y_val)
            self.Y_0 = (self.Y_length - self.cell_Y_count * Y_val) / 2