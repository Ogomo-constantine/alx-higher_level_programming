#!/usr/bin/python3
class MyInt(int):
    """
    Represents a rebel integer, with == and != operators inverted.
    """

    def __eq__(self, other):
        """
        Inverts the == operator.

        Args:
            other: The value to compare with.

        Returns:
            True if self and other are not equal, False otherwise.
        """
        return super().__ne__(other)

    def __ne__(self, other):
        """
        Inverts the != operator.

        Args:
            other: The value to compare with.

        Returns:
            True if self and other are equal, False otherwise.
        """
        return super().__eq__(other)
