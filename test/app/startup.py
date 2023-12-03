from fastapi import FastAPI


def __call__(app: FastAPI):
    """
    A function that is called when the object is invoked as a function.

    Args:
        app (FastAPI): The FastAPI object.

    Returns:
        None: This function does not return anything.
    """
    print("system starting up...")
