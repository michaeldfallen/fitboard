import fitbit, json

class Group:
  def __init__(self, name, group_id):
    self.name = name
    self.group_id = group_id

class GroupStats:
  def __init__(self, json):
    self.total_steps = json['totalSteps']
    self.total_miles = json['totalMiles']
    self.total_very_active_minutes = json['totalVeryActiveMinutes']
    self.top_member = json['graphData'][0]

groups = [
  Group("Belfast", "22QDSC"),
  Group("Bristol", "22QDVN"),
  Group("Derry", "22QDS4"),
  Group("Dublin", "22QDN9"),
  Group("Gdańsk", "22QDL3"),
  Group("London", "22QF5M"),
  Group("Reading", "22QF5J"),
  Group("Swansea", "22QDYD"),
]

def download_todays_stats(group):
  json = fitbit.groupDashboard(group.group_id)
  GroupStats(json)

def download_all_groups_stats():
  for group in groups:
    download_todays_stats(group)

