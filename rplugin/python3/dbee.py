import pynvim
import sqlalchemy as sa
import pandas as pd


class DBeeError(Exception):
    pass


@pynvim.plugin
class DBee(object):

    def __init__(self, nvim):
        self.nvim = nvim
        self.qry_counter = 0
        self.connection = None
        self.engine = None
        self.url = None
        self.is_ready = False
        self.pandas_kw = dict()

    def buffer_name(self, n):
        """Build a buffer name."""
        buffer_name_fmt = "__DBee_%s__"
        return buffer_name_fmt % n

    @pynvim.command('DBeeInfo')
    def info(self):
        """Print out connection information."""
        self.nvim.command("echo 'DBee is using %s'" % self.url)

    @pynvim.command('DBeeBuffer')
    def mark_buffer(self):
        """Mark a buffer as an Scratch.

        Creates an scratch or temporal buffer to store the query. Also adds 'Q'
        as mapping to delete the buffer.
        """
        send_cmd = self.nvim.command
        # cmd("setlocal nobuflisted noswapfile buftype=nofile bufhidden=delete")
        send_cmd("nnoremap <buffer> gq :q<cr>")
        send_cmd("echo 'Press gq to close the buffer.'")

    def get_selection(self):
        reg = "a"
        prev_reg = self.nvim.command_output("echo getreg('%s')" % reg)
        self.nvim.command("normal! gv\"%sy" % reg)
        out = self.nvim.command_output("echo getreg('%s')" % reg).strip()
        self.nvim.command("echo '%s'" % out)
        self.nvim.command("call setreg('%s', '%s')" % (reg, prev_reg))
        return out

    @pynvim.command('DBeeSetConnection', nargs='*', range='')
    def set_connection(self, url, range):
        """Set connection.

        Update the url attribute and creates an sqlalchemy engine with it.

        Parameters
        ----------
        url : list(str)

        Example
        -------
        >>> :DBeeSetConnection sqlite:///./dbee.nvim/tests/chinook.db
        Configurated sqlite:///./dbee.nvim/tests/chinook.db
        """
        if len(range) and not len(url):
            # Visual mode
            _url = self.get_selection()
            self.url = _url
        elif isinstance(url, list):
            # Command mode
            _url = url[0]
            self.url = _url
        else:
            raise NotImplementedError("url not processed, %s" % url)

        engine = sa.create_engine(_url)
        self.connection = engine.connect()
        self.engine = engine
        self.nvim.command("echo 'Configurated %s'" % _url)
        self.is_ready = True

        return self.is_ready

    @pynvim.command('DBeeSetPandasKw', nargs='*')
    def set_pandas_kw(self, args):
        """Change pandas keyword.

        Parameters
        ----------
        args : list

        Example
        -------
        >>> :DBeeSetPandasKw 'max_cols=30' 'decimal=","'
        """
        for arg in args:
            k, v = arg.split("=")
            self.pandas_kw[k] = eval(v)

    def new_buffer(self):
        """Creates a new buffer."""
        # TODO smart buffee
        nvim = self.nvim
        nvim.command(":setlocal splitright")

        bufname = self.buffer_name(self.qry_counter)
        nvim.command(":vsplit %s" % bufname)

        self.mark_buffer()

        buffer = nvim.current.buffer
        return buffer

    def read_sql(self, q, eng):
        """Read sql query."""
        out = pd.read_sql(q, eng)
        self.qry_counter += 1
        return out

    def append_header(self, buffer, url, query_list):
        """Include header to a buffer."""

        head_url = "url: %s" % url
        buffer[:] = [head_url, ""]

        for i, qry in enumerate(query_list):
            prefix = ".......:"
            if i == 0:
                prefix = "In[%03d]:" % self.qry_counter
            head_qry = "%s %s" % (prefix, qry)
            buffer.append(head_qry)

        buffer.append("")

    @pynvim.command('DBeeQuery', nargs='*', range='')
    def get_query(self, args, range):
        """Read queries."""
        url = self.url
        if not self.is_ready:
            msg = "Connection is not configurated yet. "
            msg += "You can use `:DBeeSetConnection <url>`."
            raise DBeeError(msg)

        # get selected query
        ini, end = range
        nvim = self.nvim
        query_list = nvim.current.buffer[ini-1:end]  # vim starts at 0

        # create a buffer and fill it with the query
        buffer = self.new_buffer()
        self.append_header(buffer, url, query_list)

        # read the query
        query = " ".join(query_list)
        query_out = self.read_sql(query, self.connection)

        query_out_list = query_out.to_string(**self.pandas_kw).split("\n")
        buffer.append(query_out_list)
