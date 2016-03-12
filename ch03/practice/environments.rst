Per creare un ambiente virtuale Python 2.7.8 con pyenv, chiamato ``myproject``,
si usa il comando ``pyenv virtualenv``::

    $ pyenv shell 2.7.8
    $ pyenv virtualenv myproject


Per fare la stessa cosa con conda::

    $ conda create -n myproject python=2.7.8
