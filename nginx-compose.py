import yaml

# yaml documentation:
# http://pyyaml.org/wiki/PyYAMLDocumentation
# yaml include:
# https://stackoverflow.com/questions/528281/how-can-i-include-an-yaml-file-inside-another

with open("examples/motor.yml", 'r') as stream:
  try:
    print(yaml.load(stream))
  except yaml.YAMLError as exc:
    print(exc)
