from typing import Any, Optional

def round(f: Any): ...
def _float_check_precision(precision_digits: Optional[Any] = ..., precision_rounding: Optional[Any] = ...): ...
def float_round(value: Any, precision_digits: Optional[Any] = ..., precision_rounding: Optional[Any] = ..., rounding_method: str = ...): ...
def float_is_zero(value: Any, precision_digits: Optional[Any] = ..., precision_rounding: Optional[Any] = ...): ...
def float_compare(value1: Any, value2: Any, precision_digits: Optional[Any] = ..., precision_rounding: Optional[Any] = ...): ...
def float_repr(value: Any, precision_digits: Any): ...
_float_repr = float_repr

def float_split_str(value: Any, precision_digits: Any): ...
def float_split(value: Any, precision_digits: Any): ...
