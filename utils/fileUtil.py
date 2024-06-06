import os

from PyQt5.QtCore import QSettings, QDir
from PyQt5.QtWidgets import QFileDialog


def select_single_file(weight, suffix_filter: str, last_dir_key: str):
    """
    打开单个文件
    :param weight:
    :param suffix_filter:
    :param last_dir_key:
    :return:
    """
    # 历史目录
    settings = QSettings('PyQGIS_Development')
    last_dir = settings.value(last_dir_key, QDir().homePath())

    file_dialog = QFileDialog(weight)
    file_dialog.setWindowTitle('文件选择')
    file_dialog.setNameFilter(suffix_filter)
    file_dialog.setDirectory(last_dir)
    file_dialog.setFileMode(QFileDialog.FileMode.ExistingFile)
    file_dialog.setViewMode(QFileDialog.ViewMode.Detail)

    if file_dialog.exec():
        filenames = file_dialog.selectedFiles()
        filepath = filenames[0]
        # 记录历史目录
        settings.setValue(last_dir_key, os.path.dirname(filepath))
        return filepath

    return ''
