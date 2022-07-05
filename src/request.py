import requests
import time
from tqdm import tqdm
from unidecode import unidecode


class Request:
    def __init__(self, url: str, dictionary: str):
        self.url = url
        self.dictionary = dictionary

    def run(self):
        with open(self.dictionary, "r", encoding="utf-8") as f:
            lines = f.readlines()
            print(lines)
            k = 0
            # Loop in all words
            for word in tqdm(lines):
                word = unidecode(word.lower().replace('\n', ''))    # Do some cleaning
                request_url = self.url.replace("###", word)         # Append word to url
                r = requests.get(request_url)
                if r.status_code == 200:
                    print(f"Found: {word}")
                if k == 30:
                    k = 0
                    time.sleep(20)
                k+=1