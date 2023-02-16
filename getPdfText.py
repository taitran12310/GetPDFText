# from core import fulltext
from optparse import OptionParser
import fulltext
import pdftotext
import traceback

def getParser(defaults):
    """Create and return an OptionParser instance, with supplied defaults
    """
    op = OptionParser()
    op.add_option("-m",
                  dest="method",
                  help="method",
                  default=defaults['method'])
    op.add_option("-f",
                  dest="file_path",
                  help="File path",
                  default=defaults['file_path'])
    op.add_option("-p",
                  dest="password",
                  help="File password",
                  default=defaults['password'])
    return op

def getText1(file_path):
    encs = [ "utf-8", "shift_jis", "UTF-16LE"]
    content = None
    for i, encode in enumerate(encs):
        try:
            content = fulltext.get(file_path, enc=encode)
            return content
        except UnicodeDecodeError as err:
            if i >= len(encs) - 1:
                print('%s' % (file_path), 'UnicodeDecodeError', encode, err)
                print(traceback.format_exc())
    return None

def getText2(file_path, password):
    with open(file_path, "rb") as f:
        if password is None:
            pdf = pdftotext.PDF(f)
        else:
            pdf = pdftotext.PDF(f, password)
    return "".join(pdf)


def main():
    defaults = {
        'method': 'getText1',
        'file_path': './pdf/1.pdf',
        'password': None
    }

    # Initially parse arguments
    opts, args = getParser(defaults).parse_args()
    
    if(opts.method == 'getText1'):
        text = getText1(opts.file_path)
    else:
        text = getText2(opts.file_path, opts.password)
    print(text)

if __name__ == '__main__':
    main()