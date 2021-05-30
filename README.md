# dbee.nvim


`dbee.nvim` is a SQL explorer in vim with Python as backend. Allow you setup a
database connection using an url which is processed by SQLAlchemy and returns
the query result in a new buffer.

# Installation


```vim
Plug 'https://github.com/mmngreco/debee.nvim' {':UpdateRemotePlugins'}
```

## Python dependencies

- sqlalchemy
- pandas

# Usage

- `:DBeeSetConnection <url>`: replace `<url>` with your desired connection
    string.
- `:DBeeInfo`: prints out the current connetion string.
- `:'<,'>DBeeQuery`: only in visual mode, returns the query output in a new buffer.

# Mapping

No mappings defined by default. You can define your own mapping adding
something like this in your `vimrc`:

```vim
vnoremap <C-q> DBeeQuery
```

# Development

```bash
./run.sh vim
./run.sh ipy
```
