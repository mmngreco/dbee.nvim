if !has('python3')
    echo "No Python3 found, DBee.nvim will be disabled."
    finish
elseif exists('g:loaded_dbee')
    finish
endif

let g:loaded_dbee=1
