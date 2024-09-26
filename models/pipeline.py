import joblib

class Pipeline:

    def charge(self, url):
        return joblib.load(url)