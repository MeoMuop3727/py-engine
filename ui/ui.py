import pygame
from dataclasses import dataclass, field
from typing import Optional, Callable

from libs.pce.systems import (
    GameObject, 
    Transform
)
from libs.pce.utils import apply_instance

@dataclass(slots=True)
class CSS_StyleType: 

    """
    Base style container for UI elements.

    Intended to be subclassed rather than used directly. Defines the
    common style fields shared by every UI type (transform,
    visibility), which concrete UI styles extend with their own
    fields (e.g. color, border, font). Instances of this type are
    used both as the default/restore style and as the "live",
    state-modified style of a `UserInterfaceType`.

    Attributes:
        transform (Transform): The position, scale, and rotation of
            the UI element.
        visible (bool): Whether the UI element is rendered.
    """

    transform: Transform = field(default_factory=Transform)
    visible: bool = True

class UserInterfaceType(GameObject):

    """
    Base class for all UI elements built on the engine's game object system.

    Intended to be subclassed rather than used directly. A
    `UserInterfaceType` wraps a `CSS_StyleType` describing its visual
    style and exposes a set of state methods (`hovered`, `pressed`,
    `actived`, `enabled`, `disabled`, `focused`) representing the
    different interaction states a UI element can be in. Subclasses
    implement these state methods to modify `_modified_style` based
    on their own conditions (e.g. mouse collision, click state), and
    implement `_render` to draw the element according to its current
    style.

    Two style instances are kept:
        - `_style`: the default/original style, used to restore the
          UI after a temporary state ends. Must not be mutated.
        - `_modified_style`: the live style actually used for
          rendering, updated by the state methods to reflect the
          UI's current state (hovered, pressed, disabled, etc.).

    Attributes:
        func (Callable[[], None]): The callback function associated
            with this UI element (e.g. invoked on interaction).
            Must be assigned by the subclass or user; unset by
            default.
    """

    def __init__(self, 
                 surface: pygame.Surface,
                 style: Optional[CSS_StyleType] = None,
                 audios = None, 
                 animations = None, 
                 connections = None):
        super().__init__(surface, audios, animations, None, connections)

        self.func: Callable[[], None] = ...

        self._style = apply_instance(CSS_StyleType(), style)            # Default css style of UI
                                                                        # It helps restore default style after new states of UI is end
                                                                        # Must not change anything in here
        
        self._modified_style = apply_instance(CSS_StyleType(), style)   # Modified css style of UI
                                                                        # It save and can be changed to be suitable with the current state of UI
                                                                        # Shouldd use it to apply all changes, eg hovered, pressed, etc, for UI

    # States machine
    # All states of a UI
    # Set up your condition and update new style for `_modified_style`
    # Those funcs must be called in update/render in scene
    def hovered(self, style: CSS_StyleType, /): 
        """ `Hovering` the UI. """
        ...
    def pressed(self, style: CSS_StyleType, /): 
        """ `Hovering` and `Pressing` the UI. """
        ...
    def actived(self, style: CSS_StyleType, /): 
        """ Two states, `on` and `off`, to act the state. """
        ...
    def enabled(self, style: CSS_StyleType, /): 
        """ Can be considered likely `default` state of UI, can interacte with UI. """
        ...
    def disabled(self, style: CSS_StyleType, /): 
        """ By constract with enabled, cannot interacte with the UI. """
        ...
    def focused(self, style: CSS_StyleType, /): 
        """ After `pressing`, the state cannot change (`off`) until having another condition to turn off. """
        ...

    # Render
    # This function must be called in update/render func in UI
    # Function will render state of UI
    def _render(self): ...

    # Update
    # This function must be called in update/render func in scene
    def update(self): 
        """ This `function` must be called in update/render func in `scene`. """
        ...

    # Emit
    # Active all other connections
    def emit(self): 
        """ Active all other `connections`. """
        ...

