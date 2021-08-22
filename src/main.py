
from ui.patheditor_ui import Ui_MainWindow
from PyQt5.QtWidgets import (QApplication, QMainWindow, QHBoxLayout, QSpacerItem, 
	QLabel, QListWidgetItem, QWidget, QSizePolicy
)
from PyQt5.QtCore import Qt
import os, sys, ui.images


def get_path(): 
	return os.getenv("PATH")


class AppWindow(Ui_MainWindow):

	def setupUi(self, window):
		super().setupUi(window)
		self.path_list = []
		self._populate_list()
		self._update_path_str()

		self.pushButton_AddDirectory.clicked.connect(self._add_directory)
		self.pushButton_RemoveDirectory.clicked.connect(self._remove_directory)
		self.checkBox_SortDirectories.stateChanged.connect(self._toggle_sort)
		self.checkBox_RemoveDuplicates.stateChanged.connect(self._remove_duplicates)


	def _populate_list(self) -> None:
		path_str = get_path()
		if not path_str:
			return
		for directory in path_str.split(":"): 
			self.path_list.append(directory)
			self._add_directory_to_list(directory)


	def _add_directory(self) -> None:
		self.listWidget.addItem("path entry")
		item = self.listWidget.item(self.listWidget.count()-1)
		self.listWidget.editItem(item)


	def _remove_directory(self) -> None:
		row_item = self.listWidget.currentRow()
		self.listWidget.takeItem(row_item)
	

	def _toggle_sort(self, state) -> None: 
		self.listWidget.setSortingEnabled(not self.listWidget.isSortingEnabled())
		if self.listWidget.isSortingEnabled():
			self.listWidget.sortItems()

		# Manual way...
		self.listWidget.clear()
		self.path_list.sort()
		for i in self.path_list:
			self._add_directory_to_list(i)
		self._update_path_str()


	
	def _remove_duplicates(self, state) -> None:
		self.listWidget.clear()
		if state == Qt.Checked:
			nodups = list(dict.fromkeys(self.path_list))
			for i in nodups:
				self._add_directory_to_list(i)
			self._update_path_str(nodups)
		else:
			for i in self.path_list:
				self._add_directory_to_list(i)
			self._update_path_str()


	def _add_directory_to_list(self, directory) -> None:
		layout = QHBoxLayout(self.centralwidget)
		spacer = QSpacerItem(150, 30, QSizePolicy.Expanding)

		layout.addWidget(QLabel(directory))
		layout.addItem(spacer)
		# layout.addWidget(QPushButton("Edit"))
		widget = QWidget()
		widget.setLayout(layout)
		item = QListWidgetItem(self.listWidget)
		item.setCheckState(Qt.Unchecked)
		self.listWidget.addItem(item)
		self.listWidget.setItemWidget(item, widget)
	

	def _update_path_str(self, path_list=None) -> None:
		if not path_list:
			path_list = self.path_list

		path = ":".join(map(str, path_list))
		self.label_PathOutput.setText(f"PATH={path}")
	

if __name__ == "__main__":
	app = QApplication(sys.argv)
	window = QMainWindow()
	ui = AppWindow()
	ui.setupUi(window)
	window.show()
	sys.exit(app.exec_())