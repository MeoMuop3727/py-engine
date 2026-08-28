from .type import IconType
from ._defination import _ICONS

class IconRegister:

    """
    Registry that stores and manages the collection of available icons.

    Wraps a name -> `IconType` mapping, seeded from the built-in `_ICONS`
    definitions, and exposes methods to register, unregister, and look up
    icons by name.
    """

    def __init__(self):

        """
        Initialize the registry with a copy of the built-in icon set.

        A copy of `_ICONS` is used so that mutating this instance's
        registry never affects the shared `_ICONS` dict.
        """

        self._list_icons: dict[str, IconType] = _ICONS.copy()

    def register(self, *icons: IconType):

        """
        Add one or more new icons to the registry.

        Args:
            *icons: One or more `IconType` instances to add.

        Raises:
            TypeError: If any argument is not an `IconType` instance.
            KeyError: If an icon with the same `name` is already registered.
        """

        for index, icon in enumerate(icons):
            if not isinstance(icon, IconType):
                raise TypeError(f"The value at {index!r} is {icon.__name__!r}, not IconType")

            if icon.name in self._list_icons:
                raise KeyError(f"The {icon.name!r} existed")

            self._list_icons[icon.name] = icon

    def unregister(self, *icons: IconType):

        """
        Remove one or more icons from the registry.

        Args:
            *icons: One or more `IconType` instances to remove.

        Raises:
            TypeError: If any argument is not an `IconType` instance.
            KeyError: If an icon with the given `name` is not registered.
        """

        for index, icon in enumerate(icons):
            if not isinstance(icon, IconType):
                raise TypeError(f"The value at {index!r} is {icon.__name__!r}, not IconType")

            if icon.name not in self._list_icons:
                raise KeyError(f"The {icon.name!r} is not existed")

            self._list_icons.pop(icon.name)

    def get_icon(self, name_icon: str) -> IconType:

        """
        Look up a registered icon by name.

        Args:
            name_icon: The `name` of the icon to retrieve.

        Returns:
            The `IconType` instance registered under `name_icon`.

        Raises:
            KeyError: If no icon with `name_icon` is registered.
        """

        if name_icon not in self._list_icons:
            raise KeyError(f"The {name_icon!r} is not existed")
        return self._list_icons[name_icon]