


class Point(object):
    def __init__(self, x: float=0, y: float=0, z: float=0) -> None:
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)

    def move(self, deltaX: float=0, deltaY: float=0, deltaZ: float=0) -> None:
        self.x += float(deltaX)
        self.y += float(deltaY)
        self.z += float(deltaZ)

    def __str__(self) -> str:
        return f"{self.x} {self.y} {self.z}"