import yaml


def getCheat():
    try:
        with open('config.yml', 'r') as f:
            config = yaml.load(f, Loader=yaml.FullLoader)
            return config['CHEAT']
    except FileNotFoundError:
        return None
    except KeyError:
        print("In config.yml, please set ('CHEAT') to true or false.")
        exit()


def getImpossible():
    try:
        with open('config.yml', 'r') as f:
            config = yaml.load(f, Loader=yaml.FullLoader)
            return config['IMPOSSIBLE']
    except FileNotFoundError:
        return None
    except KeyError:
        print("In config.yml, please set ('IMPOSSIBLE') to true or false.")
        exit()
