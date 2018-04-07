# nginx-compose
Nginx config generation based on YAML file

nginx compose
```
  -) reads configuration file
  -) build collection of var
  -) build collection of temlates
  -) build collection of each (for location)
  -) DENY sections locations to deny 
  -) write upstreams
  -) write servers with all locations
```