def decode_hidden_message(input_file):
    # Input file
    with open(input_file, 'r') as file:
        lines = file.readlines()

    # Extract numbers and words from every single line
    pyramid_data = [(int(line.split()[0]), line.split()[1]) for line in lines]

    # Pyramid structure
    pyramid = []
    current_number = 1
    while pyramid_data:
        row = [word for number, word in pyramid_data if number == current_number]
        if not row:
            return "Invalid input: Pyramid structure is not complete"
        pyramid.append(row)
        current_number += 1
        pyramid_data = [(number, word) for number, word in pyramid_data if number != current_number]

    # Pyramid lines
    message_words = [line[-1] for line in pyramid]

    # Return the decoded message
    return ' '.join(message_words)

# Test with the provided example
input_file = "input.txt"
decoded_message = decode_hidden_message(input_file)
print(decoded_message)