class Utils:
    @staticmethod
    def safe_int(val, default=0):
        try:
            return int(val)
        except:
            pass
        return default
