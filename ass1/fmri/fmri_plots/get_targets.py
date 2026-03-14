## Please install Nilearn before running this code

from nilearn import datasets

# Subject 1
haxby = datasets.fetch_haxby(subjects=(1,), fetch_stimuli=True)
print(haxby['session_target'])  # This tells you path to the target file


# Subject 2
haxby = datasets.fetch_haxby(subjects=(2,), fetch_stimuli=True)
print(haxby['session_target'])  # This tells you path to the target file

# Subject 3
haxby = datasets.fetch_haxby(subjects=(3,), fetch_stimuli=True)
print(haxby['session_target'])  # This tells you path to the target file

# Subject 4
haxby = datasets.fetch_haxby(subjects=(4,), fetch_stimuli=True)
print(haxby['session_target'])  # This tells you path to the target file

# Subject 5
haxby = datasets.fetch_haxby(subjects=(5,), fetch_stimuli=True)
print(haxby['session_target'])  # This tells you path to the target file
