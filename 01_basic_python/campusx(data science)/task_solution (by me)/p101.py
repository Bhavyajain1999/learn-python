def get_final_line(filename):
    final_line = ''
    for current_line in open(filename, 'r'):
        final_line = current_line
    return final_line

get_final_line("sample.txt")