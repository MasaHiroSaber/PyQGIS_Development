from PyQt5.QtCore import QFile


class QSSLoader:
    def __init__(self, path: str) -> None:
        self._path = path

    def load(self) -> str:
        f = QFile(self._path)
        f.open(QFile.ReadOnly | QFile.Text)
        stylesheet = f.readAll()
        return stylesheet.data().decode("utf-8")