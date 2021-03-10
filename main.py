import cv2
import os
import numpy


class Cell:

    def __init__(self, crop, center=[0, 0, 0]):
        ''' crop: array of cropped image '''
        self.data = crop
        self.Y_length = len(self.data)
        self.X_length = len(self.data[0])

        ''' center: coordinate of center of cell in [X, Y, Z] format '''
        self.center = center
        self.output_points = self.OutputPoints()


    ''' showing image contained in cell '''
    def Show(self):
        cv2.imshow('cell', self.data)


    def OutputPoints(self):
        value = numpy.sum(self.data) / (self.Y_length*self.X_length)
        #print(value)
        shift_Y = self.Y_length / 10 # for having indipendents rows after cut
        delta_Y = (((255-value) / 255) * (self.Y_length/2 - shift_Y))
        if delta_Y < self.Y_length / 20:
            delta_Y = self.Y_length / 20
        foreward_point = [self.center[0], self.center[1] + delta_Y, self.center[2]]
        backward_point = [self.center[0], self.center[1] - delta_Y, self.center[2]]
        return [foreward_point, backward_point]


class Pattern:

    def __init__(self, path, options):
        ''' options: size of cells, example:
            [[X_value, X_unit], [Y_value, Y_unit]] '''
        self.image = cv2.imread(path, 0)
        #self.image = cv2.imread("abc.tiff", mode='RGB')
        self.X_length = len(self.image[0])
        self.Y_length = len(self.image)

        self.X_0 = 0
        self.Y_0 = 0
        self.Analyse(self.image, options)
        self.Cropper()
        self.spline_points = self.RowPoints()


    def Show(self):
        cv2.imshow('image', self.image)


    def Analyse(self, image, options):
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


    def Cropper(self):
        self.crops = list()
        for j in range(self.cell_Y_count):
            row = list()
            for i in range(self.cell_X_count):
                X_center = (self.cell_X_length/2) + i*self.cell_X_length + self.X_0
                Y_center = (self.cell_Y_length/2) + j*self.cell_Y_length + self.Y_0
                center = [X_center, Y_center, 0]

                X_start = int(i*self.cell_X_length)
                X_end = int((i+1)*self.cell_X_length)
                Y_start = int(j*self.cell_Y_length)
                Y_end = int((j+1)*self.cell_Y_length)
                #print(X_start, X_end, Y_start, Y_end)

                crop = self.image[Y_start : Y_end, X_start : X_end]
                #cv2.imshow('test', crop)
                new_cell = Cell(crop, center)
                row.append(new_cell)
            self.crops.append(row)


    def RowPoints(self):
        result = list()
        for j in range(self.cell_Y_count):
            row = list()
            row_forward = list()
            row_backward = list()

            first_cell = self.crops[j][0]
            first_point_X = first_cell.center[0] - first_cell.X_length/2
            first_point_Y = first_cell.center[1]
            first_point = [first_point_X, first_point_Y, 0]
            row_forward.append(first_point)
            row_backward.append(first_point)
            
            for i in range(self.cell_X_count):
                row_forward.append(self.crops[j][i].output_points[0])
                row_backward.append(self.crops[j][i].output_points[1])

            last_cell = self.crops[j][-1]
            last_point_X = last_cell.center[0] + last_cell.X_length/2
            last_point_Y = last_cell.center[1]
            last_point = [last_point_X, last_point_Y, 0]
            row_forward.append(last_point)
            row_backward.append(last_point)
            
            row += row_forward

            row_backward.reverse()
            row += row_backward

            result.append(row)
        return result
            
            
    def Save(self):
        with open("pattern_points.txt", "w") as f:
            for row in range(self.cell_Y_count):
                for point in self.spline_points[row]:
                    f.write("%f,%f,%f\n" % (point[0], point[1], point[2]))
                f.write("&\n")


if __name__ == '__main__':
    ROOT = os.getcwd()
    img_path = os.path.join(ROOT, "input.jpg")

    options = [[50, 'count'], [65, 'count']]
    pat = Pattern(img_path, options)
    
    #print(pat.crops[12][5].output_points)
    #print(pat.spline_points[0])
    pat.Save()
