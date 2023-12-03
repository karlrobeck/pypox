async def endpoint(name: str):
    return name

from fastapi import APIRouter

router = APIRouter()

@router.get('')
async def test():
    pass

@router.post('')
async def testt():
    pass