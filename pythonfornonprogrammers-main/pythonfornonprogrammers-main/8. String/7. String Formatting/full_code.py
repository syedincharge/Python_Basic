#   Created by Elshad Karimov
#   Copyright © AppMillers. All rights reserved.
#   www.appmillers.com

# String Formatting


error_no = 45457984738
name = 'Edy'

# print('Hello, {}'.format(name))

# print('Hey {}, there is a 0x{:x} error!'.format(name, error_no))
print('Hey {name}, there is a 0x{error_no:x} error!'.format(error_no=error_no, name=name))
print(f'Hey {name}, there is a {error_no:#x} error!')

