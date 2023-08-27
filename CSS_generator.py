# from word_analyzer import convert_float_value_to_string
# # classes format: {"filter-name":["type-name", "type-name2", "type-name3"] }
#
# # remember the naming:
# # filter
# # type
#
#
# default_css_settings = {"starting_characters": {" ": "space", "\t": "tab"},
#                         "font_color": "black",
#                         "font_size": 20,
#                         "font_family": "Arial"
#                         }
#
# class CSSGenerator:
#     def __init__(self, colors, filters):
#         self.filters = filters
#         self.colors = colors
#
#     def get_marking_css(self):
#         marking_stylesheet = ""
#         for filter_x in self.filters:
#             for color_index, type_x in enumerate(filter_x):
#                 color = self.colors[color_index]
#                 marking_stylesheet += f".{filter}-{type_x}.selected" + "{"
#                 marking_stylesheet += f"background:linear-gradient(transparent 60%, {color} 60%);" + "}"
#
#         return marking_stylesheet
#
#     def get_default_css(self):
#         default_stylesheet = ""
#
#         # default styles here
#         default_stylesheet += f"#main-text{{color:{default_css_settings['font_color']};" \
#                       f"font-size:{default_css_settings['font_size']}pt;" \
#                       f"font-family:{default_css_settings['font_family']};}}"
#
#         if "first-line-indent" in self.filters:
#             indent_sizes = self.filters["first-line-indent"]
#
#             for indent_size in indent_sizes:
#                 if isinstance(indent_size, float):
#                     indent_size_name = self._convert_float_value_to_string(indent_size)
#                 else:
#                     indent_size_name = indent_size
#
#                 default_stylesheet += f".first-line-indent-{indent_size_name}{{text-indent:{indent_size}pt;}}"
#
#         elif "left-indent" in self.filters:
#             left_indent_sizes = self.filters["left-indent"]
#
#             for left_indent_size in left_indent_sizes:
#                 if isinstance(left_indent_size, float):
#                     left_indent_size_name = self._convert_float_value_to_string(left_indent_size)
#                 else:
#                     left_indent_size_name = left_indent_size
#
#                 default_stylesheet += f".left-indent-{left_indent_size_name}{{margin-left:{left_indent_size}pt;}}"
#
#         elif "font-name" in self.filters:
#             font_names = self.filters["font-name"]
#
#             for font_name in font_names:
#                 font_name_in_css = self._convert_font_name_for_css(font_name)  # TODO implement this function
#                 # Note: if corresponding font is not found in CSS, there will be no font setting for this class
#                 # and the font will be inherited from the paragraph
#                 if font_name_in_css is not None:
#                     default_stylesheet += f".font_name-{font_name}{{font_name:{font_name_in_css}}}"
#
#         elif "font-size" in self.filters:
#             font_sizes = self.filters["font-size"]
#
#             for font_size in font_sizes:
#                 if isinstance(font_size, float):
#                     font_size_name = convert_float_value_to_string(font_size)
#                 else:
#                     font_size_name = font_size
#
#                 default_stylesheet += f".font-size-{font_size_name}{{font-size:{font_size}pt;}}"
#
#         elif "font-underline" in self.filters:
#             default_stylesheet += ".font-underline{text-decoration: underline;}"
#
#         elif "font-bold" in self.filters:
#             print("comes here")
#             default_stylesheet += ".font-bold{font-weight: bold;}"
#
#         elif "font-color" in self.filters:
#             font_colors = self.filters["font-color"]
#
#             for font_color in font_colors:
#                 default_stylesheet += f".font-color-{font_color}{{font-color:#{font_color};}}"
#
#         elif "highlight-color" in self.filters:
#             # TODO implement later on
#             pass
#
#         elif "font-italic" in self.filters:
#             default_stylesheet += ".font-italic{font-style: italic;}"
#
#         else:
#             raise (ValueError("unknown class"))  # TODO another function must catch this error (perhaps console.log)
#
#         return default_stylesheet