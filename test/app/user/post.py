from user.schemas import User


async def endpoint(body: User) -> str:
    """
    An asynchronous function that represents an endpoint.

    Args:
        body (User): The request body of the endpoint.

    Returns:
        str: The name of the user.

    This code defines an asynchronous function called endpoint that represents an endpoint in an API. It takes a parameter called body of type User, which represents the request body of the endpoint. The function returns the name of the user as a string.

    """
    return body.name
