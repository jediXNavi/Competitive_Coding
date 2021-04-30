def generate(numRows):
    pascals_tri = []

    if numRows == 0:
        return pascals_tri
    pascals_tri.append([1])
    for i in range(1, numRows):
        prevRow = pascals_tri[i-1]
        newRow = []
        newRow.append(1)

        for j in range(1, len(prevRow)):
            newRow.append(prevRow[j-1]+prevRow[j])

        newRow.append(1)
        pascals_tri.append(newRow)

    return pascals_tri



