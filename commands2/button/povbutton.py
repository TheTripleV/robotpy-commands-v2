from wpilib import Joystick

from .button import Button


class POVButton(Button):
    """
    A class used to bind command scheduling to joystick POV presses.
    Can be composed with other buttons with the operators in Trigger.

    @see Trigger
    """

    def __init__(self, joystick: Joystick, angle: int, povNumber: int = 0) -> None:
        """
        Creates a POVButton that commands can be bound to.

        :param joystick: The joystick on which the button is located.
        :param angle: The angle of the POV corresponding to a button press.
        :param povNumber: The number of the POV on the joystick.
        """
        super().__init__(lambda: joystick.getPOV(povNumber) == angle)
