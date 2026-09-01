from typing import Optional, TypeVar, Union, Any

_T = TypeVar("_T")
def apply_value(value: Any, var: Optional[_T] = None) -> Union[_T, Any]:

    """
    Applies a default value to a variable when the variable is None.

    If `var` is None, the function returns `value`; otherwise, it returns
    the value of `var` unchanged.

    Args:
        value: The default object to apply when `var` is None.
        var: The variable to check. If None, `value` is returned.

    Returns:
        The value of `var` if it is not None; otherwise, `value`.

    Example:
        >>> apply_value(10, var)
        ... var

        >>> apply_value(10, var)
        ... 10
    """

    return value if var is None else var 