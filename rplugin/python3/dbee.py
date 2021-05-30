import pynvim
import sqlalchemy as sa
import pandas as pd


@pynvim.plugin
class DBee(object):

    def __init__(self, nvim):
        self.nvim = nvim
        self.connection = None
        self.engine = None
        self.url = None
        self.is_ready = False

    @pynvim.command('DBeeInfo')
    def info(self):
        self.nvim.command("echo 'DBee is using %s'" % self.url)

    @pynvim.command('DBeeSetConnection', nargs='*')
    def set_connection(self, url):

        if isinstance(url, list):
            _url = url[0]
            self.url = _url
        else:
            _url = self.url

        self.nvim.command("echo 'Configurated %s'" % _url)

        engine = sa.create_engine(_url)
        self.connection = engine.connect()
        self.engine = engine
        self.is_ready = True

    def new_buffer(self):
        nvim = self.nvim
        nvim.command(":setl splitright")
        nvim.command(":vsplit __DBee__")

    @pynvim.command('DBeeQuery', nargs='*', range='')
    def get_query(self, args, range):

        if not self.is_ready:
            if len(args):
                url = args[0]
            else:
                url = self.url

            self.set_connection(url)

        # get selected query
        ini, end = range
        nvim = self.nvim
        query = nvim.current.buffer[ini-1:end]

        # creates a new buffer and put the query and output there
        self.new_buffer()
        cur_buffer = nvim.current.buffer
        cur_buffer[:] = [">>> %s" % q for q in query] + [""]
        query_out = pd.read_sql(query[0], self.connection)
        kw = dict(max_colwidth=30)
        cur_buffer.append(query_out.to_string(**kw).split("\n"))
