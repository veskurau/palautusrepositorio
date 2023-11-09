import toml
from urllib import request
from project import Project


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        #print(content)
        parsed_toml = toml.loads(content)
        #print(parsed_toml)
        name = parsed_toml["tool"]["poetry"]["name"]
        description = parsed_toml["tool"]["poetry"]["description"]
        dependencies = parsed_toml["tool"]["poetry"]["dependencies"]
        dev_dependencies = parsed_toml["tool"]["poetry"]["group"]["dev"]["dependencies"]
        #rint(dependencies)
        #print(f"Name on: {name}")

        #new_toml_string = toml.dumps(parsed_toml)
        #print(new_toml_string)

        # with open('new_toml_file.toml', 'w') as f:
        #     new_toml_string = toml.dump(parsed_toml, f)
        # print(new_toml_string)

        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        return Project(name, description, dependencies, dev_dependencies)
