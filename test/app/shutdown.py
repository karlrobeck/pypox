from fastapi import FastAPI


def __call__(app: FastAPI) -> None:
    """
    A special method that allows an instance of the class to be called as a function.

    Parameters:
    - app: An instance of the FastAPI class.

    Returns:
    - None

    """
    print("system shutting down...")
