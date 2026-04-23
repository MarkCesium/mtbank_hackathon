class AppError(Exception):
    def __init__(self, message: str = "An error occurred"):
        self.message = message
        super().__init__(self.message)


class NotFoundError(AppError):
    def __init__(self, message: str = "Resource not found"):
        super().__init__(message)


class AlreadyExistsError(AppError):
    def __init__(self, message: str = "Resource already exists"):
        super().__init__(message)


class InvalidCredentialsError(AppError):
    def __init__(self, message: str = "Invalid credentials"):
        super().__init__(message)


class DailyLimitExceededError(AppError):
    def __init__(self, message: str = "Daily attempts limit exceeded"):
        super().__init__(message)


class ValidationError(AppError):
    def __init__(self, message: str = "Validation failed"):
        super().__init__(message)
