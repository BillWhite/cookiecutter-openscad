import subprocess
from pathlib import Path

def str2list(strlist) -> list[str]:
    if not strlist:
        return []
    return [t.strip() for t in strlist.split(',') if t.strip() != ""]

def make_assemblies(kind, strlist):
    names = str2list(strlist)
    args = ["bin/make_assembly", f"--{kind}"] + names
    subprocess.run(args)

def make_source_files(strlist, contents=[]):
    names = str2list(strlist)
    src = Path("src")
    for name in names:
        filepath = src / Path(f'{name}.scad')
        with open(filepath, "w") as of:
            for line in contents:
                of.write(line + '\n')

def make_one_assembly_definition(namelist) -> list[str]:
    answer = []
    for name in namelist:
        answer += ['module ' + name + ' {', '}']
    return answer

CONFIG_CONTENTS =['include <GRISCAD/units.scad>',
                  'include <GRISCAD/vectors.scad>'];

make_assemblies("assembly", "{{cookiecutter.main_assemblies}}")
make_assemblies("other", "{{cookiecutter.other_assemblies}}")
make_source_files("{{cookiecutter.other_source_files}}")
make_source_files("config",
                  (CONFIG_CONTENTS if ("{{cookiecutter.use_griscad}}" == 'y') else []))

make_source_files("{{cookiecutter.main_file}}",
                  ["include <config.scad>"]
                  + make_one_assembly_definition(str2list("{{cookiecutter.main_assemblies}}"))
                  + make_one_assembly_definition(str2list("{{cookiecutter.other_assemblies}}")))
make_source_files("{{cookiecutter.other_source_files}}",
                  ["include <config.scad>"])

