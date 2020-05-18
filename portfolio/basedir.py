import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


print('Base directory is: %s' % (BASE_DIR))

quit_ = False
while not quit_:
    quit_ = input('Enter q to quit: ').lower()
    if quit_ == 'q':
        quit_ = True
