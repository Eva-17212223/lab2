from unittest.mock import patch
from src import calculator


def test_addition_integration(capsys):
    """Test normal addition and exit."""
    user_inputs = ['1', '5', '3', 'n']
    with patch('builtins.input', side_effect=user_inputs):
        calculator.main()
    captured = capsys.readouterr()
    assert "Addition result: 8.0" in captured.out


def test_invalid_choice_then_exit(capsys):
    """Test handling of invalid menu choice before a valid operation."""
    # Invalid choice (9) → then subtraction (2) with inputs 2 and 2 → then exit
    user_inputs = ['9', '2', '2', '2', 'n']
    with patch('builtins.input', side_effect=user_inputs):
        calculator.main()
    captured = capsys.readouterr()
    assert "Invalid choice" in captured.out
    assert "Subtraction result: 0.0" in captured.out


def test_divide_by_zero(capsys):
    """Test divide-by-zero handling and graceful recovery."""
    # Division 10 / 0 → error → try again → valid division → exit
    user_inputs = [
        '4', '10', '0',      # divide by zero
        '4', '8', '2',       # valid division
        'n'                  # exit
    ]
    with patch('builtins.input', side_effect=user_inputs + ['n'] * 3):
        calculator.main()
    captured = capsys.readouterr()
    assert "Error" in captured.out
    assert "zero" in captured.out.lower()
    assert "Division result: 4.0" in captured.out


def test_non_numeric_input(capsys):
    """Test handling of non-numeric inputs and recovery."""
    # Addition with invalid numbers first, then valid input
    user_inputs = [
        '1', 'a', 'b',       # invalid attempt
        '1', '3', '4',       # valid addition
        'n'                  # exit
    ]
    with patch('builtins.input', side_effect=user_inputs + ['n'] * 3):
        calculator.main()
    captured = capsys.readouterr()
    assert "Invalid input. Please enter numeric values only." in captured.out
    assert "Addition result: 7.0" in captured.out
