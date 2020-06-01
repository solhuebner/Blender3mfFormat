# Blender add-on to import and export 3MF files.
# Copyright (C) 2020 Ghostkeeper
# This add-on is free software: you can redistribute it and/or modify it under the terms of the GNU Affero General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
# This add-on is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU Affero General Public License for details.
# You should have received a copy of the GNU Affero General Public License along with this plug-in. If not, see <https://gnu.org/licenses/>.

# <pep8 compliant>

"""
This module contains mocks for Blender's API.

The mocks in this module are meant to be very basic mocks. They will not return
anything special or do anything. They are just meant to remove the basic import
errors and add the missing names.
"""

class MockOperator:
    pass

class MockImportHelper:
    pass

class MockExportHelper:
    pass
