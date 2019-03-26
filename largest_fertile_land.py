from calculate_land import Land_Plot
from rect import Rect

def largest_fertile(input_string):
    input_list = input_string.splitlines()
    plot_matrix = []
    i = 1
    m_end = int(input_list[0][0]) + 1
    while i < m_end:
        plot_matrix.append(input_list[i])
        i += 1
    out_string = ''
    i += 1
    plot = Land_Plot(plot_matrix, 'F')
    plot.process_all_rows()
    rects_to_consider = plot.all_rects
    while i < len(input_list):
        top_row = int(input_list[i][0]) - 1
        bottom_row = int(input_list[i][-1])
        boundary_rect = Rect(0, len(plot_matrix[0]), top_row, bottom_row - 1)
        largest_area = find_largest_area(boundary_rect, rects_to_consider, 0)
        out_string += str(largest_area) + '\n'
        i += 1
    return out_string

def find_largest_area(boundary, rects_list, cropped_area, i = 0):
    if i >= len(rects_list):
        return cropped_area
    elif cropped_area >= rects_list[i].area():
        return cropped_area
    else:
        return find_largest_area(boundary, rects_list, update_cropped(boundary, rects_list[i], cropped_area), i + 1)

def update_cropped(boundary, rect, current_area):
    inner_rect = Rect(rect.lindex, rect.rindex, max([rect.start, boundary.start]), min([rect.end, boundary.end]))
    return max([inner_rect.area(), current_area])