from prefect import flow, task
import httpx


BASE_URL = "https://pokeapi.co/api/v2/pokemon"

@task
def do_request():
    res = httpx.get(url=f"{BASE_URL}/2")
    return res.json()

@flow(name='Simple Request flow')
def run_flow():
    res = do_request()
    print(res)

run_flow()