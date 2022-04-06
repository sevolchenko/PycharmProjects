import sys

from SettingsDialog import SettingsDialog
from AboutDialog import AboutDialog

from MainWindowUI import Ui_MainWindow as MainWindowUI

from PyQt5.QtGui import QPainter, QStandardItemModel, QKeyEvent, QFont, QResizeEvent
from PyQt5.QtWidgets import QMainWindow, QItemDelegate, QStyleOptionViewItem
from PyQt5.QtCore import QModelIndex, Qt

from Game import *


class MainWindow(QMainWindow, MainWindowUI):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

        self.settings_dialog = SettingsDialog()
        self.about_dialog = AboutDialog()

        self._game = QuadrotecaGame(int(self.spin_level.value()), self.settings_dialog.shake_count)

        class MyDelegate(QItemDelegate):
            def __init__(self, parent=None, *args):
                QItemDelegate.__init__(self, parent, *args)

            def paint(self, painter: QPainter, option: QStyleOptionViewItem, idx: QModelIndex):
                painter.save()
                self.parent().on_item_paint(idx, painter, option)
                self.parent().try_paint_on_win(painter)
                painter.restore()

        self.tableView.setItemDelegate(MyDelegate(self))

        self.tableView.setModel(QStandardItemModel(5, 5))

        self.button_restart.clicked.connect(self.on_new_game)
        self.spin_level.valueChanged.connect(self.on_new_game)

        self.tableView.keyPressEvent = self.on_key_pressed
        self.tableView.resizeEvent = self.resize_table
        self.resizeEvent = self.resize_table

        self.actionNew_Game.triggered.connect(self.on_new_game)
        self.actionSettings.triggered.connect(self.on_settings)
        self.actionAbout.triggered.connect(self.on_about)
        self.actionExit.triggered.connect(self.on_exit)

        self.update_view()

    def on_item_paint(self, e: QModelIndex, painter: QPainter, option: QStyleOptionViewItem) -> None:
        r, c = e.row(), e.column()

        background = Qt.white
        if self._game.selected_row <= r < self._game.selected_row + 3 and self._game.selected_col <= c < self._game.selected_col + 3:
            background = Qt.darkBlue
        painter.setBrush(background)
        painter.drawRect(option.rect)

        data = self._game[r, c].data
        painter.setBrush(self.settings_dialog.colors[data])
        painter.drawEllipse(option.rect)

    def update_view(self):
        self.tableView.viewport().update()
        self.label_moves.setText('moves: {0}'.format(self._game.count_of_moves))
        self.label_rotates.setText('rotates: {0}'.format(self._game.count_of_rotations))
        self.label_cols.setText('ready columns: {0}/5'.format(self._game.count_of_ready_cols))
        self.tableView.setFocus()

    def on_new_game(self):
        self._game = QuadrotecaGame(int(self.spin_level.value()), self.settings_dialog.shake_count)
        self.update_view()

    def on_key_pressed(self, e: QKeyEvent):
        key = e.key()
        if key == Qt.Key_Up:
            self._game.moving_key_pressed(-1, 0)
        elif key == Qt.Key_Down:
            self._game.moving_key_pressed(1, 0)
        elif key == Qt.Key_Left:
            self._game.moving_key_pressed(0, -1)
        elif key == Qt.Key_Right:
            self._game.moving_key_pressed(0, 1)
        elif key == Qt.Key_X or key == 1063:
            self._game.rotation_key_pressed(True)
        elif key == Qt.Key_Z or key == 1071:
            self._game.rotation_key_pressed(False)
        self.update_view()

    def resize_table(self, e: QResizeEvent = None):
        self_geom = self.geometry()
        vert_geom = self.rightWidget.geometry()
        self.tableView.resize(int(0.9 * min(vert_geom.x(), self_geom.height())), int(0.9 * min(vert_geom.x(), self_geom.height())))
        table_geom = self.tableView.geometry()
        for i in range(5):
            self.tableView.setColumnWidth(i, int(table_geom.width() // 5))
            self.tableView.setRowHeight(i, int(table_geom.height() // 5))

    def try_paint_on_win(self, painter: QPainter):
        if self._game.state == GameState.WIN:
            painter.fillRect(self.tableView.rect(), self.settings_dialog.colors[0])
            painter.setFont(QFont('Bahnschrift', int(self.tableView.rect().size().width()) // 13))
            painter.drawText(self.tableView.rect(), Qt.AlignCenter, 'congratulations!\nyou solve the puzzle')

    def on_settings(self):
        self.settings_dialog.show()

    def on_about(self):
        self.about_dialog.show()

    def on_exit(self):
        sys.exit(self)


    # cd C:\Users\loide\AppData\Local\Programs\Python\Python310
    # python -m PyQt5.uic.pyuic -x C:\Users\loide\PycharmProjects\task5\MainWindow.ui -o C:\Users\loide\PycharmProjects\task5\MainWindowUI.py
