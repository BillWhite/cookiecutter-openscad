import sys
import subprocess
from pathlib import Path

def make_assemblies(kind, strlist):
    names = [t.strip() for t in strlist.split(',') if t.strip() != ""]
    args = ["bin/make_assembly", f"--{kind}"] + names
    subprocess.run(args)

def make_source_files(strlist):
    names = [t.strip() for t in strlist.split(',') if t.strip() != ""]
    src = Path("src")
    for name in names:
        filepath = src / Path(f'{name}.scad')
        with open(filepath, "w") as of:
            pass
make_assemblies("assembly", "{{cookiecutter.main_assemblies}}")
make_assemblies("other", "{{cookiecutter.other_assemblies}}")
make_source_files("{{cookiecutter.other_source_files}}")




