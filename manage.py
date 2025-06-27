from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QLayout, QHBoxLayout, QVBoxLayout, QGridLayout, QLineEdit, QTextEdit, QComboBox, QTableWidget, QTableWidgetItem, QHeaderView, QAbstractItemView, QScrollArea, QSpacerItem, QSizePolicy, QFrame, QScrollArea, QDialog, QDateEdit
from PyQt6.QtCore import Qt, QTimer, QDateTime, QSize, QDate
from PyQt6.QtGui import QTextOption, QFont, QIcon
import sys

#----------------------------------------------

class MainWindow(QWidget):
    def __init__(self, add, info, account, helpful):
        super().__init__()
        # main
        self.add = add
        self.info = info
        self.account = account
        self.helpful = helpful
        self.setWindowTitle("ZPAX")
        self.setGeometry(100, 100, 800, 600)
        self.setWindowIcon(QIcon('static/increase_4721635.png'))
        vbox = QVBoxLayout()
        self.setLayout(vbox)

        # header main
        gbox = QGridLayout()
        # application name
        name = QLabel("zpax")
        name.setAlignment(Qt.AlignmentFlag.AlignCenter)
        name.setFixedHeight(30)
        # back button
        back_button = QPushButton("◀")
        back_button.setFixedSize(30, 30)
        # forward button
        forward_button = QPushButton("▶")
        forward_button.setFixedSize(30, 30)
        # exit button
        exit_button = QPushButton("✖")
        exit_button.setFixedSize(30, 30)
        exit_button.setContentsMargins(0, 0, 0, 0)
        exit_button.clicked.connect(self.close)
        # information
        information = QPushButton("❓")
        information.clicked.connect(self.to_info)
        information.setFixedSize(30, 30)
        # add header
        gbox.addWidget(name, 0, 2)
        gbox.addWidget(back_button, 0, 0)
        gbox.addWidget(forward_button, 0, 1)
        gbox.addWidget(information, 0, 3)
        gbox.addWidget(exit_button, 0, 4)

        # menu
        vbox_menu = QVBoxLayout()
        # exit btn
        exit_button = QPushButton("Exit")
        exit_button.clicked.connect(self.close)
        exit_button.setFixedSize(250, 30)
        # add factor
        add_button = QPushButton("Add")
        add_button.clicked.connect(self.to_add)
        add_button.setFixedSize(250, 30)
        # status
        status_button = QPushButton("Status")
        status_button.setFixedSize(250, 30)
        status_button.clicked.connect(self.to_status)
        # hbox for helpful and account
        hbox = QHBoxLayout()
        helpful_button = QPushButton("Helpful")
        helpful_button.clicked.connect(self.to_helpful)
        helpful_button.setFixedSize(120, 30)
        account_button = QPushButton("Account")
        account_button.clicked.connect(self.to_account)
        account_button.setFixedSize(120, 30)
        hbox.addStretch()
        hbox.addWidget(helpful_button)
        hbox.addWidget(account_button)
        hbox.addStretch()
        # add menu
        vbox_menu.addStretch()
        vbox_menu.addWidget(add_button, alignment=Qt.AlignmentFlag.AlignCenter)
        vbox_menu.addLayout(hbox)
        vbox_menu.addWidget(status_button, alignment=Qt.AlignmentFlag.AlignCenter)
        vbox_menu.addWidget(exit_button, alignment=Qt.AlignmentFlag.AlignCenter)
        vbox_menu.addStretch()

        # add to layout
        vbox.addLayout(gbox)
        vbox.addLayout(vbox_menu)

        # creator
        ___ = QLabel("_________________________")
        ___.setStyleSheet("color: #b4b4b450;")
        creator = QLabel("Created by: paxle")
        creator.setStyleSheet("color: #b4b4b450;")
        vbox.addWidget(___, alignment=Qt.AlignmentFlag.AlignCenter)
        vbox.addWidget(creator, alignment=Qt.AlignmentFlag.AlignCenter)

    def to_add(self):
        add.show()
        main.hide()
    
    def to_info(self):
        info.show()
        main.hide()
    
    def to_status(self):
        status.show()
        main.hide()
    
    def to_account(self):
        account.show()
        main.hide()
    
    def to_helpful(self):
        helpful.show()
        main.hide()

#-------------------------------------

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = MainWindow(AddWindow, InfoWindow, AccountsWindow, AddHelpfulWindow)
    add = AddWindow(MainWindow)
    info = InfoWindow(MainWindow)
    status = StatusWindow(MainWindow)
    account = AccountsWindow(MainWindow)
    addaccount = AddAccountWindow(MainWindow, AccountsWindow)
    helpful = HelpfulWindow(MainWindow)
    addhelpful = AddHelpfulWindow(MainWindow)
    edithelpful = EditHelpfulWindow(MainWindow)
    editaccount = EditAccountWindow(MainWindow, AccountsWindow)
    infostatus = InfoStatusWindow()
    alarm = AlarmWindow()
    main.show()
    sys.exit(app.exec())