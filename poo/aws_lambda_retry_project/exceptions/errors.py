class ThrottleError(Exception):
    """Exception raised when a throttling error occurs (e.g., rate exceeded on AWS CLI)."""

    pass
