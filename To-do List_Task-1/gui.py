import sys

from PyQt5 import QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

# -------------------------Dark Theme--------------------------------------------------
palette = QPalette()
palette.setColor(QPalette.Window, QColor(53, 53, 53))
palette.setColor(QPalette.WindowText, Qt.white)
palette.setColor(QPalette.Base, QColor(25, 25, 25))
palette.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
palette.setColor(QPalette.ToolTipBase, Qt.black)
palette.setColor(QPalette.ToolTipText, Qt.white)
palette.setColor(QPalette.Text, Qt.white)
palette.setColor(QPalette.Button, QColor(53, 53, 53))
palette.setColor(QPalette.ButtonText, Qt.white)
palette.setColor(QPalette.BrightText, Qt.red)
palette.setColor(QPalette.Link, QColor(42, 130, 218))
palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
palette.setColor(QPalette.HighlightedText, Qt.black)
# -------------------------Dark Theme--------------------------------------------------

# -------------------------Class addingWindow--------------------------------------START
class addingWindow(QWidget):
    def __init__(self, mainWindow):
        super().__init__()
        self.WindowIcon = QIcon('images/icon.png')
        self.setWindowTitle("Add a New Task")
        self.setWindowIcon(self.WindowIcon)


        self.mainWindow = mainWindow
        mainLayout = QHBoxLayout()

        self.Formlayout = QFormLayout()

        self.label_task = QLabel()
        self.label_task.setText("Enter Your New Task: ")

        self.task_inputbox = QLineEdit()

        self.Formlayout.addRow(self.label_task, self.task_inputbox)

        self.button_add = QPushButton('Add', self)
        self.button_add.clicked.connect(self.addTask)
        self.button_add.adjustSize()

        mainLayout.addLayout(self.Formlayout)
        mainLayout.addWidget(self.button_add)

        self.setLayout(mainLayout)

    def addTask(self):
        if str(self.task_inputbox.text()) == '':
            error = QMessageBox()
            error.setWindowTitle("Error!!")
            error.setIcon(QMessageBox.Critical)
            error.setWindowIcon(QIcon('images/icon.png'))
            error.setText("Enter Task Please!!                                ")
            error.exec()
        else:
            self.mainWindow.MyList.append(str(self.task_inputbox.text()))
            self.mainWindow.update_window()
            self.close()

# -------------------------Class addingWindow--------------------------------------END


# -------------------------Class editingWindow-------------------------------------START
class editingWindow(QWidget):
    def __init__(self, mainWindow):
        super().__init__()
        self.WindowIcon = QIcon('images/icon.png')
        self.setWindowTitle("Editing a Task")
        self.setWindowIcon(self.WindowIcon)

        self.mainWindow = mainWindow
        mainLayout = QHBoxLayout()

        self.Formlayout = QFormLayout()

        self.num_of_task = QLabel()
        self.num_of_task.setText("Task Number: ")

        self.num_of_task_inputbox = QLineEdit()

        self.label_task = QLabel()
        self.label_task.setText("Edited Task: ")

        self.task_inputbox = QLineEdit()

        self.Formlayout.addRow(self.num_of_task, self.num_of_task_inputbox)
        self.Formlayout.addRow(self.label_task, self.task_inputbox)

        self.button_edit = QPushButton('Edit', self)
        self.button_edit.clicked.connect(self.editTask)
        self.button_edit.adjustSize()

        mainLayout.addLayout(self.Formlayout)
        mainLayout.addWidget(self.button_edit)

        self.setLayout(mainLayout)

    def editTask(self):
        error = QMessageBox()
        error.setWindowTitle("Error!!")
        error.setIcon(QMessageBox.Critical)
        error.setWindowIcon(QIcon('images/icon.png'))
        if str(self.task_inputbox.text()) == '':
            error.setText("Enter Task Please!!                                ")
            error.exec()
        elif int(self.num_of_task_inputbox.text()) - 1 >= len(self.mainWindow.MyList):
            error.setText("Enter Correct Task Number Please!!                 ")
            error.exec()
        else:
            self.mainWindow.MyList[int(self.num_of_task_inputbox.text()) - 1] = str(self.task_inputbox.text())
            self.mainWindow.update_window()
            self.close()

# -------------------------Class editingWindow-----------------------------------------END

# -------------------------Class deletingWindow----------------------------------------START
class deletingWindow(QWidget):
    def __init__(self, mainWindow):
        super().__init__()
        self.WindowIcon = QIcon('images/icon.png')
        self.setWindowTitle("Deleting a Task")
        self.setWindowIcon(self.WindowIcon)

        self.mainWindow = mainWindow
        mainLayout = QHBoxLayout()

        self.Formlayout = QFormLayout()

        self.num_of_task = QLabel()
        self.num_of_task.setText("Task Number: ")

        self.num_of_task_inputbox = QLineEdit()

        self.Formlayout.addRow(self.num_of_task, self.num_of_task_inputbox)

        self.button_delete = QPushButton('Delete', self)
        self.button_delete.clicked.connect(self.deleteTask)
        self.button_delete.adjustSize()

        mainLayout.addLayout(self.Formlayout)
        mainLayout.addWidget(self.button_delete)

        self.setLayout(mainLayout)

    def deleteTask(self):
        if int(self.num_of_task_inputbox.text()) - 1 >= len(self.mainWindow.MyList):
            error = QMessageBox()
            error.setWindowTitle("Error!!")
            error.setIcon(QMessageBox.Critical)
            error.setWindowIcon(QIcon('images/icon.png'))
            error.setText("Enter Correct Task Number Please!!                 ")
            error.exec()
        else:
            NewList = []
            Num_of_Tasks = int(len(self.mainWindow.MyList))
            for i in range(Num_of_Tasks):
                if i + 1 == int(self.num_of_task_inputbox.text()):
                    continue
                else:
                    NewList.append(self.mainWindow.MyList[i])
            self.mainWindow.MyList = []
            self.mainWindow.MyList = NewList

            self.mainWindow.update_window()
            self.close()
# -------------------------Class deletingWindow------------------------------------END

# -------------------------Class MainWindow----------------------------------------START
class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.WindowIcon = QIcon('images/icon.png')
        self.setWindowTitle("To-Do List")
        self.setWindowIcon(self.WindowIcon)
        self.setMinimumWidth(650)

        self.MyList = []
        self.mainLayout = QVBoxLayout()

        self.label_logo = QLabel()
        self.label_logo.adjustSize()
        self.label_logo.setAlignment(QtCore.Qt.AlignCenter)
        self.label_logo.setVisible(True)
        self.label_logo.setPixmap(QPixmap('images/icon.png').scaled(200, 200))

        self.TitleLabel = QLabel("To-Do List")
        self.TitleLabel.adjustSize()
        self.TitleLabel.setAlignment(QtCore.Qt.AlignCenter)

        label_title_font = self.TitleLabel.font()
        label_title_font.setPointSize(18)
        label_title_font.bold()

        self.TitleLabel.setFont(label_title_font)
        self.TitleLabel.adjustSize()

        self.button_add = QPushButton('Add', self)
        self.button_add.adjustSize()
        self.button_add.clicked.connect(self.addTask)

        self.button_edit = QPushButton('Edit', self)
        self.button_edit.adjustSize()
        self.button_edit.clicked.connect(self.editTask)

        self.button_delete = QPushButton('Delete', self)
        self.button_delete.adjustSize()
        self.button_delete.clicked.connect(self.deleteTask)

        self.listLayout = QVBoxLayout()

        button_Hlayout = QHBoxLayout()
        button_Hlayout.addWidget(self.button_add)
        button_Hlayout.addWidget(self.button_edit)
        button_Hlayout.addWidget(self.button_delete)

        self.Tasks_Label = QLabel()

        self.mainLayout.addWidget(self.label_logo)
        self.mainLayout.addWidget(self.TitleLabel)
        self.mainLayout.addLayout(button_Hlayout)
        self.mainLayout.addWidget(self.Tasks_Label)
        self.mainLayout.addStretch(1)
        self.setLayout(self.mainLayout)
        self.adjustSize()

    # -------------------------Functions-----------------------------------------------START
    def addTask(self):
        self.addTaskWindow = addingWindow(self)
        self.addTaskWindow.show()

    def editTask(self):
        self.editTaskWindow = editingWindow(self)
        self.editTaskWindow.show()

    def deleteTask(self):
        self.delteTaskWindow = deletingWindow(self)
        self.delteTaskWindow.show()

    def update_window(self):
        Num_of_Tasks = int(len(self.MyList))
        Tasks = ''
        for i in range(Num_of_Tasks):
            Tasks = Tasks + str(i+1)+') ' + str(self.MyList[i]) + '\n'
        self.Tasks_Label.setText(Tasks)
        self.Tasks_Label.setVisible(True)

        label_tasks_font = self.Tasks_Label.font()
        label_tasks_font.setPointSize(11)
        # label_tasks_font.bold()

        self.Tasks_Label.setFont(label_tasks_font)
        self.Tasks_Label.adjustSize()
        self.adjustSize()
    # -------------------------Functions-------------------------------------------END

# -------------------------Class MainWindow----------------------------------------END

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setPalette(palette)
    app.setStyle("Fusion")

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())
