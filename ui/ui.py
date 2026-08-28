from typing import Optional
from libs.pce.systems import GameObject, Transform
from libs.pce.utils import apply_instance

class UserInterfaceType(GameObject):
    def __init__(self, 
                 surface = None, 
                 transform: Optional[Transform] = None,
                 audios = None, 
                 animations = None):
        super().__init__(surface, audios, animations, None, None)
        self.transform = apply_instance(Transform, transform)
