import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QTextEdit, QVBoxLayout, QWidget
from PyQt6.QtCore import Qt


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("파일 드래그 앤 드롭")
        self.setGeometry(100, 100, 400, 300)

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout(self.central_widget)

        self.text_edit = QTextEdit(self)
        self.text_edit.setReadOnly(True)  # 편집 불가능하도록 설정

        self.layout.addWidget(self.text_edit)

        self.text_edit.setAcceptDrops(True)  # 드롭 기능을 활성화

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        files = [url.toLocalFile() for url in event.mimeData().urls()]
        self.process_dropped_files(files)

    def process_dropped_files(self, files):
        if files:
            file_list = "\n".join(files)
            self.text_edit.setText("드롭된 파일 목록:\n" + file_list)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())