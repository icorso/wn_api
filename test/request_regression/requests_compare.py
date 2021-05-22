import difflib
from os import listdir


def request_compare():
    indexes_to_ignore = ['7', '11', '12', '13', '37', '55', '62', '90']
    mypath = '/home/mf/simulator_regression/'
    prev_version = '5_11_0_0'
    current_version = '6_0_0_0'
    prev_version_files = [f for f in listdir(mypath + prev_version)]
    current_version_files = [f for f in listdir(mypath + current_version)]

    print('Comparing files in directories {} {}'.format(mypath + prev_version + '/', mypath + current_version + '/\n'))

    if prev_version_files == current_version_files:
        for f in prev_version_files:
            is_error = False
            text1 = open(mypath + prev_version + '/' + f).readlines()
            text2 = open(mypath + current_version + '/' + f).readlines()

            print('Comparing file {}'.format(f))
            for line in difflib.unified_diff(text1, text2, n=0):
                if any('idx="{}"'.format(idx) in line for idx in indexes_to_ignore)\
                        or any(el in line for el in ['---', '+++', '@@']):
                    pass
                else:
                    is_error = True
                    print(line)
            if not is_error:
                print('... ok')
    else:
        print('Directories are differs ' + mypath + prev_version + '/ and ' + mypath + current_version
              + '/')
        print(prev_version + ' extra files:')
        print(set(prev_version_files).difference(current_version_files))

        print(current_version + ' extra files:')
        print(set(current_version_files).difference(prev_version_files))

request_compare()
