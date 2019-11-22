from ruamel.yaml import YAML

yaml = YAML(typ='safe')

def load_config(config_file_path):
    """
    Load the YAML file from the config_file_path and return a dictionary
    with the YAML configuration

    Parameters
    ----------
    config_file_path : str
        The path to the YAML file

    Returns
    -------
    yaml
    """
    with open(config_file_path, 'r') as stream:
        return yaml.load(stream)

