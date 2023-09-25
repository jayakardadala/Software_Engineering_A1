from cx_Freeze import setup, Executable

setup(
    name="Fermat",
    version="0.1",
    description="This program allows the user to search for near misses to Fermat's Last Theorem.",
    executables=[Executable("fermat_near_miss.py")]
)
