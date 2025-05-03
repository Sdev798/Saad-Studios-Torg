from PySide6.QtCore import Slot
from PySide6.QtWidgets import QMainWindow, QApplication, QCheckBox, QMessageBox, QPushButton, QGroupBox, QGridLayout, QHBoxLayout, QLabel, QSizePolicy
import pandas as pando
import app
import sys, time, threading


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = app.Ui_MainWindow()
        self.ui.setupUi(self)
        self.completed_task = None
        self.ui.nw_task.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(1))
        self.ui.addtask.clicked.connect(lambda: self.create_new_task(self.ui.taskname_add.text(), change_widget=True))
        tasks = self.check_tasks_file()
        for task in tasks:
            self.create_new_task(task)
        self.ui.webEngineView.stop()

        

    #To-do LSIT FUNCTIONs
    def check_tasks_file(self):
        dt = pando.read_csv("tasks.csv")
        return list(dt["Tasks"])
    @Slot()
    def done_task_function(self, task_obj_name):
        #remove button
        if task_obj_name:
            widget = self.findChildren(QGroupBox, name=task_obj_name)
            widget[0].deleteLater()
        #Play saound
        #Remove task from list

    
    def create_new_task(self, name, change_widget=False, description=None):
        if not name:
            return QMessageBox.information(self, "No task Name", "Please fill required input!", QMessageBox.Ok)
        self.grp_box = QGroupBox(name)
        self.grp_box.setMinimumHeight(20)
        self.grp_box.setObjectName(f"TASK_{name}")
        self.grp_box.setMinimumHeight(100)
        layout_f_grpbox = QHBoxLayout(self.grp_box)
        self.ui.gridLayout_8.addWidget(self.grp_box)
       
        check_button = QPushButton("Incompleted")
        check_button.setCheckable(True)
        check_button.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        check_button.clicked.connect(lambda: self.done_task_function(check_button.parent().objectName()))
        layout_f_grpbox.addWidget(check_button)
        task_text = QLabel(description)
        if change_widget:
            self.ui.stackedWidget.setCurrentIndex(0)
            self.ui.taskname_add.clear()
        if description != None:
            layout_f_grpbox.addWidget(task_text)





if __name__ == "__main__":
    core = QApplication(sys.argv)
    window = Window()
    window.show()
    core.exec()