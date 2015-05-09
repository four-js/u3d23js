import yaml

scene_file = 'samples/cubes/Assets/main.unity'
docs = yaml.load_all(file(scene_file, 'r'))
try:
    for doc in docs:
        for k,v in doc.items():
            print k, "->", v
        print "\n",
except Exception, e:
    print e

