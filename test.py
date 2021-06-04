import cProfile
from main import main

cProfile.run("main(True)", sort='cumulative')