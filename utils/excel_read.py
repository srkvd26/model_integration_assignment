import openpyxl

class ExcelRead:
    @staticmethod
    def read(file_path):
        wb = openpyxl.load_workbook(file_path, data_only=True)
        sheet = wb.active
        headers = [cell.value for cell in sheet[1]]
        data = []

        for row in sheet.iter_rows(min_row=2, values_only=True):
            row_dict = {}
            for h, v in zip(headers, row):
                if v is None:
                    row_dict[h] = ""
                else:
                    val = str(v).strip()
                    # Remove wrapping quotes if present
                    if val.startswith('"') and val.endswith('"'):
                        val = val[1:-1]
                    row_dict[h] = val
            data.append(row_dict)

        return data
