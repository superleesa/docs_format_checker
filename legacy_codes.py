# def create_span_tag(current_character_props: dict) -> str:
#     html = "<span"
#
#     found_at_least_one_class = False
#     for prop_name, prop_value in current_character_props.items():
#         if prop_value:
#             if not found_at_least_one_class:
#                 html += " class=\""
#                 found_at_least_one_class = True
#
#             if prop_name in boolean_properties:
#                 html += f"{prop_name} "
#
#             else:
#                 html += f"{prop_name}-{prop_value} "
#
#     if found_at_least_one_class:
#         html = html[0:len(html) - 1]  # to remove extra space at the end
#         html += "\""
#
#     html += ">"
#
#     return html

# def add_class_to_dictionary(prop_name, prop_value, dictionary):
#     """mutates the dictionary inside"""
#     if prop_name in boolean_properties:
#         if prop_name not in dictionary:
#             dictionary[prop_name] = True
#     else:
#         if prop_name in dictionary:
#             dictionary[prop_name].append(prop_value)
#         else:
#             dictionary[prop_name] = [prop_value]


# html += "<p class=\"document-paragraph "
# found_at_least_one_class = False
# for prop_name, prop_value in paragraph_props.items():
#     if prop_value:
#         # classes shouldn't contain dots (".") because it is used to refer to a particular class in CSS
#         if isinstance(prop_value, float):
#             prop_value = convert_float_value_to_string(prop_value)
#
#         html += f"{prop_name}-{prop_value} "
#         # add_class_to_dictionary(prop_name, prop_value, html_classes)
#

#
# html = html[0:len(html) - 1]
# html += "\""
# html += ">"

# new_span_tag, new_classes = create_a_span_tag_with_innertext_and_update_required_classes(char, current_character_props)
                    # html += new_span_tag
                    #
                    # # inserting new classes into the existing ones
                    # for prop_name, prop_value in new_classes.items():
                    #     add_class_to_dictionary(prop_name, prop_value, html_classes)

# def create_a_span_tag_with_innertext_and_update_required_classes(character, current_character_props, required_classes):
#
#
#     html = "<span"
#
#     found_at_least_one_class = False
#     for prop_name, prop_value in current_character_props.items():
#         if prop_value:
#             if not found_at_least_one_class:
#                 html += " class=\""
#                 found_at_least_one_class = True
#
#             if prop_name in boolean_properties:
#                 html += f"{prop_name} "
#                 required_classes[prop_name] = True
#             else:
#                 html += f"{prop_name}-{prop_value} "
#                 if prop_name in required_classes:
#                     required_classes[prop_name].append(prop_value)
#                 else:
#                     required_classes[prop_name] = [prop_value]
#
#     if found_at_least_one_class:
#         html = html[0:len(html) - 1]  # to remove extra space at the end
#         html += "\""
#     html += f">{character}"
#
#     return html



########## FROM PDF version
# pages = get_pages_from_pdf(file_path)
    #
    # mapper_index_to_font, mapper_index_to_character, fonts_used = extract_characters_and_fonts(pages)
    # content = create_html_for_font_classification(mapper_index_to_font, mapper_index_to_character)
    # colors = generate_color(len(fonts_used))
    # style = generate_css_for_coloring(fonts_used, colors)
    #
    # return render_template("analyze2.html", content=Markup(content), style=Markup(style),
    #                        filename=Markup.escape(filename), fonts_used=fonts_used, colors=colors)


# def get_default_style_for_the_content(self):
#     """
#     :param html_classes: {"class_name": [class_val1, class_val2, ...], "class_name2": [class_val1, ....]}
#     :return:
#     """
#     css_styles = ""
#     html_classes = self.html_classes
#
#     # default styles here
#     css_styles += f"#main-text{{color:{default_css_settings['font_color']};" \
#                   f"font-size:{default_css_settings['font_size']}pt;" \
#                   f"font-family:{default_css_settings['font_family']};}}"
#
#     if "first-line-indent" in html_classes:
#         indent_sizes = html_classes["first-line-indent"]
#
#         for indent_size in indent_sizes:
#             if isinstance(indent_size, float):
#                 indent_size_name = self._convert_float_value_to_string(indent_size)
#             else:
#                 indent_size_name = indent_size
#
#             css_styles += f".first-line-indent-{indent_size_name}{{text-indent:{indent_size}pt;}}"
#
#     elif "left-indent" in html_classes:
#         left_indent_sizes = html_classes["left-indent"]
#
#         for left_indent_size in left_indent_sizes:
#             if isinstance(left_indent_size, float):
#                 left_indent_size_name = self._convert_float_value_to_string(left_indent_size)
#             else:
#                 left_indent_size_name = left_indent_size
#
#             css_styles += f".left-indent-{left_indent_size_name}{{margin-left:{left_indent_size}pt;}}"
#
#     elif "font-name" in html_classes:
#         font_names = html_classes["font-name"]
#
#         for font_name in font_names:
#             font_name_in_css = self._convert_font_name_for_css(font_name)  # TODO implement this function
#             # Note: if corresponding font is not found in CSS, there will be no font setting for this class
#             # and the font will be inherited from the paragraph
#             if font_name_in_css is not None:
#                 css_styles += f".font_name-{font_name}{{font_name:{font_name_in_css}}}"
#
#     elif "font-size" in html_classes:
#         font_sizes = html_classes["font-size"]
#
#         for font_size in font_sizes:
#             if isinstance(font_size, float):
#                 font_size_name = self._convert_float_value_to_string(font_size)
#             else:
#                 font_size_name = font_size
#
#             css_styles += f".font-size-{font_size_name}{{font-size:{font_size}pt;}}"
#
#     elif "font-underline" in html_classes:
#         css_styles += ".font-underline{text-decoration: underline;}"
#
#     elif "font-bold" in html_classes:
#         print("comes here")
#         css_styles += ".font-bold{font-weight: bold;}"
#
#     elif "font-color" in html_classes:
#         font_colors = html_classes["font-color"]
#
#         for font_color in font_colors:
#             css_styles += f".font-color-{font_color}{{font-color:#{font_color};}}"
#
#     elif "highlight-color" in html_classes:
#         # TODO implement later on
#         pass
#
#     elif "font-italic" in html_classes:
#         css_styles += ".font-italic{font-style: italic;}"
#
#     else:
#         raise (ValueError("unknown class"))  # TODO another function must catch this error (perhaps console.log)
#
#     return css_styles

# def create_html(self):
#     """returns html with tailwind like class names
#
#         while paring the document, it escapes html syntax related characters if there is any
#
#     """
#     paragraphs = self.paragraphs
#     html = ""
#
#     for paragraph in paragraphs:
#         # check for paragraph indentation
#         if paragraph.text == "":
#             html += "<br>"
#             continue
#
#         paragraph_props = {"first-line-indent": self._get_first_line_indent(paragraph),
#                            "left-indent": self._get_left_indent(paragraph),
#                            "starting-characters": self._get_starting_characters(paragraph)}
#
#         length_of_starting_characters = len(
#             paragraph_props["starting-characters"])  # for inserting html non-breakble spaces later on
#
#         # creating <p> tag for each paragraph
#         html += self._create_given_tag_with_classes(paragraph_props, "p")
#         self._add_classes_to_dictionary(paragraph_props, self.html_classes)  # mutates html_class
#
#         # creating <span> tag for each class found in texts within this paragraph
#         is_starting_run = True
#         previous_character_props = {}
#         current_character_props = {}
#         for run in paragraph.runs:
#             font = run.font
#
#             # important property of this run
#             current_character_props["font-name"] = self._get_font_name_without_space(font)
#             current_character_props["font-size"] = self._get_font_size(font)
#
#             # other properties of this run
#             current_character_props["font-underline"] = font.underline
#             current_character_props["font-bold"] = font.bold
#             current_character_props["font-color"] = self._get_font_color(font)
#             current_character_props["highlight-color"] = self._get_font_highlight_color(font)
#             current_character_props["font-italic"] = font.italic
#
#             for i in range(len(run.text)):
#                 char = run.text[i]
#                 char_type = unicodedata.east_asian_width(char)
#                 current_character_props["char-width"] = char_type
#                 char = str(Markup.escape(char))
#
#                 # html doesn't recognize the normal space (if there are more than 1) and tab characters
#                 # so we need to use non-breakable space
#                 if i < length_of_starting_characters:
#                     if char == " ":
#                         char = "&nbsp;"
#                     elif char == "\t":
#                         char = "&nbsp;&nbsp;&nbsp;&nbsp;"
#
#                 if is_starting_run or current_character_props != previous_character_props:
#                     if current_character_props != previous_character_props:
#                         # current values for properties different from the previous ones
#                         # -> need to close the previous span and start a new span
#                         html += "</span>"
#
#                     # the first span in a paragraph
#                     html += self._create_given_tag_with_classes(current_character_props, "span")
#                     html += char
#                     self._add_classes_to_dictionary(current_character_props,
#                                                     self.html_classes)  # mutates html_classes inside
#
#                     # .copy() to ensure that the previous_character_props is not changed when current_character_props is changed
#                     previous_character_props = current_character_props.copy()
#                     is_starting_run = False
#
#                 else:
#                     # current_character_props == previous_character_props:
#                     html += char
#
#         html += "</span></p>"  # don't need to add <br> because new paragraph makes texts automatically to be on next line
#
#     return html
#
#
# def _add_classes_to_dictionary(self, to_add_properties: dict, html_classes: dict) -> None:
#     """
#     mutates html_classes
#
#     note: we use dict (hash table) to store the property values for each property because we want a quick check on
#      property existence (array will make this process slower)
#
#     # TODO implement own hash table without data attribute (we only need key)
#
#     :param char:
#     :param properties:
#     :param html_classes:
#     :return:
#     """
#     for prop_name, prop_value in to_add_properties.items():
#         if prop_value is None:
#             continue
#         if prop_name in boolean_properties:
#             if prop_name not in html_classes:
#                 html_classes[prop_name] = True
#         else:
#             # considers two things
#             # 1) whether property name exists already
#             # 2) if so, whether property value (for the property) exists already or not
#             if prop_name in html_classes:
#                 html_classes[prop_name][prop_value] = None
#             else:
#                 html_classes[prop_name] = {prop_value: None}
#
#
# def _create_given_tag_with_classes(self, properties: dict, tag_name: str) -> str:
#     """
#     A tag for given tag name that has class properties identified by the given properties will be returned.
#
#     Main operations are:
#     1) for each property key:value, a corresponding html class key-value is created
#     2) they are inserted in the class property of the given tag
#
#     :param properties: properties that will be converted into classes; it is a dictionary
#     :param tag_name:
#     :return:
#     """
#     whole_tag = f"<{tag_name}"
#
#     found_at_least_one_class = False
#     for prop_name, prop_value in properties.items():
#         if prop_value:
#             if not found_at_least_one_class:
#                 whole_tag += " class=\""
#                 found_at_least_one_class = True
#
#             if prop_name in boolean_properties:
#                 prop_value = prop_name
#
#             if isinstance(prop_value, float):
#                 prop_value = convert_float_value_to_string(prop_value)
#
#             whole_tag += f"{prop_name}-{prop_value} "
#
#     if found_at_least_one_class:
#         whole_tag = whole_tag[0:len(whole_tag) - 1]  # to remove extra space at the end
#         whole_tag += "\""
#
#     whole_tag += ">"
#
#     return whole_tag
#
#
# def _get_first_line_indent(self, paragraph):
#     """return the indent in pt if there is any; alse return "none" (a string)"""
#     res = paragraph.paragraph_format.first_line_indent
#
#     if res:
#         return res.pt
#
#
# def _get_left_indent(self, paragraph):
#     """returns indent in pt"""
#     res = paragraph.paragraph_format.left_indent
#
#     if res:
#         return res.pt
#
#
# def _get_starting_characters(self, paragraph):
#     possible_starting_characters = default_css_settings["starting_characters"]
#     no_more_starting_characters = False
#
#     starting_characters_found = ""
#
#     for run in paragraph.runs:
#         for char in run.text:
#             if char in possible_starting_characters:
#                 char_name = possible_starting_characters[char]
#                 starting_characters_found += char_name
#             else:
#                 no_more_starting_characters = True
#                 break
#
#         if no_more_starting_characters:
#             break
#
#     return starting_characters_found
#
#
# def _get_font_underline(self, font):
#     res = font.underline
#
#     if res:
#         return True
#
#
# def _get_font_name_without_space(self, font):
#     res = font.name
#     if res:
#         return res.replace(" ", "")
#
#
# def _get_font_size(self, font):
#     res = font.size
#
#     if res:
#         return res.pt
#
#
# def _get_font_highlight_color(self, font):
#     res = font.highlight_color
#     if res:
#         return str(res.rgb)
#
#
# def _get_font_color(self, font):
#     """returns color in hex format"""
#     res = font.color.rgb
#
#     if res:
#         return str(res)

# def get_html_classes_for_each_filter(self):
#     """
#     the output is formatted as arrays in dictionary like this:
#     {"font-name": ["font-name-1", "font-name-2", "font-name-3"], "char-width": ["char-width-Na", "char-width-Half-F"]}
#     :return:
#     """
#     filters_and_class_names = {}
#     max_count = 0
#     for prop_name, prop_values in self.html_classes.items():
#         if prop_name in valid_filters and not isinstance(prop_values, bool):
#             is_first_prop_value = True
#             count = 0
#             for prop_value in prop_values:
#                 if isinstance(prop_value, float):
#                     prop_value = self._convert_float_value_to_string(prop_value)
#
#                 if is_first_prop_value:
#                     filters_and_class_names[prop_name] = [f"{prop_name}-{prop_value}"]
#                     is_first_prop_value = False
#                 else:
#                     filters_and_class_names[prop_name].append(f"{prop_name}-{prop_value}")
#
#                 count += 1
#
#             if count > max_count:
#                 max_count = count
#
#         elif prop_name in valid_filters and isinstance(prop_values, bool):
#             filters_and_class_names[prop_name] = [f"{prop_name}-{prop_values}"]
#
#             if max_count < 1:
#                 max_count = 1
#
#     self.max_number_of_class_names_per_filter = max_count
#     return filters_and_class_names