import itertools

import unicodecsv as csv

from pycassa.pool import ConnectionPool
from pycassa.columnfamily import ColumnFamily


def columnfamily_dump(host, port, keyspace, columnfamily, columns, limit, outfile, header, delimiter):
    pool = ConnectionPool(keyspace, ['{}:{}'.format(host, port)], timeout=None)
    col_fam = ColumnFamily(pool, columnfamily)

    if columns:
        keys = set(columns.split(u','))
    else:
        rows = col_fam.get_range(row_count=limit)
        keys = set(key for key in itertools.chain.from_iterable(row[1].iterkeys() for row in rows))

    keys.add(u'{}_id'.format(columnfamily))

    writer = csv.DictWriter(outfile, keys, extrasaction=u'ignore', delimiter=delimiter)

    if header:
        writer.writeheader()

    rows = col_fam.get_range(columns=keys, row_count=limit)
    row_buffer_count = 0
    csv_rows = []
    for (id, data) in rows:
        d = {u'{}_id'.format(columnfamily): id}
        d.update(data)
        csv_rows.append(d)
        row_buffer_count += 1

        if row_buffer_count >= col_fam.buffer_size:
            writer.writerows(csv_rows)
            csv_rows = []
            row_buffer_count = 0
    else:
        writer.writerows(csv_rows)
