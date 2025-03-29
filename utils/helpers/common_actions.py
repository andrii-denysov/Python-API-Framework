import json


class CommonActions:
    @staticmethod
    def parse_json(json_data):
        """
        Convert JSON string/bytes into python dict
        :param json_data: str or bytes of JSON format
        :return result dict
        """
        if isinstance(json_data, bytes):
            json_data = str(json_data, "utf8")
        try:
            return json.loads(json_data)
        except json.JSONDecodeError:
            return json.loads(json_data.replace("'", "\""))

    @staticmethod
    def build_query(dictionary: dict):
        """
        Transforms a dictionary into a specific string format.
        :param dictionary: dict with a search keyword and value to search
        :return: {"author": "Shakespeare", "title": "Sonnet"} -> "author,title/Shakespeare;Sonnet"
        """
        keys = ",".join(dictionary.keys())
        values = ";".join(dictionary.values())
        return f"{keys}/{values}"