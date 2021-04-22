#ALTER SHIZZLE VON CITY
# city_serial = 0

# def checkCityDuplicates(index, set_to_check):
#   temp_city_list = []
  
#   for row in set_to_check:
#     temp_city_list.append(row[1])

#   if host_cities_list[index][2] in temp_city_list:
#     return False
#   else:
#     return True

# for index in range(len(host_cities_list)):
#   temp_cityname = host_cities_list[index][2]
#   temp_citynoc = host_cities_list[index][0]
  
#   cur.execute("SELECT * FROM cities")
#   temp_city_set = cur.fetchall()

#   if temp_cityname and temp_citynoc != ' ':
#     if checkCityDuplicates(index, temp_city_set):
#       if len(temp_citynoc) <= 3:
            
#             cur.execute("""
#             INSERT INTO cities (ckey, name, noc)
#             VALUES (%s, %s, %s)
#             """,
#             (city_serial, temp_cityname, temp_citynoc)) 
            
#             city_serial += 1



# ALTER SHIZZLE VON COUNTRY:
# for index in range(len(noc_regions_list)):
#   temp_cname = noc_regions_list[index][1]
  
#   if noc_regions_list[index][0] != '':
#     temp_cnoc = noc_regions_list[index][0]
#   else:
#     temp_cnoc = None
  
#   if noc_regions_list[index][2] != '':
#     temp_pop = noc_regions_list[index][2]
#   else:
#     temp_pop = None

#   if noc_regions_list[index][3]:
#     temp_gdp = noc_regions_list[index][3]
#   else:
#     temp_gdp = None
  
#   if temp_cname != '':
    
#     cur.execute("""
#     INSERT INTO countries (noc, name, population, gdp) 
#     VALUES (%s, %s, %s, %s)
#     """,
#     (temp_cnoc, temp_cname, temp_pop, temp_gdp))
  
#   # elif temp_cnoc and temp_cname != ' ':
    
#   #   cur.execute("""
#   #   INSERT INTO countries (noc, name) 
#   #   VALUES (%s, %s)
#   #   """,
#   #   (temp_cnoc, temp_cname))


######################################################
# FOLLOWING BLOCK CONTAINS CODE FOR TEAM TABLE
######################################################
team_serial = 0

def checkTeamDuplicates(name, year, set_to_check):
  temp_team_list = []
  
  for row in set_to_check:
    temp_team_list.append((row[1], row[3]))

  if ((name, int(year))) in temp_team_list:
    return False
  else:
    return True

for index in range(len(athletes_events_list)):
  temp_tname = athletes_events_list[index][6]
  temp_tnoc = athletes_events_list[index][7]
  temp_tyear = athletes_events_list[index][9]

  cur.execute("SELECT * FROM teams")
  temp_teams_set = cur.fetchall()
  
  if temp_tname != ' ':
    if checkTeamDuplicates(temp_tname, temp_tyear, temp_teams_set):

      cur.execute("""
      INSERT INTO teams (tkey, name, noc, year)
      VALUES (%s, %s, %s, %s)
      """,
      (team_serial, temp_tname, temp_tnoc, temp_tyear))

      team_serial += 1


def checkAthleteDuplicates(akey, set_to_check):
  temp_athlete_list = []
  
  for row in set_to_check:
    temp_athlete_list.append(row[0])

  if int(akey) in temp_athlete_list:
    return False
  else:
    return True





#NEW CITY SHIZZLE:
city_serial = 1
for index in range(len(host_cities_list)):
  temp_cityname = host_cities_list[index][2]
  temp_citynoc = host_cities_list[index][0]

  if len(temp_citynoc) <= 3:
    cur.execute("""
    INSERT INTO cities (ckey, name, noc)
    SELECT %s, %s, %s WHERE NOT EXISTS
      (SELECT name FROM cities WHERE name = %s);
    """,
    (city_serial, temp_cityname, temp_citynoc, temp_cityname))
    
    city_serial += 1



def fillGamesInTable(): 
#TODO -> fix this wonky mess
  game_year_list = []

  cur.execute("SELECT * FROM games")
  games = cur.fetchall()
  for row in games:
    game_year_list.append(row[0])

  cur.execute("SELECT * FROM cities")
  cities = cur.fetchall()

  for index in range(len(game_year_list)):
    for iterator in range(len(host_cities_list)):
      if int(game_year_list[index]) == int(host_cities_list[iterator][3]):
        
        for its_complicated in cities:
          if host_cities_list[iterator][2] == its_complicated[1]:
            temp_ckey = its_complicated[0]
        
    cur.execute("""
              INSERT INTO gamesin (year, ckey)
              VALUES (%s, %s)
              """,
              (game_year_list[index], temp_ckey))