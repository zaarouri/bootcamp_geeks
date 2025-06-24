def decode_matrix(matrix_lines):
    # Convert the string into a matrix (list of lists)
    rows = []
    for line in matrix_lines:
        row = []
        for char in line:
            row.append(char)
        rows.append(row)

    # Get number of columns and rows
    num_cols = len(rows[0])
    num_rows = len(rows)

    # Read columns top to bottom
    raw_message = ""
    for col in range(num_cols):
        for row in range(num_rows):
            raw_message += rows[row][col]

    # Build the cleaned message
    result = ""
    i = 0
    while i < len(raw_message):
        if raw_message[i].isalpha():
            result += raw_message[i]
        else:
            # Check if it's between two letters
            if (i > 0 and raw_message[i - 1].isalpha()):
                j = i
                while j < len(raw_message) and not raw_message[j].isalpha():
                    j += 1
                if j < len(raw_message) and raw_message[j].isalpha():
                    result += " "
                    i = j - 1  # move to the char before the next letter
        i += 1

    return result


matrix = [
    "7ii",
    "Tsx",
    "h%?",
    "i #",
    "sM ",
    "$a ",
    "#t%",
    "^r!"
]

message = decode_matrix(matrix)
print(message)
