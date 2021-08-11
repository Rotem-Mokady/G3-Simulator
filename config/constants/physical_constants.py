#  here we define all our physical parameters in the project


class Pipe:
    """
    Long pipe outside of the machine itself, from the irrigation pipe on the ground to machine on underground.
    """
    RADIUS_METERS = 0.0262
    DIAMETER_METERS = 2 * RADIUS_METERS


class Piston:
    """
    The water pusher inside of the machine.
    """
    RADIUS_METERS = 0.045
    DIAMETER_METERS = 2 * RADIUS_METERS


class PushRod:
    """
    Rod that push the piston up and down.
    """
    RADIUS_METERS = 0.02


class Water:
    """
    Water as general material, in 25 celsius degrees.
    """
    NI = 9.1 * 10**(-7)
    WATER_DENSITY = 997.07  # for 25 celsius degrees


class Earth:
    GRAVITY = 9.80665
