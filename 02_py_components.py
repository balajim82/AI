"""
1. This file we are going discuss about Programming components.
    1. Constants
    2. Literals
    3. Identifiers
    4. varibles
    5. Reserved Words
"""

# Constants
# In Python, there is no Specific to mention as constant like in Java.
# for coding understanding, will give as capitalvalue and assign value.

GLOBAL_CONSTANT = 255
print("Value of Constant", GLOBAL_CONSTANT)

import keyword

print(keyword.kwlist)

# keywords should not as constants, identifiers, varibles.

# constants and varibles are subset of identifiers
# Rules for Identifiers
# 1. Allowed chars A-Z , a-z, 0-9, _
# 2. Special Keywords should not use ex: if, elif, def, int
# 3. identifiers are case sesitive.
# 4. Avoid using any identifier start or ends with __

# Examples
num = 10  # Valid
_num = 10  # Valid
__num = 12  # not Recommandable.
print(_num)
