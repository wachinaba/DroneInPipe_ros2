from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QWaitCondition, Qt, QtCriticalMsg

class PointEditor(QtWidgets.QWidget):
  """
  Custom Qt Widget to edit points(scan data).
  """

  def __init__(self, points, *args, **kwargs):
    super(PointEditor, self).__init__(*args, **kwargs)
    self.points = points

    self.setSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
  
  def sizeHint(self) -> QtCore.QSize:
      return QtCore.QSize(200, 200)

  def paintEvent(self, e):
    painter = QtGui.QPainter(self)
    brush_bg = QtGui.QBrush()
    brush_bg.setColor(QtGui.QColor("lightGray"))
    brush_bg.setStyle(Qt.SolidPattern)
    rect = QtCore.QRect(0, 0, painter.device().width(), painter.device().height())
    painter.fillRect(rect, brush_bg)

  

