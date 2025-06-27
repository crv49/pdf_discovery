import tabula
import pandas as pd

tables = tabula.read_pdf(
    'financial_only.pdf',
    pages='all',
    # multiple_tables=True,
    # lattice=False,      # For tables with borders
    # stream=False,       # For tables without borders
    # guess=True,
    # pandas_options={'header': None},
)

for i, table in enumerate(tables, 1):
    print(table)

#False, False, True