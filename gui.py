from PyQt5.QtWidgets import (
    QDialog,
    QApplication,
    QPlainTextEdit,
    QSizePolicy,
)
import interface
import sys, os
import main
import datetime


class GUI(QDialog):
    def __init__(self) -> None:
        super().__init__()
        self.Combiner = main.Combine_Arcticle
        self.Article = main.Article
        self.ui = interface.Ui_Dialog()
        self.ui.setupUi(self)
        self.list_plaintexts = [self.ui.plainTextEdit_1]

        self.ui.pushButton_Add.clicked.connect(self.New_Page)
        self.ui.pushButton_Past.clicked.connect(self.PastToCurrentTab)
        self.ui.pushButton_Remove.clicked.connect(self.Remove_Page)
        self.ui.pushButton_Output.clicked.connect(self.Output_Article)

    def New_Page(self):

        number_page = self.ui.tabWidget.count() + 1
        plaintext = QPlainTextEdit()
        plaintext.setObjectName(f"plainTextEdit_{number_page}")
        policy = plaintext.sizePolicy()
        policy.setVerticalPolicy(QSizePolicy.Minimum)
        policy.setHorizontalPolicy(QSizePolicy.Minimum)
        plaintext.setSizePolicy(policy)
        self.list_plaintexts.append(plaintext)

        self.ui.tabWidget.addTab(plaintext, f"Articel {number_page}")
        self.ui.tabWidget.setCurrentIndex(number_page - 1)

    def Remove_Page(self):
        index = self.ui.tabWidget.currentIndex()
        self.ui.tabWidget.removeTab(index)
        self.list_plaintexts.pop(index)

    def PastToCurrentTab(self):
        index = self.ui.tabWidget.currentIndex()
        self.list_plaintexts[index].paste()

    def Output_Article(self):
        step = self.ui.spinBox.value()
        self.articles = []
        for plaintext in self.list_plaintexts:
            text = plaintext.toPlainText()
            article = self.Article(text, step)
            self.articles.append(article)
        combiner = self.Combiner(self.articles)
        combiner.match_articels()
        result = combiner.combine()
        result = result.replace("\n\n", "\n")
        self.Save_TO_File(result)

    def Save_TO_File(self, text: str):
        time = datetime.datetime.now().strftime("%m-%d-%Y %H;%M;%S")
        path = os.path.join(os.getcwd(), f"result-{time}.txt")
        with open(f"{path}", "w", encoding="utf-8") as file:
            file.writelines(text)


if __name__ == "__main__":
    app = QApplication([])
    gui = GUI()
    gui.show()
    sys.exit(app.exec_())
