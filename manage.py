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

#-----------------------------------------------------------

class AccountsWindow(QWidget):
    def __init__(self, main):
        super().__init__()
        self.main = main
        self.setWindowTitle("Accounts")
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

        # layout
        v_account = QVBoxLayout()
        h_account = QHBoxLayout()
        h_account_header = QHBoxLayout()
        # widgets
        name_label = QLabel("abbass")
        name_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        cart_label = QLabel("6277-6831-5743-4432")
        cart_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        information_button = QPushButton("✎")
        information_button.clicked.connect(self.to_editaccount)
        information_button.setFixedSize(30, 30)
        # add to h_account
        h_account.addWidget(name_label)
        h_account.addWidget(cart_label)
        h_account.addWidget(information_button)

        table_name = QLabel("name")
        table_name.setAlignment(Qt.AlignmentFlag.AlignCenter)
        table_name.setStyleSheet("border: 1px solid #161616;border-radius: 2px;")
        table_cart = QLabel("cart")
        table_cart.setAlignment(Qt.AlignmentFlag.AlignCenter)
        table_cart.setStyleSheet("border: 1px solid #161616;border-radius: 2px;")
        information_label = QLabel("")
        information_label.setFixedSize(30, 30)
        information_label.setStyleSheet("border: 1px solid #161616;border-radius: 2px;")
        # add to h_account_header
        h_account_header.addWidget(table_name)
        h_account_header.addWidget(table_cart)
        h_account_header.addWidget(information_label)

        # add h to v
        v_account.addLayout(h_account_header)
        v_account.addLayout(h_account)

        # footer button
        h_footer = QHBoxLayout()
        add_button = QPushButton("add")
        add_button.clicked.connect(self.to_addaccount)
        add_button.setFixedSize(120, 30)
        back_button = QPushButton("back")
        back_button.clicked.connect(self.to_main)
        back_button.setFixedSize(120, 30)
        # add to h_footer
        h_footer.addStretch()
        h_footer.addWidget(add_button)
        h_footer.addWidget(back_button)

        # add layout
        vbox.addLayout(gbox)
        vbox.addLayout(v_account)
        vbox.addStretch()
        vbox.addLayout(h_footer)

    # def
    def to_main(self):
        main.show()
        account.hide()
    
    def to_addaccount(self):
        addaccount.show()
        account.hide()
    
    def to_editaccount(self):
        editaccount.show()
        account.hide()
    
    def to_info(self):
        info.show()
        account.hide()

#----------------------------------------------------------

class AddAccountWindow(QWidget):
    def __init__(self, main, account):
        super().__init__()
        self.main = main
        self.account = account
        self.setWindowTitle("Add Account")
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
        back_button.clicked.connect(self.to_account)
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
        name_label = QLabel("Name:")
        name_line = QLineEdit()
        name_line.setAlignment(Qt.AlignmentFlag.AlignCenter)
        cart_label = QLabel("Cart:")
        cart_line = QLineEdit()
        cart_line.setAlignment(Qt.AlignmentFlag.AlignCenter)
        description_label = QLabel("Description:")
        description_line = QTextEdit()
        # layout
        g_info_account = QGridLayout()
        g_info_account.addWidget(name_label, 0, 0)
        g_info_account.addWidget(name_line, 0, 1)
        g_info_account.addWidget(cart_label, 1, 0)
        g_info_account.addWidget(cart_line, 1, 1)
        g_info_account.addWidget(description_label, 2, 0)
        g_info_account.addWidget(description_line, 2, 1)

        # add layout
        vbox.addLayout(gbox)
        vbox.addLayout(g_info_account)

        # footer button
        h_footer = QHBoxLayout()
        add_button = QPushButton("save")
        add_button.setFixedSize(200, 30)
        back_button = QPushButton("cancel")
        back_button.clicked.connect(self.to_account)
        back_button.setFixedSize(200, 30)
        # add to h_footer
        h_footer.addWidget(add_button)
        h_footer.addWidget(back_button)

        # add layout
        vbox.addLayout(gbox)
        vbox.addStretch()
        vbox.addLayout(h_footer)

    # def
    def to_account(self):
        account.show()
        addaccount.hide()
    
    def to_info(self):
        info.show()
        addaccount.hide()

#----------------------------------------------------------

class EditAccountWindow(QWidget):
    def __init__(self, main, account):
        super().__init__()
        self.main = main
        self.account = account
        self.setWindowTitle("Edit Account")
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
        back_button.clicked.connect(self.to_account)
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
        name_label = QLabel("Name:")
        name_line = QLineEdit()
        name_line.setAlignment(Qt.AlignmentFlag.AlignCenter)
        cart_label = QLabel("Cart:")
        cart_line = QLineEdit()
        cart_line.setAlignment(Qt.AlignmentFlag.AlignCenter)
        description_label = QLabel("Description:")
        description_line = QTextEdit()
        # layout
        g_info_account = QGridLayout()
        g_info_account.addWidget(name_label, 0, 0)
        g_info_account.addWidget(name_line, 0, 1)
        g_info_account.addWidget(cart_label, 1, 0)
        g_info_account.addWidget(cart_line, 1, 1)
        g_info_account.addWidget(description_label, 2, 0)
        g_info_account.addWidget(description_line, 2, 1)

        # add layout
        vbox.addLayout(gbox)
        vbox.addLayout(g_info_account)

        # footer button
        h_footer = QHBoxLayout()
        add_button = QPushButton("save")
        add_button.setFixedSize(200, 30)
        back_button = QPushButton("cancel")
        back_button.clicked.connect(self.to_account)
        back_button.setFixedSize(200, 30)
        delete_button = QPushButton("delete")
        delete_button.clicked.connect(self.alarm)
        delete_button.setFixedSize(200, 30)
        # add to h_footer
        h_footer.addWidget(add_button)
        h_footer.addWidget(back_button)
        h_footer.addWidget(delete_button)

        # add layout
        vbox.addLayout(gbox)
        vbox.addStretch()
        vbox.addLayout(h_footer)

    # def
    def to_account(self):
        account.show()
        editaccount.hide()
    
    def alarm(self):
        alarm.show()
    
    def to_info(self):
        info.show()
        editaccount.hide()

#----------------------------------------------------------

class HelpfulWindow(QWidget):
    def __init__(self, main):
        super().__init__()
        self.main = main
        self.setWindowTitle("Helpful")
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
        information.clicked.connect(self.to_information)
        information.setFixedSize(30, 30)
        # add header
        gbox.addWidget(name, 0, 2)
        gbox.addWidget(back_button, 0, 0)
        gbox.addWidget(forward_button, 0, 1)
        gbox.addWidget(information, 0, 3)
        gbox.addWidget(exit_button, 0, 4)

        # widget
        title_label = QLabel("title")
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        date_label = QLabel("date")
        date_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        price_label = QLabel("price")
        price_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        description_label = QLabel("description")
        description_label.setWordWrap(True)
        description_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        edit_button = QPushButton("edit")
        edit_button.clicked.connect(self.to_edithelpful)
        delete_button = QPushButton("delete")
        delete_button.clicked.connect(self.to_alarm)
        add_button = QPushButton("add")
        add_button.clicked.connect(self.to_addhelpful)
        # layout
        v_helpful = QVBoxLayout()
        v_helpful_info = QVBoxLayout()
        v_helpful_description = QVBoxLayout()
        v_helpful_button = QVBoxLayout()
        h_helpful_all = QHBoxLayout()
        # add to layout
        v_helpful_info.addWidget(title_label)
        v_helpful_info.addWidget(date_label)
        v_helpful_info.addWidget(price_label)
        v_helpful_description.addWidget(description_label)
        v_helpful_button.addWidget(edit_button)
        v_helpful_button.addWidget(delete_button)
        h_helpful_all.addLayout(v_helpful_info)
        h_helpful_all.addLayout(v_helpful_description)
        h_helpful_all.addLayout(v_helpful_button)
        v_helpful.addLayout(h_helpful_all)
        # scroll
        scroll_v_helpful_widget = QWidget()
        scroll_v_helpful_widget.setLayout(v_helpful)
        scroll_v_helpful = QScrollArea()
        scroll_v_helpful.setWidget(scroll_v_helpful_widget)
        scroll_v_helpful.setWidgetResizable(True)

        # add layout
        vbox.addLayout(gbox)
        vbox.addWidget(scroll_v_helpful)
        vbox.addStretch()
        vbox.addWidget(add_button)

    # def
    def to_main(self):
        main.show()
        helpful.hide()

    def to_addhelpful(self):
        addhelpful.show()
        helpful.hide()
    
    def to_edithelpful(self):
        edithelpful.show()
        helpful.hide()
    
    def to_alarm(self):
        alarm.show()
    
    def to_information(self):
        info.show()
        helpful.hide()

#----------------------------------------------------------

class AddHelpfulWindow(QWidget):
    def __init__(self, main):
        super().__init__()
        self.main = main
        self.setWindowTitle("Add Helpful")
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
        back_button.clicked.connect(self.to_helpful)
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
        title_label = QLabel("title:")
        title_line = QLineEdit()
        date_label = QLabel("date:")
        date_line = QComboBox()
        date_line.addItems(["هر ماه", "هر هفته", "هر روز", "هر 2 ماه", "هر 3 ماه", "هر سال"])
        price_label = QLabel("price:")
        price_line = QLineEdit()
        description_label = QLabel("description:")
        description_line = QTextEdit()
        # layout
        v_widget = QVBoxLayout()
        # add widget
        v_widget.addWidget(title_label)
        v_widget.addWidget(title_line)
        v_widget.addWidget(date_label)
        v_widget.addWidget(date_line)
        v_widget.addWidget(price_label)
        v_widget.addWidget(price_line)
        v_widget.addWidget(description_label)
        v_widget.addWidget(description_line)

        # add layout
        vbox.addLayout(gbox)
        vbox.addLayout(v_widget)

        # footer button
        h_footer = QHBoxLayout()
        add_button = QPushButton("add")
        cancel_button = QPushButton("cancel")
        cancel_button.clicked.connect(self.to_helpful)
        h_footer.addStretch()
        h_footer.addWidget(add_button)
        h_footer.addWidget(cancel_button)
        vbox.addLayout(h_footer)
    
    # def
    def to_main(self):
        main.show()
        helpful.hide()
    
    def to_helpful(self):
        helpful.show()
        addhelpful.hide()
    
    def to_info(self):
        info.show()
        addhelpful.hide()

#-----------------------------------------------------------

class EditHelpfulWindow(QWidget):
    def __init__(self, main):
        super().__init__()
        self.main = main
        self.setWindowTitle("Edit Helpful")
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
        back_button.clicked.connect(self.to_helpful)
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
        title_label = QLabel("title:")
        title_line = QLineEdit()
        date_label = QLabel("date:")
        date_line = QComboBox()
        date_line.addItems(["هر ماه", "هر هفته", "هر روز", "هر 2 ماه", "هر 3 ماه", "هر سال"])
        price_label = QLabel("price:")
        price_line = QLineEdit()
        description_label = QLabel("description:")
        description_line = QTextEdit()
        # layout
        v_widget = QVBoxLayout()
        # add widget
        v_widget.addWidget(title_label)
        v_widget.addWidget(title_line)
        v_widget.addWidget(date_label)
        v_widget.addWidget(date_line)
        v_widget.addWidget(price_label)
        v_widget.addWidget(price_line)
        v_widget.addWidget(description_label)
        v_widget.addWidget(description_line)

        # add layout
        vbox.addLayout(gbox)
        vbox.addLayout(v_widget)

        # footer button
        h_footer = QHBoxLayout()
        add_button = QPushButton("add")
        cancel_button = QPushButton("cancel")
        cancel_button.clicked.connect(self.to_helpful)
        h_footer.addStretch()
        h_footer.addWidget(add_button)
        h_footer.addWidget(cancel_button)
        vbox.addLayout(h_footer)
    
    # def
    def to_main(self):
        main.show()
        helpful.hide()
    
    def to_helpful(self):
        helpful.show()
        edithelpful.hide()
    
    def to_info(self):
        info.show()
        edithelpful.hide()

#-----------------------------------------------------------

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