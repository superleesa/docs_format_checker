# note: font-color should never be listed here since highlighting it will cause the original colors to be gone
# (it's obvious anyways)
# format -> reference-name: display-name
valid_filters = {"char-width": "全角・半角",
                 "font-name": "フォント名",
                 "font-bold": "太字",
                 "font-italic": "イタリック",
                 "font-underline": "下線"}



boolean_properties = ["font-bold", "font-italic", "font-underline"]



def convert_float_value_to_string(float_value: float) -> str:
    """float-point valus cannot handle precise calculations so convert to str first"""

    str_float_value = str(float_value)
    length = len(str_float_value)
    index_of_point = None

    for i in range(length):
        if str_float_value[i] == ".":
            index_of_point = i
            break

    before_point = str_float_value[:index_of_point]
    after_point = str_float_value[index_of_point + 1:]

    return before_point + "-" + after_point