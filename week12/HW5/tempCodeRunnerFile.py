import os,pandas, numpy, json

def convert_clomn_to_text(folder_panth):
    for filename in os.listdir(folder_panth):
        if filename.endswith('.csv'):
            csv_path = os.path.join(folder_panth, filename)
            column = pandas.read_csv(csv_path,usecols=['Close/Last'])
            values = column['Close/Last'].iloc[1:].str.replace('$','',regex = False).astype(float)

            txt_filename = filename.replace('.csv', '.txt')
            txt_path = os.path.join(folder_panth, txt_filename)

            with open(txt_path, 'w') as txt_file:
                for value in values:
                    txt_file.write(f"{value}\n")

convert_clomn_to_text('week12\HW5')