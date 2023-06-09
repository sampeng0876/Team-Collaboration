import tabula
# Read pdf into a list of DataFrame
dfs = tabula.read_pdf("test.pdf", pages='all')