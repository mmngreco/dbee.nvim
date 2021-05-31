if !has('python3')
    echo "No Python3 found, DBee.nvim will be disabled."
    finish
elseif exists('loaded_dbee')
    finish
endif

let loaded_dbee=1

function DBeeMarkBuffer()
    setlocal buftype=nofile
    setlocal bufhidden=hide
    setlocal noswapfile
    setlocal buflisted
    nnoremap <buffer> q :bd!<cr>
endfunction


" function DBeeInstallDependencies()
"     :python3 << EOF
"     from pathlib import Path

"     dbee_root = Path(vim.eval("expand('<sfile>:p:h')")) / '..'
"     dbee_installer = (dbee_root / "install.py").expanduser().absolute()
"     pybin = "pyfile"
"     vim.eval("%s -u %s" % (pybin, dbee_installer))

"     EOF
"     :UpdateRemotePlugins
" endfunction

autocmd! BufNewFile __DBee__ call DBeeMarkBuffer()
