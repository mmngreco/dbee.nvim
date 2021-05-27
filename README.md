# Example Neovim Python Plugin

very wip!!!!


```bash
./run.sh
```

```bash
nvim -u vimrc +UpdateRemotePlugin +qa && NVIM_LISTEN_ADDRESS=/tmp/nvim nvim -u vimrc tests/query.txt
ipython -i -c "from pynvim import attach; nvim = attach('socket', path='/tmp/nvim')"
```

To test from python

```python
>>> from pynvim import attach
>>> nvim = attach('socket', path='/tmp/nvim')
>>> buffer = nvim.current.buffer # Get the current buffer
>>> buffer[0] = 'replace first line'
>>> buffer[:] = ['replace whole buffer']
>>> nvim.command('vsplit')
>>> nvim.windows[1].width = 10
>>> nvim.vars['global_var'] = [1, 2, 3]
>>> nvim.eval('g:global_var')
nvim.eval("getline(a:firstline, a:lastline)")
```


