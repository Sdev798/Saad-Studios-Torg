import datetime
import os
from PySide6.QtGui import QKeySequence
from PySide6.QtCore import Qt
from PySide6.QtCore import Slot
from PySide6.QtWidgets import QMainWindow, QApplication, QCheckBox, QMessageBox, QPushButton, QGroupBox, QGridLayout, QHBoxLayout, QLabel, QSizePolicy
import pandas as pando
import app
import sys, time, threading, json


class POMODORO:
    def __init__(self, working_task=None):
        #Gather Settings
        self.pomo_settings = None
        try:
            with open("tmsettings.json", "r+") as tm_settings_f:
                self.pomo_settings = json.loads(tm_settings_f.read())
        except FileNotFoundError:
            default_pomo_settings = {"pomo":30, "break":5, "long_break":15, "loop":4}
            with open('tmsettings.json', "w+") as tm_settings_f:
                json.dump(default_pomo_settings, tm_settings_f)
                tm_settings_f.close()
            self.pomo_settings = default_pomo_settings
        self.pomo_stop = False


    def intro_start_pomo(self):
        threading.Thread(target=lambda : self.start_pomodoro()).start()
    def stop_pomodoro(self):
        self.pomo_stop = True
    def start_pomodoro(self):
        total_seconds = self.pomo_settings['pomo'] * 60

        while total_seconds >= 0:
            if self.pomo_stop:
                break
            countdown = datetime.timedelta(seconds=total_seconds)
            for seconds in range(60):
                window.ui.label.setText(f"{[total_seconds // 3600 if (total_seconds //3600) >= 1 else 0][0]}:{[total_seconds // 60 if (total_seconds // 60) >= 1 else 0][0]}:{["0" if seconds > 50 else ""][0]}{60 - seconds}")
                time.sleep(1)
            total_seconds -= 1
        if self.pomo_stop:
            return  ""





class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = app.Ui_MainWindow()
        self.ui.setupUi(self)
        self.completed_task = None
        self.ui.nw_task.clicked.connect(lambda: self.set_add_task_environment())
        self.ui.addtask.clicked.connect(lambda: self.create_new_task(self.ui.taskname_add.text(), change_widget=True))
        self.ui.tabWidget.currentChanged.connect(lambda :self.verify_pomo_tab())
        self.ui.startpomo.clicked.connect(lambda :[self.start_timer() if self.ui.startpomo.isChecked() == True else self.stop_timer()][0])
        tasks = self.check_tasks_file()
        if tasks != None:
            for task in tasks:
                self.create_new_task(task)
        self.ui.webEngineView.stop()
    #Pomodoro Settings
    def verify_pomo_tab(self):
        if self.ui.tabWidget.currentIndex() == 1:
            POMODORO()
    def start_timer(self):
        self.ui.startpomo.setText("Pause")
        POMODORO().intro_start_pomo()
    def stop_timer(self):
        self.ui.startpomo.setText("Resume")
        POMODORO().stop_pomodoro()
        

    #To-do LSIT FUNCTIONs
    def set_add_task_environment(self):
        self.ui.taskname_add.setFocus()
        self.ui.addtask.setShortcut(QKeySequence(Qt.Key.Key_Return))  # Enter Key
        self.ui.stackedWidget.setCurrentIndex(1)
    def check_tasks_file(self):
        try:
            dt = pando.read_csv("tasks.csv")
        except: return None
        return list(dt["Tasks"])
    @Slot()
    def done_task_function(self, task_obj_name):
        #remove button
        if task_obj_name:
            widget = self.findChildren(QGroupBox, name=task_obj_name)
            widget[0].deleteLater()
        #Play saound
        #Remove task from list
    #Need Edit
    def create_new_task(self, name, change_widget=False, description=None):
        if not name:
            return QMessageBox.information(self, "No task Name", "Please fill required input!", QMessageBox.Ok)
        self.grp_box = QGroupBox(self)
        try:
            self.grp_box.setTitle(name)
        except TypeError:
            self.grp_box.setTitle("#UNSUPPORTED NAME")
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
        #Task File Managment
        try:
            tsk_file_dt = pando.DataFrame(pando.read_csv("Tasks.csv"))
        except FileNotFoundError:
            dt = pando.DataFrame({"Tasks":name}, index=[0])
            dt.to_csv("Tasks.csv")


if __name__ == "__main__":
    core = QApplication(sys.argv)
    window = Window()
    window.show()
    core.exec()