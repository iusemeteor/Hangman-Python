import yaml

def get_token():
    try:
        with open('config.yml', 'r') as f:
            config = yaml.load(f, Loader=yaml.FullLoader)
            return config['token']
    except FileNotFoundError:
        return None

def getGuildID():
    try:
        with open('config.yml', 'r') as f:
            config = yaml.load(f, Loader=yaml.FullLoader)
            return config['guild_id']
    except FileNotFoundError:
        return None
    
def get_characterai_token():
    try:
        with open('config.yml', 'r') as f:
            config = yaml.load(f, Loader=yaml.FullLoader)
            return config['character_ai_token']
    except FileNotFoundError:
        return None

def get_characterai_character_id():
    try:
        with open('config.yml', 'r') as f:
            config = yaml.load(f, Loader=yaml.FullLoader)
            return config['character_ai_character_id']
    except FileNotFoundError:
        return None

def get_dms_only():
    try:
        with open('config.yml', 'r') as f:
            config = yaml.load(f, Loader=yaml.FullLoader)
            return config['dms_only']
    except FileNotFoundError:
        return None
    except KeyError:
        return False  # Default to False if the key is missing

def getDebug():
    try:
        with open('config.yml', 'r') as f:
            config = yaml.load(f, Loader=yaml.FullLoader)
            return config['debug']
    except FileNotFoundError:
        return None
    except KeyError:
        return False  # Default to False if the key is missing