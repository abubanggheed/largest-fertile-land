from calculate_land import Land_Plot

def largest_fertile_land(input_string):
    input_list = input_string.splitlines()
    plot_matrix = []
    i = 1
    m_end = input_list[0][0] + 1
    while i < m_end:
        plot_matrix.append(input_list[i])
        i += 1
    out_string = ''
    i += 1
    while i < len(input_list):
        top_row = input_list[i][0]
        bottom_row = input_list[i][-1]
        plot = Land_Plot(plot_matrix[top_row:bottom_row], 'F')
        out_string += str(plot.process_all_rows()) + '\n'
        i += 1
    return out_string