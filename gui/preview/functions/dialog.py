from PyQt5.QtCore import Qt
from qfluentwidgets import MessageBox, InfoBar, InfoBarPosition


def messageDialog(self, title, content):
    w = MessageBox(title, content, self)
    if w.exec_():
        return True
    else:
        return False


def successInfoBar(self, title, content, duration=2000):
    InfoBar.success(
        title=title,
        content=content,
        orient=Qt.Horizontal,
        isClosable=True,
        position=InfoBarPosition.TOP_RIGHT,
        duration=duration,
        parent=self
    )


def errorInfoBar(self, title, content, duration=2000):
    InfoBar.error(
        title=title,
        content=content,
        orient=Qt.Horizontal,
        isClosable=True,
        position=InfoBarPosition.TOP_RIGHT,
        duration=duration,
        parent=self
    )


def warningInfoBar(self, title, content, duration=2000):
    InfoBar.warning(
        title=title,
        content=content,
        orient=Qt.Horizontal,
        isClosable=True,
        position=InfoBarPosition.TOP_RIGHT,
        duration=duration,
        parent=self
    )
