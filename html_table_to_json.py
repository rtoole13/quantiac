def html_table_to_json(filepath, targetpath):
    with open(filepath,'r') as f:
        lines = [line.strip() for line in f]
        rows = ''.join(lines).split('<tr>')
        rows = [row for row in rows if row != '']
        
        entries = dict.fromkeys(range(len(rows)))
        
        for i in entries.keys():
            entries[i] = {}
            entries[i]['raw_string'] = rows[i]

            cols = entries[i]['raw_string'].split('<td')
            cols = [col.lstrip() for col in cols if col != '']
            cols = [col for col in cols if not col.startswith('style')]

            entries[i]['symbol'] = cols[0].replace('</td>', '').replace('>', '')
            entries[i]['name'] = cols[1].replace('</td>', '').replace('>', '')
            entries[i]['type'] = cols[2].replace('</td>', '').replace('>', '')
            
        #trim
        processed = entries.copy()
        for i in processed.keys():
            processed[i].pop('raw_string')
            
        #dump to json
        import json
        with open(targetpath, 'w') as f:
            json.dump(processed, f)

if __name__ == '__main__':
    import sys
    args = sys.argv
    if len(args) < 3:
        sys.exit('First argument is to be the html file to read from. Second arg is target json to write to.')

    html_table_to_json(args[1], args[2])
    