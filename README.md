divingintoipynb
===============

Diving into ipython notebook

Create ipython profile
---

    ipython profile create double11

    openssl genrsa -des3 -out mycert.key 2048
    openssl rsa -in mycert.key -out mycert.key
    openssl req -new -key mycert.key -out mycert.csr
    openssl x509 -req -days 365 -in mycert.csr -signkey mycert.key -out mycert.crt

    In [1]: from IPython.lib import passwd

    In [2]: passwd()
    Enter password:
    Verify password:
    Out[2]: 'sha1:9bb2d9f28625:c294b0ee5b13fd0ec26f19a0e4e52afe6bfd7561'

    e ~/.ipython/profile_double11/ipython_notebook_config.py

    c.IPKernerlApp.pylab = 'inline'
    c.NotebookApp.ip = '0.0.0.0'
    c.NotebookApp.open_browser = False
    c.NotebookApp.password = u'sha1:9bb2d9f28625:c294b0ee5b13fd0ec26f19a0e4e52afe6bfd7561'
    c.NotebookApp.port = 9999

    c.NotebookApp.certfile = u'/Users/dongweiming/.ipython/profile_double11/security/mycert.crt'
    c.NotebookApp.keyfile = u'/Users/dongweiming/.ipython/profile_double11/security/mycert.key'

    mkdir ~/.ipython/profile_double11/static/custom -p
    touch ~/.ipython/profile_double11/static/custom/custom.css
