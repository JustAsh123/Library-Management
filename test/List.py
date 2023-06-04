from PyQt5 import QtCore, QtGui, QtWidgets

data = [
    (1, 'Maths', 'RS Agrawal', 'NCERT', 13),
    (2, 'Computer', 'Sumitra Arora', 'Tata Ltd', 26),
    (3, '', '', '', 0),
    (4, 'Physics', 'HC Verma', 'BPB', 14),
    (5, 'Harry Potter', 'JK Rowling', '', 14),
    (6, 'Merchant of Venice', 'William Shakespeare', 'XYZ', 32)
]

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.table_widget = QtWidgets.QTableWidget(self.centralwidget)
        self.table_widget.setObjectName("table_widget")
        self.verticalLayout.addWidget(self.table_widget)
        self.button_delete = QtWidgets.QPushButton(self.centralwidget)
        self.button_delete.setObjectName("button_delete")
        self.verticalLayout.addWidget(self.button_delete)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.load_data()
        self.table_widget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.table_widget.itemSelectionChanged.connect(self.update_delete_button)

        self.button_delete.setEnabled(False)
        self.button_delete.clicked.connect(self.delete_selected_rows)

    def load_data(self):
        self.table_widget.setColumnCount(5)
        self.table_widget.setHorizontalHeaderLabels(['ID', 'Title', 'Author', 'Publisher', 'Quantity'])
        self.table_widget.setRowCount(len(data))
        for row, item in enumerate(data):
            for col, value in enumerate(item):
                table_item = QtWidgets.QTableWidgetItem(str(value))
                self.table_widget.setItem(row, col, table_item)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.button_delete.setText(_translate("MainWindow", "Delete"))

    def update_delete_button(self):
        selected_rows = self.table_widget.selectionModel().selectedRows()
        self.button_delete.setEnabled(len(selected_rows) > 0)

    def delete_selected_rows(self):
        selected_rows = self.table_widget.selectionModel().selectedRows()
        rows_to_delete = sorted(row.row() for row in selected_rows)[::-1]
        for row in rows_to_delete:
            self.table_widget.removeRow(row)

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Delete:
            self.delete_selected_rows()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
