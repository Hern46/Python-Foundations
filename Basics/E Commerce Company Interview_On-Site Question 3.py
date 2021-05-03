def rectangles(r1, r2):

    x_overlap = False
    y_overlap = False
    output_rec = {}

    if r2['x'] < r1['x']:
        if abs(r2['x'] - r1['x']) < r2['w']:
            x_overlap = True
            output_rec['w'] = (r2['w'] + r2['x']) - r1['x']
            output_rec['x'] = r1['x']
    else:
        if abs(r2['x'] - r1['x']) < r1['w']:
            x_overlap = True
            output_rec['w'] = (r1['w'] + r1['x']) - r2['x']
            output_rec['x'] = r2['x']

    if r2['y'] < r1['y']:
        if abs(r2['y'] - r1['y']) < r2['h']:
            y_overlap = True
            output_rec['h'] = (r2['h'] + r2['y']) - r1['y']
            output_rec['y'] = r1['y']
    else:
        if abs(r2['y'] - r1['y']) < r1['h']:
            y_overlap = True
            output_rec['h'] = (r1['h'] + r1['y']) - r2['y']
            output_rec['y'] = r2['y']

    if x_overlap and y_overlap:
        return output_rec
    else:
        return False

r1 = {'x': 2 , 'y': 4,'w':5,'h':12}
r2 = {'x': 1 , 'y': 5,'w':7,'h':14}

print(rectangles(r1, r2))

