from abc import ABC, abstractmethod
from typing import Any


class Loss(ABC):
  """
  This is base class of all inherited losses.
  """
  
  @property
  def name(self):
    """
    Get loss name.
    """
    return self.__name
  
  def coefficient(self):
    """
    Get coefficient.
    """
    return self.__coefficient

  def __init__(self, name: str = "default", coefficient: float = 1.0, *args: Any, **kwargs: Any) -> None:
    """
    Constructor.
    :param name:        name of loss function.
    :param coefficient: coefficient factor.
    :param args:        addition arguments.
    :param kwargs:      additional keyword arguments.
    """
    super().__init__()
    self.__name = name
    self.__coefficient = coefficient

  @abstractmethod
  def __call__(self, *args: Any, **kwds: Any) -> Any:
    """
    Compute loss.
    :param args:  additional arguments.
    :param kwds:  additional keyword arguments.
    :return:      computed loss value.
    """
    return NotImplemented()