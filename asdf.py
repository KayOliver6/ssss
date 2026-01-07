#!/usr/bin/env python3
"""
A simple asdf utility for keyboard layout testing and text pattern generation.
"""

def asdf_pattern(length=4):
    """
    Generate the classic 'asdf' keyboard pattern.
    
    Args:
        length (int): Number of times to repeat the pattern (default: 4)
    
    Returns:
        str: The asdf pattern repeated
    
    Raises:
        ValueError: If length is negative or not an integer
    """
    if not isinstance(length, int):
        raise ValueError("Length must be an integer")
    if length < 0:
        raise ValueError("Length must be non-negative")
    return "asdf" * length


def asdf_reverse():
    """
    Return the reverse of the asdf pattern.
    
    Returns:
        str: 'fdsa'
    """
    return "fdsa"


def asdf_keyboard_row():
    """
    Return the home row of a QWERTY keyboard.
    
    Returns:
        str: The home row keys
    """
    return "asdfghjkl"


def main():
    """Main function to demonstrate asdf functionality."""
    print("ASDF Utility")
    print("-" * 40)
    print(f"Pattern (4x): {asdf_pattern()}")
    print(f"Pattern (8x): {asdf_pattern(8)}")
    print(f"Reverse: {asdf_reverse()}")
    print(f"Keyboard home row: {asdf_keyboard_row()}")


if __name__ == "__main__":
    main()
