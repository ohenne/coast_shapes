import shapefile
import csv

##### INPUT
sf = shapefile.Reader(r'//Users/olgahenneberg/Documents/land-polygons-complete-4326/land_polygons.shp')
number_shapes = len(sf.shapes())
filename = 'coast_points_shape68068.csv'
print('number of shapes imported: ', len(sf.shapes()))

##### OUTPUT
with open(filename, mode='w') as csvFile:
    writer = csv.writer(csvFile, delimiter=',')
    writer.writerow(['shape_id', 'point_id', 'lon', 'lat'])

#### get coast lines
polygon_number = 0
total_points = 0
considered_points = 0
considered_shapes = 0
outdata = []
# loop through every shape
land_polygon = sf.shapes()[68067]
polygon_number = 68068
points = land_polygon.points
number_of_points = len(points)
total_points += number_of_points
# print('number of points: ', len(points))
# its ok to cross a rectangular island
#if number_of_points > 1000:
print('at polygon ', polygon_number)
# loop through all points of one shape and store in output
# why loop trough it ?
considered_points += number_of_points
considered_shapes += 1

point_id = range(number_of_points)
#output = [[str(polygon_number)]*number_of_points, ]
if number_of_points > 10: 
        for ipt in range(number_of_points-1):
            with open(filename, 'a') as csvFile:
                writer = csv.writer(csvFile)
                writer.writerow([str(polygon_number), str(ipt), str(points[ipt][0]), str(points[ipt][1])])


csvFile.close()
print(total_points, ' points in total')
print(considered_points, ' points considered')
print(number_shapes, ' shapes imported')
print(considered_shapes, ' shapes considered')
