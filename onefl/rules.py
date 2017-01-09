"""
Goal: Store logic related to hashing data according to
predefined rules.

Authors:
     Andrei Sura <sura.andrei@gmail.com>
"""

# TODO: research the claim from
# L. Sweeney. k-anonymity: a model for protecting privacy.
# International Journal on Uncertainty, Fuzziness and Knowledge-based Systems
#
# "...87% (216 million of 248 million) of the population in the
#   United States had reported characteristics that likely made them
#   unique based only on {5-digit ZIP, gender, date of birth}."

from onefl import utils  # noqa
from onefl.normalized_patient import NormalizedPatient  # noqa


# _1 First Name + Last Name + DOB + Gender
RULE_CODE_F_L_D_G = 'F_L_D_G'

# _2 Last Name + First Name + DOB + Race
RULE_CODE_F_L_D_R = 'F_L_D_R'


# In order to guarantee correctness we will allow the partners
# to add to the configuration only values from the map below.
# If we add new rules then we will ask the partners to download a new version
# of the client software.
AVAILABLE_RULES_MAP = {

    RULE_CODE_F_L_D_G: {
        'required_attr': ['pat_first_name', 'pat_last_name', 'pat_birth_date', 'pat_gender'],  # NOQA
        'pattern': '{0.pat_first_name}{0.pat_last_name}{0.pat_birth_date}{0.pat_gender}',  # NOQA
    },
    RULE_CODE_F_L_D_R: {
        'required_attr': ['pat_first_name', 'pat_last_name', 'pat_birth_date', 'pat_race'],  # NOQA
        'pattern': '{0.pat_last_name}{0.pat_first_name}{0.pat_birth_date}{0.pat_race}',  # NOQA
    },
}
