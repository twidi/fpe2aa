method = 'HOSTNAME'
rules = (
    # hostname       # settings to load (in the "settings" directory)
    (r'^twidi-r700', ('dev', 'local/twidi-r700')),
    (r'^presidapps.*-www(?:\-\d+)?', ('prod', 'dotcloud', 'local/prod')),
)

