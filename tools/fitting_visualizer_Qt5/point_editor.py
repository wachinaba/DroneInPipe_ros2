from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QWaitCondition, Qt, QtCriticalMsg, center

class GridStyle:
  def __init__(self, grid_size=100, subgrid_num=5, grid_pen=QtGui.QPen(QtGui.QColor("black")), subgrid_pen=QtGui.QPen(QtGui.QColor("gray")), center_pen=QtGui.QPen(QtGui.QColor("red"))):
    self.grid_size = grid_size
    self.subgrid_num = subgrid_num
    self.grid_pen = grid_pen
    self.subgrid_pen = subgrid_pen
    self.center_pen = center_pen

class PointEditorPainter(QtGui.QPainter):
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)

  def drawGrid(self, rect: QtCore.QRect, grid_style: GridStyle):
    linenum_half = QtCore.QPoint(rect.width(), rect.height()) / (grid_style.grid_size*2)
    linenum = linenum_half * 2.5
    origin = rect.center() - linenum_half * grid_style.grid_size

    for j in range(grid_style.subgrid_num):
      if j == 0:
        self.setPen(grid_style.grid_pen)
      else:
        self.setPen(grid_style.subgrid_pen)
      for i in range(-1, linenum.x()):
        displacement = (i + j / grid_style.subgrid_num) * grid_style.grid_size
        ql = QtCore.QLine(origin.x() + displacement, 0, origin.x() + displacement, rect.height())
        self.drawLine(ql)
      for i in range(-1, linenum.y()):
        displacement = (i + j / grid_style.subgrid_num) * grid_style.grid_size
        ql = QtCore.QLine(0, origin.y() + displacement, rect.width(), origin.y() + displacement)
        self.drawLine(ql)
    
    self.setPen(grid_style.center_pen)
    self.drawLine(QtCore.QLine(rect.center().x(), 0, rect.center().x(), rect.height()))
    self.drawLine(QtCore.QLine(0, rect.center().y(), rect.width(), rect.center().y()))

class PointEditor(QtWidgets.QWidget):
  """
  Custom Qt Widget to edit points(scan data).
  """

  GRID_SIZE = 100
  SUBGRID_NUM = 5

  def __init__(self, points, *args, **kwargs):
    super(PointEditor, self).__init__(*args, **kwargs)
    self.points = points

    self.setSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
  
  def sizeHint(self) -> QtCore.QSize:
      return QtCore.QSize(200, 200)

  def paintEvent(self, e):
    painter = PointEditorPainter(self)

    # fill background in lightGray
    brush_bg = QtGui.QBrush()
    brush_bg.setColor(QtGui.QColor("lightGray"))
    brush_bg.setStyle(Qt.SolidPattern)
    rect = QtCore.QRect(0, 0, painter.device().width(), painter.device().height())
    painter.fillRect(rect, brush_bg)

    painter.drawGrid(rect, GridStyle(self.GRID_SIZE, self.SUBGRID_NUM))
