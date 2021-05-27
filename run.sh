#!/usr/bin/env bash

case $1 in
    vim)
        nvim -u vimrc +UpdateRemotePlugin +qa && NVIM_LISTEN_ADDRESS=/tmp/nvim nvim -u vimrc tests/query.txt
        ;;
    ipy)
        ipython -i -c "from pynvim import attach; nvim = attach('socket', path='/tmp/nvim')"
        ;;
    tmux)
        tmux split-window -h "nvim -u ./tests/vimrc +UpdateRemotePlugin +qa && NVIM_LISTEN_ADDRESS=/tmp/nvim nvim -u vimrc tests/query.txt"
        tmux split-window -v "ipython -i -c \"from pynvim import attach; nvim = attach('socket', path='/tmp/nvim')\""
        ;;
    *)
        echo "Usage:"
        echo "./run.sh vim"
        echo "./run.sh ipy"
        echo "./run.sh tmux"
        ;;
esac
