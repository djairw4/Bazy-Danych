import cx_Oracle

league_table = []
league_id = []
teams_table = []
teams_id = []
table = []
hgames_table = []
games_table = []
hteam_game = []
team_game = []

league_index = int()
team_index = int()
team_index2 = int()

def leagues():
    sql = ''' SELECT * FROM LIGI'''
    try:
        with cx_Oracle.connect('admin/admin@localhost:1521') as connection:
            with connection.cursor() as cursor:
                cursor.execute(sql)
                row = cursor.fetchall()
                for i in row:
                    league_id.append(i[0])
                    league_table.append(i[1])
    except cx_Oracle.Error as error:
        print(f'Błąd: {error}')

def teams():
    sql = ''' SELECT * FROM DRUŻYNY'''
    try:
        with cx_Oracle.connect('admin/admin@localhost:1521') as connection:
            with connection.cursor() as cursor:
                cursor.execute(sql)
                row = cursor.fetchall()
                for i in row:
                    teams_id.append(i[0])
                    teams_table.append(i[1])
    except cx_Oracle.Error as error:
        print(f'Błąd: {error}')

def top_list():
    sql = ''' SELECT * FROM TABELA'''
    try:
        with cx_Oracle.connect('admin/admin@localhost:1521') as connection:
            with connection.cursor() as cursor:
                cursor.execute(sql)
                row = cursor.fetchall()
                for i in row:
                    x = [i[1], str(i[2]), str(i[3]), str(i[4]), str(i[5]), str(i[6]), str(i[7]), str(i[8]), str(i[9])]
                    table.append(x)
    except cx_Oracle.Error as error:
        print(f'Błąd: {error}')

def top_list_proc(id):
    try:
        with cx_Oracle.connect('admin/admin@localhost:1521') as connection:
            with connection.cursor() as cursor:
                cursor.callproc('STWORZTABELE', [id, 2021])
    except cx_Oracle.Error as error:
        print(f'Błąd: {error}')

def league_games(id):
    sql = f"""SELECT * FROM MECZE WHERE ID_LIGI='{id}' AND NR_SEZONU=2021"""
    try:
        with cx_Oracle.connect('admin/admin@localhost:1521') as connection:
            with connection.cursor() as cursor:
                cursor.execute(sql)
                row = cursor.fetchall()
                for i in row:
                    t_index = teams_id.index(int(i[1]))
                    t_index2 = teams_id.index(int(i[2]))
                    team1 = teams_table[t_index]
                    team2 = teams_table[t_index2]
                    x = [str(team1), str(team2), str(i[3]), str(i[4])]
                    hgames_table.append(x)
                for i in hgames_table:
                    x = [f'{i[0]}  {i[2]}:{i[3]}  {i[1]}']
                    games_table.append(x)
    except cx_Oracle.Error as error:
        print(f'Błąd: {error}')

def team_games(team):
    sql = f"""SELECT * FROM MECZE WHERE GOSPODARZ='{team}' OR GOSC='{team}'"""
    try:
        with cx_Oracle.connect('admin/admin@localhost:1521') as connection:
            with connection.cursor() as cursor:
                cursor.execute(sql)
                row = cursor.fetchall()
                for i in row:
                    t_index = teams_id.index(int(i[1]))
                    t_index2 = teams_id.index(int(i[2]))
                    team1 = teams_table[t_index]
                    team2 = teams_table[t_index2]
                    x = [str(team1), str(team2), str(i[3]), str(i[4])]
                    hteam_game.append(x)
                for i in hteam_game:
                    x = [f'{i[0]}  {i[2]}:{i[3]}  {i[1]}']
                    team_game.append(x)
    except cx_Oracle.Error as error:
        print(f'Błąd: {error}')

def add_league(name):
    try:
        with cx_Oracle.connect('admin/admin@localhost:1521') as connection:
            with connection.cursor() as cursor:
                cursor.callproc('DODAJLIGE', [name])
    except cx_Oracle.Error as error:
        print(f'Błąd: {error}')

def remove_league(id):
    try:
        with cx_Oracle.connect('admin/admin@localhost:1521') as connection:
            with connection.cursor() as cursor:
                cursor.callproc('USUNLIGE', [id])
    except cx_Oracle.Error as error:
        print(f'Błąd: {error}')

def add_team_proc(name, league):
    try:
        with cx_Oracle.connect('admin/admin@localhost:1521') as connection:
            with connection.cursor() as cursor:
                data = [str(name), int(league), 2021]
                cursor.callproc('DODAJDRUZYNE2', data)
    except cx_Oracle.Error as error:
        print(f'Błąd: {error}')

def remove_team_proc(id):
    try:
        with cx_Oracle.connect('admin/admin@localhost:1521') as connection:
            with connection.cursor() as cursor:
                cursor.callproc('USUNDRUZYNE', [id])
    except cx_Oracle.Error as error:
        print(f'Błąd: {error}')

def scores_proc(team1, score1, score2, team2, id):
    try:
        with cx_Oracle.connect('admin/admin@localhost:1521') as connection:
            with connection.cursor() as cursor:
                cursor.callproc('ZMIENWYNIK', [team1, score1, score2, team2, id, 2021])
    except cx_Oracle.Error as error:
        print(f'Błąd: {error}')