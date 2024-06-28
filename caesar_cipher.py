from string import ascii_lowercase, ascii_uppercase
from art import logo

# Print the logo
print(logo)

def caesar(input_text, shift_amount, cipher_direction):
    """
    Encrypts or decrypts the input_text by shifting the letters by shift_amount.
    """
    output_text = ""  # Initialize an empty string for the output
    if cipher_direction == "2":
        shift_amount *= -1  # Reverse the shift for decryption
    for char in input_text:
        if char in ascii_lowercase:
            # Calculate new position with wrapping around the alphabet
            new_position = (ascii_lowercase.index(char) + shift_amount) % 26
            output_text += ascii_lowercase[new_position]
        elif char in ascii_uppercase:
            # Calculate new position with wrapping around the alphabet for uppercase letters
            new_position = (ascii_uppercase.index(char) + shift_amount) % 26
            output_text += ascii_uppercase[new_position]
        else:
            # Keep non-alphabetic characters unchanged
            output_text += char
    print(f"The output text is: {output_text}")

def main():
    should_continue = True
    while should_continue:
        # Get the direction of the cipher from the user
        direction = input("Type '1' to encrypt, type '2' to decrypt:\n")
        if direction not in ["1", "2"]:
            print("Invalid input. Please enter '1' for encrypt or '2' for decrypt.")
            continue
        
        # Get the message to be processed from the user
        text = input("Type your message:\n")
        
        # Get the shift amount and ensure it is within the bounds of the alphabet
        try:
            shift = int(input("Type the shift number:\n")) % 26
        except ValueError:
            print("Invalid input. Please enter a number for the shift amount.")
            continue
        
        # Call the caesar function to process the input text
        caesar(text, shift, direction)
        
        # Ask the user if they want to go again
        will_continue = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()
        if will_continue == "no":
            should_continue = False  # Set the flag to False to exit the loop
            print("Goodbye!")  # Print goodbye message

if __name__ == "__main__":
    main()
