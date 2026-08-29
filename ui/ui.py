import pygame
from dataclasses import dataclass, field
from typing import Optional

from libs.pce.systems import (
    GameObject, 
    Transform
)
from libs.pce.utils import apply_instance

@dataclass(slots=True)
class CSS_StyleType: 
    transform: Transform = field(default_factory=Transform)
    visible: bool = True

class UserInterfaceType(GameObject):
    def __init__(self, 
                 surface: pygame.Surface,
                 style: Optional[CSS_StyleType] = None,
                 audios = None, 
                 animations = None, 
                 connections = None):
        super().__init__(surface, audios, animations, None, connections)

        self._style = apply_instance(CSS_StyleType(), style)            # Default css style of UI
                                                                        # It helps restore default style after new states of UI is end
                                                                        # Must not change anything in here
        
        self._modified_style = apply_instance(CSS_StyleType(), style)   # Modified css style of UI
                                                                        # It save and can be changed to be suitable with the current state of UI
                                                                        # Shouldd use it to apply all changes, eg hovered, pressed, etc, for UI

    # States machine
    # All states of a UI
    # Function render all different states of UI
    def hovered(self, style: CSS_StyleType): 
        self._modified_style = style
    def pressed(self, style: CSS_StyleType): 
        self._modified_style = style
    def actived(self, style: CSS_StyleType): 
        self._modified_style = style
    def enabled(self, style: CSS_StyleType): 
        self._modified_style = style
    def disabled(self, style: CSS_StyleType): 
        self._modified_style = style

    # Render
    # This function must be called in update func in UI
    # Function render default state of UI
    def _render(self): ...

    # Update
    # This function must be called in update func in scene
    def update(self): ...
