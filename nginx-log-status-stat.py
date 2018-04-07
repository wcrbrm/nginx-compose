# HOURLY STAT example:
#  { "dt": "2018-04-03", "h": "14", "m": "00-59", "s": {200: 40, 301: 4}, "by_location": [{ location: "cdn", "s": {200: 40, 301: 4}}] }

# by default - no location
# list of locations could be read by same YML files
# less +F /var/log/nginx/access.log | nginx-log-statuses -f --config ./*.yml --per-hour=1