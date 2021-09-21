#  here we define all our physical dynamic parameters in the project


class Pipe:
    """
    Long pipe outside of the machine itself, from the irrigation pipe on the ground to machine on underground.
    """
    TYPES_TO_E = {
        "PVC, HDPE": 0.015 / 1000,
        "NEW GI": 0.3 / 1000,
        "OLD GI": 3 / 1000,
    }


class Piston:
    """
    The water pusher inside of the machine.
    """
    CURRENT_DOWN_VELOCITIES = [0.0001, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7]