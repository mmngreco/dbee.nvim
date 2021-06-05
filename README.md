# dbee.nvim

`dbee.nvim` is a SQL explorer in vim with Python as backend. Allow you setup a
database connection using an url which is processed by SQLAlchemy and returns
the query result in a new buffer.

![](https://i.imgur.com/N2W8dbB.gif) 

# Installation

## Python dependencies

- `SQLAlchemy`
- `pandas`


Add de following in your `vimrc`:

```vim
Plug 'https://github.com/mmngreco/debee.nvim', { 'do': './install.py' }
```

> Note: `python3 ./install.py` will install dependencies required in
> `requirements-base.txt`

If your prefer to manage dependencies yourself, you can add the following
instead:

```vim
Plug 'https://github.com/mmngreco/debee.nvim'
```

and then you will need to execute `pip install -r requirements-base.py` in the
python environment used by vim.

## Update remote plugins

After running plug installation, you will need to execute
`:UpdateRemotePlugins` to include the python code in vim, and restart.

```vim
:UpdateRemotePlugins
:qa
```

# Usage

- `:DBeeSetConnection <url>`: replace `<url>` with your desired connection
    string.
- `:DBeeInfo`: prints out the current connetion string.
- `:'<,'>DBeeQuery`: only in visual mode, returns the query output in a new buffer.

# Mapping

No mappings defined by default. You can define your own mapping adding
something like this in your `vimrc`:

```vim
vnoremap <C-q> :DBeeQuery<cr>
vnoremap <C-c> :DBeeSetConnection<cr><cr>
```

# Development

```bash
conda create -n dbee.nvim python=3.8
conda activate dbee.nvim
pip install -r requirements.txt
```

```bash
./run.sh vim
./run.sh ipy
```
