import os

with open(os.path.join(os.path.dirname(__file__), 'event_ids.txt'), 'r') as fr:
    events = fr.read().split()

# public static final String SMARTMANAGER_OPTIMISE_TAP = "SmartManager_Optimise_Tap";

for event in events:
    print('    public static final String %s = "%s";' % (event.upper(), event))
