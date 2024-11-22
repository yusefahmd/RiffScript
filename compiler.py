

# This is a extension on the tabs_parser.extract_string_notes function in tabs2music, allowing for code compilation
# TODO: explain what it does
def compiler(tabs_notes):
    notes = []
    i = 1  # Start from the second character (index 1), skips the first "-"
    while i < len(tabs_notes):
        # Check if it's a digit and capture the full number
        if tabs_notes[i].isdigit():
            num_str = tabs_notes[i]
            # Look ahead to capture the full number if it spans multiple characters
            while i + 1 < len(tabs_notes) and tabs_notes[i + 1].isdigit():
                i += 1
                num_str += tabs_notes[i]
            notes.append(int(num_str))  # Append the full number as an integer
        elif tabs_notes[i] in ["~", "-"]:
            notes.append(tabs_notes[i])  # Append "~", or "-"
        
        # Move to the next second character in the pair (skip the current '-')
        i += 2