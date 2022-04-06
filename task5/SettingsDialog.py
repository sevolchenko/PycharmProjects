from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QColor, QPixmap, QFont, QMouseEvent
from PyQt5.QtWidgets import QSizePolicy, QColorDialog, QHBoxLayout, QVBoxLayout, QLabel, QSpinBox, QDialogButtonBox, \
    QDialog


class SettingsDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("Settings")

        self.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)

        self.color_choose_dialog = QColorDialog()

        self._colors = [QColor(Qt.red), QColor(Qt.yellow), QColor(Qt.green), QColor(Qt.magenta), QColor(Qt.blue)]
        self._shake_count = 20

        layout = QVBoxLayout()
        colors_layout = QHBoxLayout()

        pixmap = QPixmap(50, 50)
        lab_0 = QLabel()
        pixmap.fill(self._colors[0])
        lab_0.setPixmap(pixmap)
        lab_0.mousePressEvent = self.on_color_clicked_0
        colors_layout.addWidget(lab_0)

        lab_1 = QLabel()
        pixmap.fill(self._colors[1])
        lab_1.setPixmap(pixmap)
        lab_1.mousePressEvent = self.on_color_clicked_1
        colors_layout.addWidget(lab_1)

        lab_2 = QLabel()
        pixmap.fill(self._colors[2])
        lab_2.setPixmap(pixmap)
        lab_2.mousePressEvent = self.on_color_clicked_2
        colors_layout.addWidget(lab_2)

        lab_3 = QLabel()
        pixmap.fill(self._colors[3])
        lab_3.setPixmap(pixmap)
        lab_3.mousePressEvent = self.on_color_clicked_3
        colors_layout.addWidget(lab_3)

        lab_4 = QLabel()
        pixmap.fill(self._colors[4])
        lab_4.setPixmap(pixmap)
        lab_4.mousePressEvent = self.on_color_clicked_4
        colors_layout.addWidget(lab_4)

        colors_layout.addStretch()

        layout_shakes = QHBoxLayout()
        font = QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(20)

        shakes_label = QLabel('Count of shakes: ')
        shakes_label.setFont(font)
        layout_shakes.addWidget(shakes_label)

        self.shakes_counter = QSpinBox()
        self.shakes_counter.setFont(font)
        self.shakes_counter.setValue(self._shake_count)
        self.shakes_counter.setMinimum(5)
        self.shakes_counter.setMaximum(255)
        self.shakes_counter.setSingleStep(10)
        self.shakes_counter.setMaximumSize(QSize(50, 16777215))
        layout_shakes.addWidget(self.shakes_counter)

        self.shakes_counter.valueChanged.connect(self.on_shakes_count_changed)

        buttonBox = QDialogButtonBox(QDialogButtonBox.Ok)
        font.setPointSize(14)
        buttonBox.setFont(font)
        buttonBox.accepted.connect(self.accept)
        buttonBox.rejected.connect(self.reject)

        layout.addLayout(colors_layout)
        layout.addStretch()
        layout.addLayout(layout_shakes)
        layout.addWidget(buttonBox)
        self.setLayout(layout)

    @property
    def colors(self) -> list:
        return self._colors

    @property
    def shake_count(self) -> int:
        return self._shake_count

    def on_shakes_count_changed(self):
        self._shake_count = int(self.shakes_counter.value())


    def on_color_clicked_0(self, e: QMouseEvent):
        self.color_choose_dialog.setCurrentColor(self._colors[0])
        self._colors[0] = self.color_choose_dialog.getColor()
        self.layout().itemAt(0).itemAt(0).widget().pixmap().fill(self._colors[0])

    def on_color_clicked_1(self, e: QMouseEvent):
        self.color_choose_dialog.setCurrentColor(self._colors[1])
        self._colors[1] = self.color_choose_dialog.getColor()
        self.layout().itemAt(0).itemAt(1).widget().pixmap().fill(self._colors[1])

    def on_color_clicked_2(self, e: QMouseEvent):
        self.color_choose_dialog.setCurrentColor(self._colors[2])
        self._colors[2] = self.color_choose_dialog.getColor()
        self.layout().itemAt(0).itemAt(2).widget().pixmap().fill(self._colors[2])

    def on_color_clicked_3(self, e: QMouseEvent):
        self.color_choose_dialog.setCurrentColor(self._colors[3])
        self._colors[3] = self.color_choose_dialog.getColor()
        self.layout().itemAt(0).itemAt(3).widget().pixmap().fill(self._colors[3])

    def on_color_clicked_4(self, e: QMouseEvent):
        self.color_choose_dialog.setCurrentColor(self._colors[4])
        self._colors[4] = self.color_choose_dialog.getColor()
        self.layout().itemAt(0).itemAt(4).widget().pixmap().fill(self._colors[4])