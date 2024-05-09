class VersionUtil:
    @staticmethod
    def get_version():
        try:
            with open("VERSION.txt", "r") as file:
                return "App v" + file.read().strip()
        except FileNotFoundError:
            return "Version information not found"
