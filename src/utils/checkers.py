"""Checker modules utils.
"""
import pathlib

from base.checker import BaseChecker

path = pathlib.Path(__file__).parent.parent.resolve()


def get_checkers() -> list[str]:
    """Gets list of checkers in the format of a Python module import"""
    checkers = [
        checker.resolve().as_posix().split("/")[-1].removesuffix(".py").replace("-", ".").capitalize()
        for checker in path.glob("checkers/*.py")
    ]

    return checkers


def get_checker(name:str, kwargs:dict={}) -> BaseChecker:
    """Imports a checker module and returns it's Checker class"""
    module = __import__(f"checkers.{name.replace('.', '-').lower()}", fromlist=[None])
    checker = module.Checker(**kwargs)

    return checker
