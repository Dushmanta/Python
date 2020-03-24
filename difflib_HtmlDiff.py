import difflib


def preprocess(text):
    text = text.strip()
    text = text.split('\n')
    return text


def main():
    before_path = 'excel_data.txt'
    after_path = 'dest_excel.txt'

    before = open(before_path, 'r').read()
    before = preprocess(before)
    after = open(after_path, 'r').read()
    after = preprocess(after)

    diff = difflib.HtmlDiff()
    html = diff.make_file(before, after, 'Before', 'After')

    output = open('output.html', 'w')
    output.write(html)
    output.close()


if __name__ == '__main__':
    main()
