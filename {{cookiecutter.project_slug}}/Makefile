ASSEMBLIES=$(shell cat assemblies.txt)
OTHERS=$(shell cat others.txt)
DEP_DIR=.deps
STL_DIR=stl
OTHER_STL_DIR=other_stl
SRC_DIR=src
DIRS=$(DEP_DIR) $(STL_DIR) $(OTHER_STL_DIR)
CLEANOBJS=$(DIRS)

OBJS=$(patsubst %, $(STL_DIR)/%.stl, $(ASSEMBLIES))
OTHER_OBJS=$(patsubst %,$(OTHER_STL_DIR)/%.stl, $(OTHERS))
DEPS=$(patsubst %, $(DEP_DIR)/%.d, $(ASSEMBLIES) $(OTHERS))

$(print $(OTHER_OBJS))

target: $(OBJS) | dirs

others: $(OTHER_OBJS) | dirs

everything: target others

$(STL_DIR)/%.stl: $(SRC_DIR)/%.scad | dirs
	openscad -o $@ $< -d $(DEP_DIR)/$*.d

$(OTHER_STL_DIR)/%.stl: $(SRC_DIR)/%.scad | dirs
	openscad -o $@ $< -d $(DEP_DIR)/$*.d

dirs:
	mkdir -p $(DIRS)

clean:
	rm -rf $(CLEANOBJS)

-include $(DEPS)

########################################################################
#  This file is part of cookiecutter-openscadpackage.
#
#  cookiecutter-openscadpackage is free software: you can redistribute it
#  and/or modify it under the terms
#  of the GNU General Public License as published by the Free Software Foundation,
#  either version 3 of the License, or (at your option) any later version. 
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
#  FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License along
#  with this program. If not, see <https://www.gnu.org/licenses/>.
#
########################################################################
