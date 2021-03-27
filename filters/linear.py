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
        delta_Y = (((255-value) / 255) * (self.Y_length/2 - min_gap/2))
        min_delta_Y = self.Y_length / 20 # minimum gap within the shape
        if delta_Y < min_delta_Y:
            delta_Y = min_delta_Y
        foreward_point = [self.center[0], self.center[1] + delta_Y]
        backward_point = [self.center[0], self.center[1] - delta_Y]
        result = [foreward_point, backward_point]
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
            row_forward = list()
            row_backward = list()

            first_cell = self.crops[j][0]
            first_point_X = first_cell.center[0] - first_cell.X_length/2
            first_point_Y = first_cell.center[1]
            first_point = [first_point_X, first_point_Y]
            row_forward.append(first_point)
            row_backward.append(first_point)
            
            for i in range(self.cell_X_count):
                row_forward.append(self.crops[j][i].output_points[0])
                row_backward.append(self.crops[j][i].output_points[1])

            last_cell = self.crops[j][-1]
            last_point_X = last_cell.center[0] + last_cell.X_length/2
            last_point_Y = last_cell.center[1]
            last_point = [last_point_X, last_point_Y]
            row_forward.append(last_point)
            row_backward.append(last_point)
            
            row += row_forward

            row_backward.reverse()
            row += row_backward
            #print(row)

            result.append(row)
            self.cells = result
        #return result        
            
    def save(self, mode='txt'):
        if mode == 'txt':
            with open("result/pattern_linear.txt", "w") as f:
                for row in range(self.cell_Y_count):
                    for point in self.cells[row]:
                        f.write("%f,%f,%f\n" % (point[0], point[1], 0))
                    f.write("&\n")
        elif mode == 'svg':
            import svgwrite
            dwg = svgwrite.Drawing('result/pattern_linear.svg', profile='tiny')
            stroke = "#000"
            fill = "#ffffff"
            stroke_width = 1
            stroke_linejoin="round"
            stroke_linecap="round"
            for i in range(self.cell_Y_count):
                #print (self.cells[i])
                points = list()
                for j in range(len(self.cells[i])):
                    #print (self.cells[i][j])
                    points.append((self.cells[i][j][0], self.cells[i][j][1]))
                dwg.add(
                    dwg.polyline(
                        points=points,
                        stroke=stroke,
                        fill=fill,
                        stroke_width=stroke_width,
                        stroke_linejoin=stroke_linejoin,
                        stroke_linecap=stroke_linecap
                        )
                    )
            dwg.save()
