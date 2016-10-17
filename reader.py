import os
import re


def strip_source_code_from_with_md(text):
    return re.sub('```.*?```', '', text, flags=re.DOTALL)


def read_file_with_source_code(filename, ext_set=None):
    """Read the file and return the original text and non source code text

        Args:
            filename: full filename
            ext_set: available extensions
            
        Returns:
            Tuple of original text and text without source code
    """
    # Strip function dictionary for specific extension
    source_code_stripper = {
        '.md': strip_source_code_from_with_md,
    }

    if ext_set is not None and not filename.lower().endswith(ext_set):
        return '', ''

    try:
        with open(filename, 'r') as trans_file:
            text_content = trans_file.read()

            if type(text_content) == bytes:
                text_content = text_content.decode('utf8')

            ext = os.path.splitext(filename)[1]

            # Except source code
            if ext in source_code_stripper:
                text_non_source_code = source_code_stripper[ext](text_content)
            else:
                text_non_source_code = ''

            return text_content, text_non_source_code
    except:
        return '', ''
