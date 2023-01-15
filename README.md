This project contains files that may be used for OpenScad projects.

## Usage

1. Install python3. Use your own judgement.
1. Install [cookiecutter](https://cookiecutter.readthedocs.io/en/stable/index.html).
1. Wherever you store your OpenScad projects, run: `$ cookiecutter gh:BillWhite/cookiecutter-openscadpackage`
   and answer the questions.
1. You will find a new folder with the name you gave. This folder will have 
   1. A `Makefile`.
   1. A `.gitignore` file.
   1. A `src` directory, which includes all OpenScad sources.
   1. A file named `assemblies.txt`.
1. In the file `assemblies.txt`, list the names of all the OpenScad sources in src without 
the initial `src/`. There may be other files in `src/` as well, but all top level assemblies
should be listed in `assemblies.txt`.
1. Run `$ make` to create the `.stl` files. They will show up in the `stl/` folder, which
`make` will create.
1. Dependencies will be stored in a folder named `.deps/`. But this is handled
silently. Make uses these to try to avoid unnecessary OpenScad runs.
1. All `stl/*.stl` files and dependency files are ignored by the .gitignore file, so they
will not be committed into git.
1. The command `$ make clean` removes the `stl/` and `.deps/` folders.

## An Example

For example, if `assemblies.txt` has the content:
   ```
   knob
   handle
   cover
   ```
then `src/` should have files `knob.scad`, `handle.scad` and `cover.scad`. There could
be other files in `src/`.

Running `make` creates `stl/knob.stl`, `stl/handle.stl` and `stl/cover.stl`.

Touching `src/knob.scad` then running `$ make` will make `stl/knob.stl` only.

Running `make clean` deletes all the temp files, `stl/` and `.deps/`.

