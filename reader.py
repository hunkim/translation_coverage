import os
import re


def strip_source_code_from_with_md(text):
    return re.sub('```.*?```', '', text, flags=re.DOTALL)


def get_source_code_stripper(ext):
    source_code_stripper = {
        '.md': strip_source_code_from_with_md,
        # Add stripper for other formats
    }

    if ext in source_code_stripper:
        return source_code_stripper[ext]

    # Return just original text
    return lambda text: text


def read_normal_text_from_file(filename, ext_set=None):
    """Read the file and return the normal text

        Args:
            filename: full filename
            ext_set: available extensions

        Returns:
            normal text without special string (e.g. except source code)
    """

    if ext_set is not None and not filename.lower().endswith(ext_set):
        return ''

    try:
        with open(filename, 'r') as trans_file:
            text_content = trans_file.read()

            if type(text_content) == bytes:
                text_content = text_content.decode('utf8')

            ext = os.path.splitext(filename)[1]

            source_code_stripper = get_source_code_stripper(ext)

            text_normal = source_code_stripper(text_content)

            return text_normal
    except:
        return ''
