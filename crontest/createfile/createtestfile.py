
import argparse
import os




def createfile():
    if  os.path.exists(f'test.xls') == False:
        temporary_file_name = os.path.join('test.xls')
        print('ol')

    with open(temporary_file_name, 'a') as f:
        f.write('i was appended')
        print('nope')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description="Fetch campaign finance data from the Oregon ORESTAR system"
    )
    #parser.add_argument('--date', default='9999-12-31', type=parse_date, help='YYYY-MM-DD format')
    args = parser.parse_args()

    createfile()