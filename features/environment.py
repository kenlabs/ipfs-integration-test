import json

def before_all(context):
    context.config = None

def before_scenario(context, scenario):
    f = open("config.json")
    context.config = json.load(f)
    f.close()
