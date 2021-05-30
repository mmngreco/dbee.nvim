let &runtimepath.=','.escape(expand('<sfile>:p:h'), '\,')
vnoremap <C-q> :DBeeQuery<cr>

" DBeeSetConnection sqlite:////home/mgreco/gitlab/mmngreco/dbee.nvim/tests/chinook.db
