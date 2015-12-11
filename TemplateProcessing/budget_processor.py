import csv
import os

output_data = [
        ['cost_center', 'account', 'month', 'value'],
    ]

cc_prefix = "CC"
months = [  'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
            'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

files = []

for newfile in os.listdir(os.getcwd()):
    extns = newfile.split(".")
    if len(extns) == 2 and extns[-1] == "csv" and extns[0].startswith("CC"):
        files.append(newfile)
        print (newfile)

for afile in files:
    next_cc_name = afile.split('_')[0]
    cost_center = next_cc_name[next_cc_name.find(cc_prefix)+len(cc_prefix):]
    with open(afile, newline='') as csvfile:
        budgetreader = csv.reader(csvfile, delimiter='.', quotechar='"')
        for row in budgetreader:
            rowdata = (','.join(row))
            row_data_list = rowdata.split(',')
            for col in range(1, 13):
                try:
                    int(row_data_list[col])
                except:
                    continue
                new_csv_row = [ cost_center,
                                row_data_list[0],
                                months[col-1],
                                row_data_list[col]]
                output_data.append(new_csv_row)

with open('output.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(output_data)
