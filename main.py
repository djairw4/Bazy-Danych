import sys

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import db

league_counter = 0
team_counter = 0

class MainScreen(QWidget):
    def __init__(self, parent=None):
        super(MainScreen, self).__init__(parent)
        self.upper_panel()
        self.MainScreenButton = self.button(0, 0, 130, 30, 20, 5, 'Strona główna')
        self.LeagueButton = self.button(0, 0, 100, 30, 155, 5, 'Ligi')
        self.TeamButton = self.button(0, 0, 100, 30, 260, 5, 'Drużyny')
        self.ExitButton = self.button(0, 0, 70, 30, 900, 5, 'Wyjście')
        self.main_view()

    def upper_panel(self):
        up_label = QLabel(self)
        up_label.resize(1000, 40)
        up_label.setStyleSheet("background-color: #7A7A7A;"
                               "color: rgb(255,255,255);"
                               "border-style: solid;"
                               "border-width: 3px;"
                               "border-color: #303030"
                               "border-radius: 10px;"
                               "foreground: #FFFFFF")
        up_label.setFont(QFont('Times', 12, QFont.Bold))

    def button(self, ax, ay, width, height, movex, movey, text=''):
        button = QPushButton(self)
        button.setGeometry(QRect(ax, ay, width, height))
        button.setText(text)
        button.setStyleSheet("color: rgb(255,255,255);"
                             "border-radius: 5px;")
        button.setFont(QFont('Times', 12, QFont.Bold))
        button.move(movex, movey)
        return button

    def main_view(self):
        # Panel z tekstem
        welcome_label = QLabel(self)
        welcome_label.setGeometry(30,50,940,40)
        welcome_label.setStyleSheet("background-color: #7A7A7A;"
                               "color: rgb(255,255,255);"
                               "foreground: #FFFFFF;"
                                 "border-width: 0px")
        welcome_label.setFont(QFont('Times', 20, QFont.Bold))
        welcome_label.setText("Witaj w programie do obsługi turniejów piłki nożnej!")
        welcome_label.setAlignment(Qt.AlignCenter)

        # Panel z obrazem
        img_1 = QPixmap('img1.png')
        resized_img = img_1.scaled(450, 450, Qt.KeepAspectRatio, Qt.FastTransformation)
        image_label = QLabel(self)
        image_label.resize(resized_img.width(), resized_img.height())
        image_label.setGeometry(100, 150, resized_img.width(), resized_img.height())
        image_label.setStyleSheet("border-width: 0px")
        image_label.setPixmap(resized_img)
        image_label.setAlignment(Qt.AlignLeft)

        # Panel tekstowy realizacja kursu
        authors_label = QLabel(self)
        authors_label.setGeometry(700, 400, 200, 100)
        authors_label.setStyleSheet("background-color: #7A7A7A;"
                               "color: rgb(255,255,255);"
                               "foreground: #FFFFFF;"
                                 "border-width: 0px")
        authors_label.setFont(QFont('Times', 14, QFont.Bold))
        authors_label.setText('Autorzy:\nAdam Czarnowski\nDawid Jarząbek\nWersja: 1.0')
        authors_label.setAlignment(Qt.AlignLeft)

class LeagueScreen(QWidget):
    def __init__(self, parent=None):
        super(LeagueScreen, self).__init__(parent)
        self.upper_panel()
        self.MainScreenButton = self.button(0, 0, 130, 30, 20, 5, 'Strona główna')
        self.LeagueButton = self.button(0, 0, 100, 30, 155, 5, 'Ligi')
        self.TeamButton = self.button(0, 0, 100, 30, 260, 5, 'Drużyny')
        self.ExitButton = self.button(0, 0, 70, 30, 900, 5, 'Wyjście')
        self.leagues()

    def upper_panel(self):
        self.up_label = QLabel(self)
        self.up_label.resize(1000, 40)
        self.up_label.setStyleSheet("background-color: #7A7A7A;"
                               "color: rgb(255,255,255);"
                               "border-style: solid;"
                               "border-width: 3px;"
                               "border-color: #303030"
                               "border-radius: 10px;"
                               "foreground: #FFFFFF")
        self.up_label.setFont(QFont('Times', 12, QFont.Bold))

    def button(self, ax, ay, width, height, movex, movey, text=''):
        button = QPushButton(self)
        button.setGeometry(QRect(ax, ay, width, height))
        button.setText(text)
        button.setStyleSheet("color: rgb(255,255,255);"
                             "border-radius: 5px;")
        button.setFont(QFont('Times', 12, QFont.Bold))
        button.move(movex, movey)
        return button

    def leagues(self):
        global league_counter
        self.combo = QComboBox(self)
        self.combo.setGeometry(120, 80, 200,25)
        self.combo.setStyleSheet("color: rgb(255,255,255);")
        self.combo.setFont(QFont('Times', 12, QFont.Bold))
        if league_counter == 0:
            db.leagues()
            db.teams()
            league_counter+=1
        else:
            pass
        self.combo.addItem('-Wybierz ligę-')
        self.combo.addItems(db.league_table)
        self.combo.activated.connect(self.activ)
        self.combo.adjustSize()

        self.label1 = QLabel(self)
        self.label1.setGeometry(80, 120, 380, 25)
        self.label1.setStyleSheet("background-color: #7A7A7A;"
                             "color: rgb(255,255,255);"
                             "foreground: #FFFFFF;"
                             "border-width: 0px")
        self.label1.setFont(QFont('Times', 10, QFont.Bold))
        self.label1.setText("Drużyna Mecze Punkty W R P Strzelone Stracone Bilans")

        self.table = QTableWidget(self)
        self.table.setGeometry(80, 150, 400, 400)
        self.table.setColumnCount(9)
        self.table.horizontalHeader().hide()
        self.table.verticalHeader().hide()
        self.table.setColumnWidth(0, 200)
        self.table.setColumnWidth(1, 40)
        self.table.setColumnWidth(2, 40)
        self.table.setColumnWidth(3, 40)
        self.table.setColumnWidth(4, 40)
        self.table.setColumnWidth(5, 40)
        self.table.setColumnWidth(6, 40)
        self.table.setColumnWidth(7, 40)
        self.table.setColumnWidth(8, 40)

        self.table.setStyleSheet("color: rgb(255,255,255);")
        self.table.setFont(QFont('Times', 10, QFont.Bold))

        self.label2 = QLabel(self)
        self.label2.setGeometry(500, 120, 120, 25)
        self.label2.setStyleSheet("background-color: #7A7A7A;"
                             "color: rgb(255,255,255);"
                             "foreground: #FFFFFF;"
                             "border-width: 0px")
        self.label2.setFont(QFont('Times', 10, QFont.Bold))
        self.label2.setText("Rozgrywki")

        self.matches = QListWidget(self)
        self.matches.setGeometry(500, 150, 400, 400)
        self.matches.setStyleSheet("color: rgb(255,255,255);")
        self.matches.setFont(QFont('Times', 12, QFont.Bold))

        self.addLeague = QPushButton(self)
        self.addLeague.setGeometry(QRect(325, 80, 100, 27))
        self.addLeague.setText('Dodaj ligę')
        self.addLeague.setStyleSheet("color: rgb(255,255,255);"
                             "border-radius: 5px;")
        self.addLeague.setFont(QFont('Times', 12, QFont.Bold))
        self.addLeague.clicked.connect(self.add_league)

        self.removeLeague = QPushButton(self)
        self.removeLeague.setGeometry(QRect(460, 80, 100, 27))
        self.removeLeague.setText('Usuń ligę')
        self.removeLeague.setStyleSheet("color: rgb(255,255,255);"
                                     "border-radius: 5px;")
        self.removeLeague.setFont(QFont('Times', 12, QFont.Bold))
        self.removeLeague.clicked.connect(self.remove_league)


        # Panel z obrazem
        img_3 = QPixmap('img3.png')
        resized_img = img_3.scaled(150, 100, Qt.KeepAspectRatio, Qt.FastTransformation)
        self.image_label = QLabel(self)
        self.image_label.resize(resized_img.width(), resized_img.height())
        self.image_label.setGeometry(900, 50, resized_img.width(), resized_img.height())
        self.image_label.setStyleSheet("border-width: 0px")
        self.image_label.setPixmap(resized_img)
        self.image_label.setAlignment(Qt.AlignRight)

    def activ(self):
        if self.combo.currentText() in db.league_table:
            db.league_index = db.league_table.index(f'{self.combo.currentText()}')
            self.matches.clear()
            self.table.clear()
            db.top_list_proc(db.league_id[db.league_index])
            db.top_list()
            self.table.setRowCount(len(db.table))
            db.league_games(db.league_id[db.league_index])
            for i in db.games_table:
                self.matches.addItems(i)
            for i in range(len(db.table)):
                for j in range(len(db.table[i])):
                    self.table.setItem(i, j, QTableWidgetItem(db.table[i][j]))
            db.hgames_table.clear()
            db.games_table.clear()
            db.table.clear()
        else:
            pass

    def add_league(self):
        global league_counter
        text, ok = QInputDialog.getText(self, "Dodaj ligę", "Podaj nazwę ligi:")
        if ok:
            db.add_league(str(text))
            self.combo.clear()
            db.league_table.clear()
            db.league_id.clear()
            self.combo.addItems(db.league_table)
        league_counter = 0

    def remove_league(self):
        global league_counter
        item, ok = QInputDialog.getItem(self, "Usuń ligę", "Wybierz ligę do usunięcia", db.league_table, 0, False)
        if ok and item:
            db.league_index = db.league_table.index(f'{item}')
            db.remove_league(int(db.league_id[db.league_index]))
            self.combo.clear()
            db.league_table.clear()
            db.league_id.clear()
            self.combo.addItems(db.league_table)
        league_counter = 0

class TeamScreen(QWidget):
    def __init__(self, parent=None):
        super(TeamScreen, self).__init__(parent)
        self.upper_panel()
        self.MainScreenButton = self.button(0, 0, 130, 30, 20, 5, 'Strona główna')
        self.LeagueButton = self.button(0, 0, 100, 30, 155, 5, 'Ligi')
        self.TeamButton = self.button(0, 0, 100, 30, 260, 5, 'Drużyny')
        self.ExitButton = self.button(0, 0, 70, 30, 900, 5, 'Wyjście')
        self.teams()

    def upper_panel(self):
        up_label = QLabel(self)
        up_label.resize(1000, 40)
        up_label.setStyleSheet("background-color: #7A7A7A;"
                               "color: rgb(255,255,255);"
                               "border-style: solid;"
                               "border-width: 3px;"
                               "border-color: #303030"
                               "border-radius: 10px;"
                               "foreground: #FFFFFF")
        up_label.setFont(QFont('Times', 12, QFont.Bold))

    def button(self, ax, ay, width, height, movex, movey, text=''):
        button = QPushButton(self)
        button.setGeometry(QRect(ax, ay, width, height))
        button.setText(text)
        button.setStyleSheet("color: rgb(255,255,255);"
                             "border-radius: 5px;")
        button.setFont(QFont('Times', 12, QFont.Bold))
        button.move(movex, movey)
        return button

    def teams(self):
        global team_counter
        self.label = QLabel(self)
        self.label.setGeometry(670, 200, 140, 25)
        self.label.setStyleSheet("background-color: #7A7A7A;"
                            "color: rgb(255,255,255);"
                            "foreground: #FFFFFF;"
                            "border-width: 0px")
        self.label.setFont(QFont('Times', 12, QFont.Bold))
        self.label.setText("Wybierz drużynę")
        self.combo = QComboBox(self)
        self.combo.setGeometry(570, 230, 200, 25)
        self.combo.setStyleSheet("color: rgb(255,255,255);")
        self.combo.setFont(QFont('Times', 12, QFont.Bold))
        if team_counter == 0:
            db.leagues()
            db.teams()
            team_counter += 1
        else:
            pass
        self.combo.addItems(db.teams_table)
        self.combo.activated.connect(self.activ)
        self.combo.adjustSize()

        self.matches = QListWidget(self)
        self.matches.setGeometry(80, 100, 420, 450)
        self.matches.setStyleSheet("color: rgb(255,255,255);")
        self.matches.setFont(QFont('Times', 12, QFont.Bold))

        # Panel z obrazem
        img_2 = QPixmap('img2.png')
        resized_img = img_2.scaled(450, 350, Qt.KeepAspectRatio, Qt.FastTransformation)
        self.image_label = QLabel(self)
        self.image_label.resize(resized_img.width(), resized_img.height())
        self.image_label.setGeometry(510, 350, resized_img.width(), resized_img.height())
        self.image_label.setStyleSheet("border-width: 0px")
        self.image_label.setPixmap(resized_img)
        self.image_label.setAlignment(Qt.AlignRight)

        self.addTeam = QPushButton(self)
        self.addTeam.setGeometry(QRect(570, 80, 150, 27))
        self.addTeam.setText('Dodaj drużynę')
        self.addTeam.setStyleSheet("color: rgb(255,255,255);"
                                     "border-radius: 5px;")
        self.addTeam.setFont(QFont('Times', 12, QFont.Bold))
        self.addTeam.clicked.connect(self.add_team)

        self.removeTeam = QPushButton(self)
        self.removeTeam.setGeometry(QRect(730, 80, 150, 27))
        self.removeTeam.setText('Usuń drużynę')
        self.removeTeam.setStyleSheet("color: rgb(255,255,255);"
                                   "border-radius: 5px;")
        self.removeTeam.setFont(QFont('Times', 12, QFont.Bold))
        self.removeTeam.clicked.connect(self.remove_team)

        self.addScore = QPushButton(self)
        self.addScore.setGeometry(QRect(650, 117, 150, 27))
        self.addScore.setText('Dodaj wynik')
        self.addScore.setStyleSheet("color: rgb(255,255,255);"
                                      "border-radius: 5px;")
        self.addScore.setFont(QFont('Times', 12, QFont.Bold))
        self.addScore.clicked.connect(self.scores)

    def activ(self):
        db.team_index = db.teams_table.index(f'{self.combo.currentText()}')
        db.team_games(db.teams_id[db.team_index])
        self.matches.clear()
        for i in db.team_game:
            self.matches.addItems(i)
        db.team_game.clear()
        db.hteam_game.clear()

    def add_team(self):
        global team_counter
        item, ok = QInputDialog.getItem(self, "Dodaj drużynę", "Wybierz ligę", db.league_table, 0, False)
        text, ok = QInputDialog.getText(self, "Dodaj drużynę", "Podaj nazwę drużyny:")
        # text2, ok1 = QInputDialog.getText(self, "Dodaj drużynę", "Wybierz ligę, do której dodana zostanie drużyna:")
        db.leagues()
        db.league_index = db.league_table.index(f'{item}')
        db.add_team_proc(str(text), int(db.league_id[db.league_index]))
        db.league_id.clear()
        db.league_table.clear()
        team_counter = 0

    def remove_team(self):
        global team_counter
        item, ok = QInputDialog.getItem(self, "Usuń drużynę", "Wybierz drużynę do usunięcia", db.teams_table, 0, False)
        if ok and item:
            db.team_index = db.teams_table.index(f'{item}')
            db.remove_team_proc(int(db.teams_id[db.team_index]))
            db.teams_table.clear()
            db.teams_id.clear()
        team_counter = 0

    def scores(self):
        team1, ok = QInputDialog.getItem(self, "Dodaj wynik", "Wybierz gospodarza:", db.teams_table, 0, False)
        team2, ok = QInputDialog.getItem(self, "Dodaj wynik", "Wybierz gościa:", db.teams_table, 0, False)
        score1, ok = QInputDialog.getText(self, "Dodaj wynik", "Podaj ilość bramek gospodarza:")
        score2, ok = QInputDialog.getText(self, "Dodaj wynik", "Podaj ilość bramek gościa:")
        league, ok = QInputDialog.getItem(self, "Dodaj wynik", "Wybierz ligę:", db.league_table, 0, False)
        if ok and team1 and team2:
            db.team_index = db.teams_table.index(f'{team1}')
            db.team_index2 = db.teams_table.index(f'{team2}')
            db.league_index = db.league_table.index(f'{league}')
            db.scores_proc(int(db.teams_id[db.team_index]), int(score1), int(score2), int(db.teams_id[db.team_index2]), int(db.league_id[db.league_index]))

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setGeometry(50, 50, 1000, 600)
        self.setFixedSize(1000, 600)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.qr = self.frameGeometry()
        self.cp = QDesktopWidget().availableGeometry().center()
        self.qr.moveCenter(self.cp)
        self.move(self.qr.topLeft())
        self.setStyleSheet("background-color: #7A7A7A;"
                           "border-style: solid;"
                           "border-width: 3px;"
                           "border-color: #303030;"
                           "border-radius: 5px;"
                           "color: rgb(255,255,255);")
        self.setFont(QFont('Times', 12, QFont.Bold))
        self.setWindowTitle("no title")
        self.startMainScreen()

    def startMainScreen(self):
        self.Window = MainScreen(self)
        self.setCentralWidget(self.Window)
        self.Window.LeagueButton.clicked.connect(self.startLeagueScreen)
        self.Window.TeamButton.clicked.connect(self.startTeamScreen)
        self.Window.ExitButton.clicked.connect(self.close_event)
        self.show()

    def startLeagueScreen(self):
        self.LeagueTab = LeagueScreen(self)
        self.setCentralWidget(self.LeagueTab)
        self.LeagueTab.MainScreenButton.clicked.connect(self.startMainScreen)
        self.LeagueTab.TeamButton.clicked.connect(self.startTeamScreen)
        self.LeagueTab.ExitButton.clicked.connect(self.close_event)
        self.show()

    def startTeamScreen(self):
        self.TeamTab = TeamScreen(self)
        self.setCentralWidget(self.TeamTab)
        self.TeamTab.MainScreenButton.clicked.connect(self.startMainScreen)
        self.TeamTab.LeagueButton.clicked.connect(self.startLeagueScreen)
        self.TeamTab.ExitButton.clicked.connect(self.close_event)
        self.show()

    def close_event(self):
        msg = QMessageBox()
        msg.setWindowFlags(Qt.FramelessWindowHint)
        msg.setStyleSheet("background-color: #7A7A7A;"
                          "border-style: solid;"
                          "border-width: 2px;"
                          "border-color: #303030;"
                          "border-radius: 5px;"
                          "color: rgb(255,255,255);"
                          "padding: 5px")
        msg.setWindowTitle('Zamykanie aplikacji')
        msg.setText('Czy na pewno chcesz zamknąć aplikację?')
        msg.setStandardButtons(QMessageBox.Yes|QMessageBox.No)
        yes_button = msg.button(QMessageBox.Yes)
        yes_button.setText('Tak')
        no_button = msg.button(QMessageBox.No)
        no_button.setText('Nie')
        msg.setFont(QFont('Times', 12, QFont.Bold))
        msg.exec_()

        if msg.clickedButton() == yes_button:
            app.quit()
        elif msg.clickedButton() == no_button:
            pass

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MainWindow()
    sys.exit(app.exec_())