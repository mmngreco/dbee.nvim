if exists('loaded_dbee')
    finish
endif
let loaded_dbee=1

echo 'Loaded dbee.nvim'

function DBeeMarkBuffer()
    setlocal buftype=nofile
    setlocal bufhidden=hide
    setlocal noswapfile
    setlocal buflisted
    nnoremap <buffer> q :bd!<cr>
endfunction

autocmd! BufNewFile __DBee__ call DBeeMarkBuffer()

