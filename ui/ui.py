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

class UserInterfaceType(GameObject):
    def __init__(self, 
                 surface: pygame.Surface,
                 style: Optional[CSS_StyleType] = None,
                 audios = None, 
                 animations = None, 
                 connections = None):
        super().__init__(surface, audios, animations, None, connections)
        self.style = apply_instance(CSS_StyleType(), style)

    # States machine
    # All states of a UI
    def hovered(self): ...
    def pressed(self): ...
    def actived(self): ...
    def enabled(self): ...
    def disabled(self): ...

    # Render
    # This function must be called in update func in UI
    def _render(self): ...

    # Update
    # This function must be called in update func in scene
    def update(self): ...
