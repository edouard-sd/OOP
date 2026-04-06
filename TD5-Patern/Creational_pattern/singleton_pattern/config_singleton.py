class ConfigManager:
    _instance = None
    
    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = ConfigManager()
        return cls._instance

    def __init__(self):
        if ConfigManager._instance is not None:
            raise Exception("This class is a singleton!")
        # Simulate loading file once
        self.config = {"database": {"host": "localhost"}, "app": {"debug": True}}

    def get(self, key: str):
        keys = key.split(".")
        value = self.config
        for k in keys:
            if isinstance(value, dict):
                value = value.get(k)
            else:
                return None
        return value

if __name__ == "__main__":
    # First call loads the file
    config = ConfigManager.get_instance()
    
    # Subsequent calls return same instance (no file read)
    config2 = ConfigManager.get_instance()
    
    # Access values
    db_host = config.get("database.host")
    debug = config.get("app.debug")
    print(f"db_host: {db_host}, debug: {debug}")\n