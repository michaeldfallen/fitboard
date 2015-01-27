import requests, json

fitbit_url = "https://www.fitbit.com/ajaxapi"

def groupDashboard(group_id):
  request_enc = (
    'request=%7B%22template%22%3A%22%2Fmgmt%2FajaxTemplate.jsp%22'
    '%2C%22serviceCalls%22%3A%5B%7B%22name%22%3A%22leaderboardAjaxService'
    '%22%2C%22args%22%3A%7B%22encodedGroupId%22%3A%22'
    ''+group_id+''
    '%22%7D%2C%22method%22%3A%22getCurrentGroupGraphData%22%7D%5D%7D'
  )

  r = requests.post(
    "https://www.fitbit.com/ajaxapi",
    data = request_enc,
    headers = { 'Content-Type': 'application/x-www-form-urlencoded' },
    cookies = {
      "u": ".2|22903264|368BD7AE-B91F-EA60-8B29-AA0FD78F1140|1421242746798|31536000",
    }
  )

  if r.status_code == 200:
    return json.loads(r.text)
  else:
    return {}
