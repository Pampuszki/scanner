class TestExample1:
    """Test Example, in the future, should be removed."""

    def test_addition(self) -> None:
        """Test the addition of two numbers."""
        number_one: int = 1
        number_two: int = 2

        result: int = number_one + number_two
        expected_val = 3
        assert result == expected_val
