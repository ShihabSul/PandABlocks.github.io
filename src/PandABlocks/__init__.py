from importlib.metadata import version

__version__ = version("PandABlocks")
del version

__all__ = ["__version__"]