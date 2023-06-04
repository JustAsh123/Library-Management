from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication, QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton


class MainMenu(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("MainMenu.ui", self)

        self.list.clicked.connect(self.open_list_books)
        self.issue.clicked.connect(self.open_issue)

    def open_issue(self):
        self.issue = IssueBook()
        self.issue.show()
        self.close()

    def open_list_books(self):
        self.list = ListBooks()
        self.list.show()
        self.close()

from bookList import give_data

data = give_data()
print(data)
class ListBooks(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("ListBooks.ui", self)

        self.load_data()
        self.table_widget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.adjust_column_widths()

        self.add_book.clicked.connect(self.open_add_book)
        self.go_back.clicked.connect(self.back)
        self.delete_but.clicked.connect(self.delete_clicked)

    def delete_clicked(self):
        popup = DeletePopup(self)
        popup.refresh_signal.connect(self.load_data)
        popup.exec_()


    def load_data(self):
        self.table_widget.setColumnCount(5)
        self.table_widget.setHorizontalHeaderLabels(['ID', 'Title', 'Author', 'Publisher', 'Quantity'])
        self.table_widget.setRowCount(len(give_data()))
        for row, item in enumerate(give_data()):
            for col, value in enumerate(item):
                table_item = QtWidgets.QTableWidgetItem(str(value))
                self.table_widget.setItem(row, col, table_item)

    def adjust_column_widths(self):
        self.table_widget.resizeColumnsToContents()
        self.table_widget.horizontalHeader().setStretchLastSection(True)

    def back(self):
        self.new = MainMenu()
        self.new.show()
        self.close()

    def open_add_book(self):
        self.add = AddBook()
        self.add.show()
        self.close()


from bookList import add_data

class AddBook(QtWidgets.QMainWindow):
    def __init__(self):
        super(AddBook, self).__init__()
        loadUi('AddBook.ui', self)
        self.add.clicked.connect(self.add_book)
        self.cancel.clicked.connect(self.cancel_but)

    def add_book(self):
        title = self.title.text()
        author = self.author.text()
        publication = self.publication.text()
        quantity = self.quantity.value()
        if title !="" and author !="" and publication!="" and quantity !=0:
            add_data(title,author,publication,quantity)
            self.list = ListBooks()
            self.list.show()
            self.close()
        else:
            self.error_message.setText("Please dont enter empty values!")
        
    
    def cancel_but(self):
        self.list = ListBooks()
        self.list.show()
        self.close()

from PyQt5.QtCore import pyqtSignal

from bookList import delete   
class DeletePopup(QDialog):
    refresh_signal = pyqtSignal()
    def __init__(self, parent=None):
        super().__init__(parent)
        loadUi('delete_popup.ui',self)
        self.delete_pop.clicked.connect(self.delete_clicked)
        self.cancel.clicked.connect(self.close_pop)
    
    def close_pop(self):
        self.close()

    def delete_clicked(self):
        number = self.ac.value()
        delete(number)
        self.refresh_signal.emit()
        self.close()


class IssueBook(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("IssueBook.ui", self)
        self.load_data()

        self.issue.clicked.connect(self.issue_clicked)
        self.back.clicked.connect(self.go_back)

    def go_back(self):
        self.main = MainMenu()
        self.main.show()
        self.close()

    def load_data(self):
        self.table_widget.setColumnCount(5)
        self.table_widget.setHorizontalHeaderLabels(['ID', 'Title', 'Author', 'Publisher', 'Quantity'])
        self.table_widget.setRowCount(len(give_data()))
        for row, item in enumerate(give_data()):
            for col, value in enumerate(item):
                table_item = QtWidgets.QTableWidgetItem(str(value))
                self.table_widget.setItem(row, col, table_item)

    def issue_clicked(self):
        popup = IssuePopup(self)
        popup.refresh_signal.connect(self.load_data)
        popup.exec_()

from register import register_issue

class IssuePopup(QDialog):
    refresh_signal = pyqtSignal()
    def __init__(self, parent=None):
        super().__init__(parent)
        loadUi('Issue Book.ui',self)
        self.issue.clicked.connect(self.issued)

    def issued(self):
        self.dateI = str(self.date.date())
        self.acI = self.ac.value()
        self.sidI = self.s_id.value()
        self.snameI = self.s_name.text()
        if self.acI !=0 and self.snameI !="":
            try:
                register_issue(self.dateI,self.acI,self.sidI,self.snameI)
                self.refresh_signal.emit()
                self.close()
            except:
                self.error_message.setText("Please enter valid Access Code")
        else:
            self.error_message.setText("Please Fill all the Fields")
    

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = MainMenu()
    ui.show()
    sys.exit(app.exec_())
