def main():
    # print(f'Column 1 \t Column 2')
    # print()

    cols = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    rows = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    

    Column = ''
    Row = ''
    for col in cols:
        a = col + col
        Column += f'\t {col}'
        Row += f'\t {a}'
        

    for row in rows:
        Row += f'\n {row}'
            
    print(Column)
    print(Row)

if __name__ == '__main__':
    main()