from .base import Loss
from typing import Any
import torch.nn.functional as F


class MLMLoss(Loss):
  """
  Predicts a masked token in a sequence, 
  and the model can attend to tokens bidirectionally.
  """

  def __init__(self, name: str = "mlm", coefficient: float = 1.0, *args: Any, **kwargs: Any) -> None:
    """
    Constructor.
    :param name:        name of loss function.
    :param coefficient: coefficient factor.
    :param args:        addition arguments.
    :param kwargs:      additional keyword arguments.
    """
    super().__init__(name=name, coefficient=coefficient, *args, **kwargs)

  def __call__(self, pred, label, *args: Any, **kwds: Any) -> Any:
    """
    Compute loss.
    :param pred:    predicted values.
    :param label:   label values.
    :param args:    additional arguments.
    :param kwargs:  additional keyword arguments.
    :return:        computed loss value.
    """
    return self.coefficient * F.cross_entropy(
      pred.view(-1, pred.shape[-1]), label.view(-1)
    )
