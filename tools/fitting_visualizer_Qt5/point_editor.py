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

  def drawGrid(rect: QtCore.QRect, grid_style: GridStyle):
    linenum_x = int(rect.width / (grid_style.grid_size*2))
    linenum_y = int(rect.height / (grid_style.grid_size*2))

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
    painter = QtGui.QPainter(self)

    # fill background in lightGray
    brush_bg = QtGui.QBrush()
    brush_bg.setColor(QtGui.QColor("lightGray"))
    brush_bg.setStyle(Qt.SolidPattern)
    rect = QtCore.QRect(0, 0, painter.device().width(), painter.device().height())
    painter.fillRect(rect, brush_bg)

    #draw a grid
    ##prepare brushes
    pen_grid = QtGui.QPen()
    pen_grid.setColor(QtGui.QColor("black"))
    pen_subgrid = QtGui.QPen()
    pen_subgrid.setColor(QtGui.QColor("gray"))

    ##calc grid lines (a half number of all lines)
    linenum_x = int(painter.device().width() / (self.GRID_SIZE*2))
    linenum_y = int(painter.device().height() / (self.GRID_SIZE*2))

    ##calc origin
    center_x = painter.device().width() / 2
    center_y = painter.device().height() / 2
    origin_x = center_x - linenum_x * self.GRID_SIZE
    origin_y = center_y - linenum_y * self.GRID_SIZE

    print("{0}, {1}, {2}, {3}".format(center_x, center_y, origin_x, origin_y))

    ##draw grid lines
    for j in range(self.SUBGRID_NUM):
      if j == 0: #if main grid
        painter.setPen(pen_grid)
      else:
        painter.setPen(pen_subgrid)
      for i in range(-1, linenum_x*2+1):
        displ = (i + j / self.SUBGRID_NUM) * self.GRID_SIZE
        ql = QtCore.QLine(origin_x + displ, 0, origin_x + displ, painter.device().height())
        painter.drawLine(ql)
      for i in range(-1, linenum_y*2+1):
        displ = (i + j / self.SUBGRID_NUM) * self.GRID_SIZE
        ql = QtCore.QLine(0, origin_y + displ, painter.device().width(), origin_y + displ)
        painter.drawLine(ql)
    