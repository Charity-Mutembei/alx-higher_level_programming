#!/usr/bin/python3
"""
a script that reads stdin line by line and computes metrics
"""
if __name__ == '__main__':
        
    import sys


    status_codes = {'200': 0, '301': 0, '400': 0, '401': 0,
                    '403': 0, '404': 0, '405': 0, '500': 0}
    total_file_size = 0
    count = 0

    try:
        for line in sys.stdin:
            count += 1
            split_line = line.split()
            if len(split_line) >= 7:
                status_code = split_line[-2]
                file_size = split_line[-1]
                total_file_size += int(file_size)

                if status_code in status_codes:
                    status_codes[status_code] += 1

            if count % 10 == 0:
                print(f'Total file size: {total_file_size}')
                for code in sorted(status_codes):
                    if status_codes[code] > 0:
                        print(f'{code}: {status_codes[code]}')

    except KeyboardInterrupt:
        print(f'Total file size: {total_file_size}')
        for code in sorted(status_codes):
            if status_codes[code] > 0:
                print(f'{code}: {status_codes[code]}')
