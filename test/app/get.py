tags = ["test"]



async def endpoint(title: str,db:Session = Depends(session) ) -> str:
    """
    An asynchronous function that takes a string parameter `title` and returns a string.

    This code defines an asynchronous function called endpoint that takes a string parameter title and returns a string. The function simply returns the value of the title parameter.
    """

    return title
