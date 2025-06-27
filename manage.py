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

#-------------------------------------------

class AddWindow(QWidget):
    def __init__(self, main):
        super().__init__()
        self.main = main
        self.setWindowTitle("ZPAX")
        self.setGeometry(100, 100, 800, 600)
        self.setWindowIcon(QIcon('static/increase_4721635.png'))
        vbox = QVBoxLayout()
        self.setLayout(vbox)

        #header
        gbox = QGridLayout()
        # application name
        name = QLabel("zpax")
        name.setAlignment(Qt.AlignmentFlag.AlignCenter)
        name.setFixedHeight(30)
        # back button
        back_button = QPushButton("◀")
        back_button.clicked.connect(self.to_main)
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

        # widget
        grid = QGridLayout()
        # name
        name_label = QLabel("name:")
        name_label.setAlignment(Qt.AlignmentFlag.AlignLeft)
        name_line = QLineEdit()
        name_line.setAlignment(Qt.AlignmentFlag.AlignLeft)
        # price
        price_label = QLabel("price:")
        price_label.setAlignment(Qt.AlignmentFlag.AlignLeft)
        price_line = QLineEdit()
        price_line.setAlignment(Qt.AlignmentFlag.AlignLeft)
        # hbox for header information
        h_header = QHBoxLayout()
        h_header.addWidget(name_label)
        h_header.addWidget(name_line)
        h_header.addWidget(price_label)
        h_header.addWidget(price_line)
        # description
        description_label = QLabel("description:")
        description_line = QTextEdit()
        description_line.setStyleSheet("border-radius: 6px;")
        # datetime
        self.time = QLabel()
        # timer
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)
        # type
        type_label = QLabel("type:")
        type_label.setAlignment(Qt.AlignmentFlag.AlignLeft)
        type_combo = QComboBox()
        type_combo.addItem("درآمد")
        type_combo.addItem("هزینه")
        type_combo.addItem("خرابکاری")
        type_combo.addItem("بدهکار")
        type_combo.addItem("بستانکار")
        type_combo.addItem("اندوخته")
        type_combo.addItem("قسط")
        type_combo.addItem("تفریحی")
        type_combo.addItem("سایر")
        # hbox for type
        h_type = QHBoxLayout()
        h_type.addWidget(type_label)
        h_type.addWidget(type_combo)
        # invoice
        invoice_label = QLabel("invoice:")
        invoice_label.setAlignment(Qt.AlignmentFlag.AlignLeft)
        invoice_line = QLineEdit()
        invoice_line.setAlignment(Qt.AlignmentFlag.AlignLeft)
        # hbox for invoice
        h_invoice = QHBoxLayout()
        h_invoice.addWidget(invoice_label)
        h_invoice.addWidget(invoice_line)

        # button
        hbox = QHBoxLayout()
        # add button
        add_button = QPushButton("add")
        add_button.setFixedSize(70, 30)
        # cancel button
        cancel_button = QPushButton("cancel")
        cancel_button.clicked.connect(self.to_main)
        cancel_button.setFixedSize(70, 30)
        # add to hbox
        hbox.addStretch()
        hbox.addWidget(add_button)
        hbox.addWidget(cancel_button)

        # add widget
        grid.addLayout(h_header, 0, 0, 1, 4)
        grid.addWidget(description_label, 1, 0)
        grid.addWidget(description_line, 2, 0, 1, 4)
        grid.addLayout(h_type, 3, 0, 1, 4)
        grid.addLayout(h_invoice, 4, 0, 1, 4)
        grid.addWidget(self.time, 5, 0)
        grid.addLayout(hbox, 5, 3)

        # add layout
        vbox.addLayout(gbox)
        vbox.addLayout(grid)

        # creator
        ___ = QLabel("_________________________")
        ___.setStyleSheet("color: #b4b4b450;")
        creator = QLabel("Created by: paxle")
        creator.setStyleSheet("color: #b4b4b450;")
        vbox.addWidget(___, alignment=Qt.AlignmentFlag.AlignCenter)
        vbox.addWidget(creator, alignment=Qt.AlignmentFlag.AlignCenter)

    # def
    def to_main(self):
        main.show()
        add.hide()
    
    def update_time(self):
        current_time = QDateTime.currentDateTime().toString('hh:mm:ss')
        date_time = QDateTime.currentDateTime().toString('yyyy.MM.dd')
        self.time.setText(f"{date_time}  |  {current_time}")
    
    def to_info(self):
        info.show()
        add.hide()

#----------------------------------------------------------------

class InfoWindow(QWidget):
    def __init__(self, main):
        super().__init__()
        self.main = main
        self.setWindowTitle("ZPAX")
        self.setGeometry(100, 100, 800, 600)
        self.setWindowIcon(QIcon('static/increase_4721635.png'))
        vbox = QVBoxLayout()
        self.setLayout(vbox)

        # header
        gbox = QGridLayout()
        # application name
        name = QLabel("zpax")
        name.setAlignment(Qt.AlignmentFlag.AlignCenter)
        name.setFixedHeight(30)
        # back button
        back_button = QPushButton("🏠")
        back_button.clicked.connect(self.to_main)
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
        information.setFixedSize(30, 30)
        # add header
        gbox.addWidget(name, 0, 2)
        gbox.addWidget(back_button, 0, 0)
        gbox.addWidget(forward_button, 0, 1)
        gbox.addWidget(information, 0, 3)
        gbox.addWidget(exit_button, 0, 4)

        # information
        information1 = QLabel("This is an accounting program based on Python algorithms.")
        information1.setWordWrap(True)
        information2 = QLabel("At the age of 19, I decided to create an accounting program with a robust user interface for public consumption for free.")
        information2.setWordWrap(True)
        information3 = QLabel("In this program, by adding invoices, you can perform all your monthly information, including net profit and taxes, and all other accounting equations.")
        information3.setWordWrap(True)

        # add layout
        vbox.addLayout(gbox)
        vbox.addWidget(information1)
        vbox.addWidget(information2)
        vbox.addWidget(information3)
        vbox.addStretch()
        

        # creator
        ___ = QLabel("_________________________")
        ___.setStyleSheet("color: #b4b4b450;")
        creator = QLabel("Created by: paxle")
        creator.setStyleSheet("color: #b4b4b450;")
        vbox.addWidget(___, alignment=Qt.AlignmentFlag.AlignCenter)
        vbox.addWidget(creator, alignment=Qt.AlignmentFlag.AlignCenter)
    
    # def
    def to_main(self):
        main.show()
        info.hide()

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