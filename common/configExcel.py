import xlrd


class Excel():
    def __init__(self, file_name = None, sheet_id = None):
        self.file_name = file_name
        self.sheet_id = sheet_id
        self.data = self.get_data()

    def get_data(self):
        data = xlrd.open_workbook(self.file_name)
        tables = data.sheets()[self.sheet_id]
        return tables

    def get_value(self, row, col):
        return self.data.cell_value(row, col)


