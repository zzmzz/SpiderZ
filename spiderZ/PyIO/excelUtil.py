import csv
import time

class ExcelUtil():
    @staticmethod
    def writefile(path, list):
        with open(path + '/result'+str(time.strftime("%Y%m%d%H%M%S",time.localtime()))+'.csv', 'wb') as csvfile:
            spamwriter = csv.writer(csvfile,dialect='excel')
            spamwriter.writerow(["text","count"])
            for row in list:
                excelRow = []
                for key in row.keys():
                    excelRow.append(row[key])
                spamwriter.writerow(excelRow)
