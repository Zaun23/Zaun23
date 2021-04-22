import sys, csv, psycopg2

#taken from example ingestData file
db_host = sys.argv[-5]
db_port = sys.argv[-4]
db_name = sys.argv[-3]
db_user = sys.argv[-2]
db_password = sys.argv[-1]

#importing csv files
athletes_events_csv = sys.argv[1] #'AthleteEvents.csv’
host_cities_csv = sys.argv[2] #'HostCitites.csv'
noc_regions_csv = sys.argv[3] #'NOCRegions.csv'

#The following two functions are taken from the example python code -> used to transfer data from csv to lists
def csv_to_list(csv_name):
#gets data from the csv file and puts it into a list of lists
#for accessing the data: data_list[row_number][column_number]
    data_list = []
    with open(csv_name, 'r', encoding='utf-8') as csvfile:
      data_squads = csv.reader(csvfile)
      
      for row in data_squads:
        #to remove all the ', to have no collisions in the code later on
        new_row = []
        for element in row:
          if isinstance(element, str):
            element = element.replace("'", "`")
          new_row.append(element)
        #print(new_row)
            
        data_list.append(new_row)
      #deletes the fist row, which contains the table heads
      #optional:uncomment if this makes working with the data easier for you
      del data_list[0]
    return data_list

def semicolon_string_to_list(string):
#interprets all ; of the given string as separator of elements
#returns a list of strings
    return string.split(';')

athletes_events_list = csv_to_list(athletes_events_csv)
host_cities_list = csv_to_list(host_cities_csv)
noc_regions_list = csv_to_list(noc_regions_csv)

#estalishing sql connection
con = psycopg2.connect(
  host = db_host,
  port = db_port,
  database = db_name,
  user = db_user,
  password = db_password
)

cur = con.cursor()

def fillGamesTable():
  for index in range(len(host_cities_list)):
    temp_gyear = host_cities_list[index][3]
    temp_start = host_cities_list[index][4]
    temp_end = host_cities_list[index][5]
    temp_gname = temp_gyear + " Summer"
  
    if temp_gyear and temp_start and temp_end != '':  
      cur.execute("""
      INSERT INTO games (year, name, startdate, enddate) 
      VALUES (%s, %s, %s, %s)
      """,
      (temp_gyear, temp_gname, temp_start, temp_end))

def fillCountryTable():  
  for index in range(len(noc_regions_list)):
    temp_cname = noc_regions_list[index][1]
    
    if noc_regions_list[index][0] != '':
      temp_cnoc = noc_regions_list[index][0]
    else:
      temp_cnoc = None
    
    if noc_regions_list[index][2] != '':
      temp_pop = noc_regions_list[index][2]
    else:
      temp_pop = None

    if noc_regions_list[index][3]:
      temp_gdp = noc_regions_list[index][3]
    else:
      temp_gdp = None
    
    if temp_cname != '':
      
      cur.execute("""
      INSERT INTO countries (noc, name, population, gdp) 
      VALUES (%s, %s, %s, %s)
      """,
      (temp_cnoc, temp_cname, temp_pop, temp_gdp))
    
def fillCitiesTable():
  for index in range(len(host_cities_list)):
    temp_cityname = host_cities_list[index][2]
    temp_citynoc = host_cities_list[index][0]

    if len(temp_citynoc) <= 3:
      cur.execute("""
      INSERT INTO cities (name, noc)
      SELECT %s, %s WHERE NOT EXISTS
        (SELECT name FROM cities WHERE name = %s);
      """,
      (temp_cityname, temp_citynoc, temp_cityname))
    
def fillGamesInTable(): 
  cur.execute("SELECT year FROM games")
  games_year_list = cur.fetchall()

  cur.execute("SELECT ckey, name FROM cities")
  cities_list = cur.fetchall()

  counter = 0

  for index in games_year_list:
    temp_cyear = host_cities_list[counter][3]
    temp_cname = host_cities_list[counter][2]

    if int(index[0]) == int(temp_cyear):
      for iterator in cities_list:
        if iterator[1] == temp_cname:
          temp_ckey = iterator[0]
   
    cur.execute("""
              INSERT INTO gamesin (year, ckey)
              VALUES (%s, %s)
              """,
              (temp_cyear, temp_ckey))
    counter += 1

def fillTeamTable():
  for index in range(len(athletes_events_list)):
    temp_tname = athletes_events_list[index][6]
    temp_tnoc = athletes_events_list[index][7]
    temp_tyear = athletes_events_list[index][9]
    
    if temp_tname != '':
      
      cur.execute("""
      INSERT INTO teams (name, noc, year)
      SELECT %s, %s, %s WHERE NOT EXISTS
        (SELECT (name, year) FROM teams WHERE name = %s and year = %s)
      """,
      (temp_tname, temp_tnoc, temp_tyear, temp_tname, temp_tyear))
    
def fillAthleteTable():
  for index in range(len(athletes_events_list)):
    temp_aname = athletes_events_list[index][1]

    if athletes_events_list[index][0] != '':
      temp_akey = athletes_events_list[index][0]
    else:
      temp_akey = None

    if athletes_events_list[index][2] != '':
      temp_gender = athletes_events_list[index][2]
    else:
      temp_gender = None
    
    if athletes_events_list[index][3] != '':
      temp_dob = athletes_events_list[index][3]
    else:
      temp_dob = None
    
    if athletes_events_list[index][4] != '':
      temp_height = athletes_events_list[index][4]
    else:
      temp_height = None

    if athletes_events_list[index][5] != '':
      temp_weight = athletes_events_list[index][5]
    else: 
      temp_weight = None

    if temp_aname != '':
      
        cur.execute("""
        INSERT INTO athletes (akey, name, gender, dob, height, weight)
        SELECT %s, %s, %s, %s, %s, %s WHERE NOT EXISTS
          (SELECT akey FROM athletes WHERE akey = %s)
        """,
        (temp_akey, temp_aname, temp_gender, temp_dob, temp_height, temp_weight, temp_akey))

def fillTeamAthletesTable():
  cur.execute("SELECT name, year, tkey FROM teams")
  temp_team_list = cur.fetchall()

  for index in range(len(athletes_events_list)):
    temp_tyear = athletes_events_list[index][9]
    temp_tname = athletes_events_list[index][6]
    temp_aid = athletes_events_list[index][0]
    
    for iterator in temp_team_list:
      if (iterator[0], iterator[1]) == (temp_tname, int(temp_tyear)):
        temp_tkey = iterator[2]

    cur.execute("""
    INSERT INTO teamathletes (tkey, akey)
    SELECT %s, %s WHERE NOT EXISTS
      (SELECT akey FROM teamathletes WHERE akey = %s)
    """,
    (temp_tkey, temp_aid, temp_aid))

def fillEventsTable():
  for index in range(len(athletes_events_list)):
    temp_event_name = athletes_events_list[index][12]
    temp_sport = athletes_events_list[index][11]

    cur.execute("""
    INSERT INTO events (eventname, sportname)
    SELECT %s, %s WHERE NOT EXISTS
      (SELECT eventname FROM events WHERE eventname = %s)
    """,
    (temp_event_name, temp_sport, temp_event_name))

def fillResultsTable():
  cur.execute("SELECT ekey, eventname FROM events")
  temp_event_list = cur.fetchall()
  
  for index in range(len(athletes_events_list)):
    temp_akey = athletes_events_list[index][0]
    temp_year = athletes_events_list[index][9]
    
    temp_medal = athletes_events_list[index][13]
    if temp_medal == "Gold":
      temp_medal = 'G'
    elif temp_medal == "Silver":
      temp_medal = 'S'
    elif temp_medal == "Bronze":
      temp_medal = 'B'
    
    temp_ename = athletes_events_list[index][12]
    
    if temp_medal != '':
      for event in temp_event_list:
        if temp_ename == event[1]:
          temp_ekey = event[0]

      cur.execute("""
      INSERT INTO results
      VALUES (%s, %s, %s, %s)
      """,
      (temp_year, temp_ekey, temp_akey, temp_medal))

#Calling all functions to fill tables
#TODO -> uncomment everything
fillGamesTable()
fillCountryTable()
fillCitiesTable()
fillGamesInTable()
fillTeamTable()
fillAthleteTable()
fillTeamAthletesTable()
fillEventsTable()
fillResultsTable()

#don't forget to uncomment everything
#con.commit() #we dont commit
cur.close()
con.close()
