from PyQt6.QtWidgets import QMainWindow, QLabel, QVBoxLayout, QWidget
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QDragEnterEvent, QDropEvent

style_path = 'filemate/resources/styles/styles.css'


class FileDropArea(QLabel):
    def __init__(self):
        super().__init__()
        self.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setText("将文件拖拽到这里")

        # 样式设置
        try:
            with open(style_path, 'r') as f:
                self.setStyleSheet(f.read())
        except FileNotFoundError:
            print(f"警告: 无法找到样式文件 {style_path}")

        self.setProperty("class", "file-drop-area")
        self.setAcceptDrops(True)

    def dragEnterEvent(self, event: QDragEnterEvent):
        if event.mimeData().hasUrls():
            event.accept()
            self.setProperty("class", "file-drop-area drag-over")
        else:
            event.ignore()

    def dragLeaveEvent(self, event: QDragEnterEvent):
        self.setProperty("class", "file-drop-area")

    def dropEvent(self, event: QDropEvent):
        files = [url.toLocalFile() for url in event.mimeData().urls()]
        self.setText("\n".join(files))
        self.setProperty("class", "file-drop-area")


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("FileMate")
        self.setMinimumSize(600, 400)

        # 创建主窗口部件
        main_widget = QWidget()
        self.setCentralWidget(main_widget)

        # 创建布局
        layout = QVBoxLayout()
        main_widget.setLayout(layout)

        # 添加文件拖放区域
        self.drop_area = FileDropArea()
        layout.addWidget(self.drop_area)


if __name__ == '__main__':
    import sys
    from PyQt6.QtWidgets import QApplication

    app = QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit(app.exec())