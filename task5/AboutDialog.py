import sys

from PyQt5.QtCore import QUrl, QMetaObject
from PyQt5.QtGui import QFont
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import QDialog, QVBoxLayout, QWidget, QDialogButtonBox, QSizePolicy


class AboutDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("About")

        self.resize(490, 505)

        self.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)

        self.verticalLayout = QVBoxLayout()
        self.centralwidget = QWidget()
        webEngineView = QWebEngineView(self.centralwidget)
        webEngineView.load(QUrl().fromLocalFile(sys.path[0] + '\\about.html'))
        webEngineView.resize(self.contentsRect().width(), self.contentsRect().height())

        buttonBox = QDialogButtonBox(QDialogButtonBox.Ok)
        font = QFont()
        font.setPointSize(14)
        buttonBox.setFont(font)
        buttonBox.accepted.connect(self.accept)
        buttonBox.rejected.connect(self.reject)

        self.verticalLayout.addWidget(self.centralwidget)
        self.verticalLayout.addWidget(buttonBox)

        self.setLayout(self.verticalLayout)