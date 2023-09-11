from fastapi import FastAPI

from anagrams import get_actors_names, search_for_anagrams

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World1"}


@app.get("/anagram/{letters}")
def read_item(letters: str):

    names = get_actors_names()
    anagrams = search_for_anagrams(letters, names)
    if len(anagrams) == 0:
        return {"No matches!  ¯ \ _ (ツ) _ / ¯.  "}
    return anagrams
