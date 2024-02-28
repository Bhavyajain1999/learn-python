# Write code here
ini_list = [[1, 2, 3],
            [3, 6, 7],
            [7, 5, 4]]

import functools
functools.reduce(lambda x,y:x+y,ini_list)