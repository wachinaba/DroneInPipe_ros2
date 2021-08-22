import sys

from PyQt5.QtWidgets import QApplication, QMainWindow

from point_editor import PointEditor

class MainWindow(QMainWindow):
  def __init__(self):
    super().__init__()
    self.points = []
    self.editor = PointEditor(self.points)
    self.setCentralWidget(self.editor)

def main():
  app = QApplication(sys.argv)

  window = MainWindow()
  window.show()

  app.exec()

if __name__ == "__main__":
  main()