import numpy
from filters.objects import CellObject, PatternObject


class Cell(CellObject):
    def __init__(self, crop, center=[0, 0]):
        super().__init__(crop, center)
        self.output_points = self.output_points_generator()

    def output_points_generator(self):
        value = numpy.sum(self.data) / (self.Y_length*self.X_length)
        #print(value)
        min_gap = self.Y_length / 10 # minimum gap with the neighbour row
        radius = (((255-value) / 255) * (self.Y_length/2 - min_gap))
        min_radius = self.Y_length / 20
        if radius < min_radius: # minimum radius size
            radius = min_radius
        center = [self.center[0], self.center[1]]
        result = [center, radius]
        return result


class Pattern(PatternObject):
    def __init(self, path, options):
        super().__init__(path, options)

    def cropper(self):
        for j in range(self.cell_Y_count):
            row = list()
            for i in range(self.cell_X_count):
                X_center = (self.cell_X_length/2) + i*self.cell_X_length + self.X_0
                Y_center = (self.cell_Y_length/2) + j*self.cell_Y_length + self.Y_0
                center = [X_center, Y_center]

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

    def row_points(self):
        result = list()
        for j in range(self.cell_Y_count):
            row = list()            
            for i in range(self.cell_X_count):
                row.append(self.crops[j][i].output_points)
            #print(row)
            result.append(row)
        return result        
            
    def save(self, mode='txt'):
        if mode == 'txt':
            with open("result/pattern_circular.txt", "w") as f:
                for row in range(self.cell_Y_count):
                    for point in self.spline_points[row]:
                        f.write("%f,%f,%f\n" % (point[0][0], point[0][1], point[1]))
                    f.write("&\n")
        elif mode == 'svg':
            import svgwrite
            dwg = svgwrite.Drawing('result/pattern_circular.svg', profile='tiny')
            stroke = "#000"
            fill = "#ffffff"
            stroke_width = 1
            stroke_linejoin="round"
            stroke_linecap="round"
            for i in range(self.cell_Y_count):
                #print (self.spline_points[i])
                for j in range(len(self.spline_points[i])):
                    #print (self.spline_points[i][j])
                    center = self.spline_points[i][j][0]
                    radius = self.spline_points[i][j][1]
                    dwg.add(
                        dwg.circle(
                            center=center,
                            r=radius,
                            stroke=stroke,
                            fill=fill,
                            stroke_width=stroke_width,
                            stroke_linejoin=stroke_linejoin,
                            stroke_linecap=stroke_linecap
                            )
                        )
            dwg.save()
