
def yamlize(ws="WS02_AOO_SCHEMA"):
  uri = "http://www.indicepa.gov.it/public-services/docs-read-service.php?dstype=FS&filename=%s.json" % ws
  s = yaml.load(urlopen(uri).read().replace("\t",""))
  yaml.dump(s,default_flow_style=1)
  schema_name = s['name']
  schema_content = s['properties']
  d = {schema_name: {'properties': s['properties']}}
  with open(ws+".schema", "w") as fh:
    fh.write(yaml.dump(d, default_flow_style=0))
  
for ws in """WS02_AOO_SCHEMA WS01_SFE_CF_SCHEMA WS08_AOOC_SCHEMA WS03_OU_SCHEMA WS04_SFE_SCHEMA WS05_AMM_SCHEMA WS06_OU_CODUNI_SCHEMA WS07_EMAIL_SCHEMA""".split():
  print("yamlizing ", ws)
  try:
    yamlize(ws)
  except Exception as e:
    print(e)
