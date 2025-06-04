# Caesar Cipher Program

A Python implementation of the Caesar Cipher encryption and decryption algorithm.

## How to Execute

1. **Save the code**: Save the Python code as `caesar_cipher.py`

2. **Run the program**:
   ```bash
   python caesar_cipher.py
   ```

3. **Follow the interactive menu**:
   - The program first shows a demonstration with examples
   - Then presents a menu with options:
     - `1` - Encrypt a message
     - `2` - Decrypt a message  
     - `3` - Exit the program

4. **Input requirements**:
   - Enter your text message when prompted
   - Enter a shift value between 0-25
   - The program validates input and handles errors

## How the Code Works

### Core Algorithm

The Caesar Cipher works by shifting each letter in the alphabet by a fixed number of positions:

- **Encryption**: Each letter moves forward in the alphabet
- **Decryption**: Each letter moves backward in the alphabet

### Key Functions

**`caesar_encrypt(text, shift)`**
- Takes input text and shift value
- Processes each character individually
- For alphabetic characters: calculates new position using ASCII values and modulo arithmetic
- Non-alphabetic characters (spaces, punctuation, numbers) remain unchanged
- Preserves case (uppercase/lowercase)

**`caesar_decrypt(text, shift)`**
- Uses the encrypt function with negative shift value
- Reverses the encryption process

**`get_user_input()`**
- Interactive menu system
- Input validation for shift values (0-25)
- Error handling for invalid inputs

**`demonstrate_cipher()`**
- Shows example encryptions and decryptions
- Demonstrates the algorithm with different shift values

### Technical Details

1. **ASCII Conversion**: Uses `ord()` to convert characters to ASCII values
2. **Modulo Arithmetic**: `% 26` ensures wrapping around the alphabet (A-Z, a-z)
3. **Case Handling**: Separate ASCII offsets for uppercase (65) and lowercase (97)
4. **Character Reconstruction**: Uses `chr()` to convert back to characters

### Example

```
Input: "Hello World!" with shift 3
Process: H→K, e→h, l→o, l→o, o→r (space stays), W→Z, etc.
Output: "Khoor Zruog!"
```

### Features

- Handles both uppercase and lowercase letters
- Preserves non-alphabetic characters
- Input validation and error handling
- Interactive user interface
- Demonstration mode with examples
- Wrap-around encryption (Z+1 = A)