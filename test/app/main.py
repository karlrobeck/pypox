import sys
import os

from fastapi import FastAPI

from pypox.compiler.api import Pypox

app: FastAPI = Pypox(os.path.dirname(__file__))()
