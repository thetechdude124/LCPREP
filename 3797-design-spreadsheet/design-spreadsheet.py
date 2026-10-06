import string

class Spreadsheet:

    '''
    store spreadhseet in a hashmap of hashmaps
    hashmap maps row idx to columns

    '''

    def __init__(self, rows: int):
        self.sheet = {}

    def setCell(self, cell: str, value: int) -> None:
        col = cell[0]
        row = cell[1:]
        if row not in self.sheet:
            self.sheet[row] = self.getNewRowMap()
        self.sheet[row][col] = value

    def resetCell(self, cell: str) -> None:
        col = cell[0]
        row = cell[1:]
        # if not in the dictionary don't need to do anything
        if row in self.sheet:
            self.sheet[row][col] = 0
        
    def getValue(self, formula: str) -> int:
        first_coord, second_coord = formula[1:].split("+")
        res = 0
        for coord in [first_coord, second_coord]:
            if not coord[0].isupper(): #must be a number then
                res += int(coord)
                continue
            col = coord[0]
            row = coord[1:]
            if row not in self.sheet:
                res += 0
            else: res += self.sheet[row][col]
        return res

    def getNewRowMap(self):
        # helper function to create a new column hashmap for every row
        new_col_hash = {c : 0 for c in string.ascii_uppercase}
        return new_col_hash
    



# Your Spreadsheet object will be instantiated and called as such:
# obj = Spreadsheet(rows)
# obj.setCell(cell,value)
# obj.resetCell(cell)
# param_3 = obj.getValue(formula)