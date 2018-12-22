import xlwt

def createBool():
    book = xlwt.Workbook()
    return book
def addSheet(sheetName,book):
    sheet = book.add_sheet(sheetName)
    return sheet
def writeData(data,sheet):
    row = 0
    for line in data:
        col = 0
        for value in line:
            sheet.write(row,col,value)
            col+=1
        rwo+=1
def save(book,filename):
    book.save(filename)
