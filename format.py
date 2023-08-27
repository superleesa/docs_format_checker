import unicodedata
import re
import os
from pdfminer.high_level import extract_pages
from typing import Iterable
from random import randint

possible_starting_characters = {" ":"半角スペース", "\t": "インデント", "\u3000": "全角スペース"}

def split_text_into_paragraphs(text):
    # inclusive start and exlusive end
    paragraphs = [[0]]
    for idx in range(len(text)):
        if text[idx] == "\n":
            paragraphs[-1].append(idx)
            paragraphs.append([idx + 1])

    paragraphs[-1].append(len(text))
    return paragraphs


def detect_starting_characters_of_paragraph(text, start_idx, end_idx):
    """
    end_idx here is exclusive
    returns the index (inclusive) of the starting character of a paragraph

    """
    starting_characters = []

    idx = start_idx
    while text[idx] in possible_starting_characters and idx < end_idx:
        corresponding_char_name = possible_starting_characters[text[idx]]
        starting_characters.append(corresponding_char_name)
        idx += 1

    return starting_characters, idx


def detect_starting_characters(text):
    split_indices = split_text_into_paragraphs(text)
    res = []
    for start, end in split_indices:
        res.append(detect_starting_characters_of_paragraph(text, start, end))
        print(detect_starting_characters_of_paragraph(text, start, end))
    return res


def highlight_full_size(text):
    new_html = ""
    predecessor_full_size = False

    for char in text:
        decision = unicodedata.east_asian_width(char)
        if (decision == "Na" or decision == "H") and predecessor_full_size:
            new_html += char + "</mark>"
            predecessor_full_size = False

        elif (decision == "F" or decision == "W") and predecessor_full_size:
            new_html += char

        elif (decision == "Na" or decision == "H") and not predecessor_full_size:
            new_html += char

        elif (decision == "F" or decision == "W") and not predecessor_full_size:
            new_html += "<mark class=\"full_size_char\">" + char
            predecessor_full_size = True

        else:
            if predecessor_full_size:
                new_html += "</mark><mark class=\"wired_char\">" + char + "</mark>"
                predecessor_full_size = False
            else:
                new_html += "<mark class=\"wired_char\">" + char + "</mark>"

    return new_html


def create_html_for_font_classification(mapper_index_to_font, mapper_index_to_character):
    html = f"<mark class=\"{mapper_index_to_font[0]}\">{mapper_index_to_character[0]}"
    previous_font = mapper_index_to_font[0]

    i = 1
    while i < len(mapper_index_to_font):
        current_font, current_character = mapper_index_to_font[i], mapper_index_to_character[i]

        # newline -> <br>
        if current_character == "\n":
            html += f"</mark><br>"
            previous_font = None

            # need to process all the neighbor newline characters
            # note: if the newline symbol is found at the end of text, then we can stop already
            while i < len(mapper_index_to_font) - 1:
                i += 1
                if mapper_index_to_character[i] == "\n":
                    html += "<br>"
                else:
                    current_font, current_character = mapper_index_to_font[i], mapper_index_to_character[i]
                    html += f"<mark class=\"{current_font}\">{current_character}"
                    previous_font = current_font
                    i += 1
                    break

        elif current_font != previous_font:
            html += f"</mark><mark class=\"{current_font}\">{current_character}"
            previous_font = current_font

        elif current_font == previous_font:
            html += f"{current_character}"
            previous_font = current_font

        i += 1

    if not html.endswith("<br>"):
        html += "</mark>"

    return html


def extract_characters_and_fonts(pages):
    return extract_characters_and_fonts_aux(pages, 0, [], [], [])


def extract_characters_and_fonts_aux(current_object, current_index, mapper_index_to_font, mapper_index_to_character,
                                     fonts_used):
    # a recursive (backtracking) function

    if isinstance(current_object, Iterable):
        # haven't reached to a character yet
        for element in current_object:
            mapper_index_to_font, mapper_index_to_character, fonts_used = extract_characters_and_fonts_aux(element,
                                                                                                           current_index,
                                                                                                           mapper_index_to_font,
                                                                                                           mapper_index_to_character,
                                                                                                           fonts_used)

        return mapper_index_to_font, mapper_index_to_character, fonts_used

    elif hasattr(current_object, 'get_text'):
        # reaches a character
        if hasattr(current_object, 'fontname'):
            current_fontname = current_object.fontname

            # ignore the encoding method of fonts
            match = re.match("[A-Z]{6}\+", current_fontname)
            if match is not None:
                start = match.span()[1]
                current_fontname = current_fontname[start:len(current_fontname)]

            mapper_index_to_font.append(current_fontname)
            mapper_index_to_character.append(current_object.get_text())

            if current_fontname not in fonts_used:
                fonts_used.append(current_fontname)

        else:
            mapper_index_to_font.append("font_not_detected")
            mapper_index_to_character.append(current_object.get_text())

            if "font_not_detected" not in fonts_used:
                fonts_used.append("font_not_detected")

        current_index += 1

        return mapper_index_to_font, mapper_index_to_character, fonts_used
    else:
        return mapper_index_to_font, mapper_index_to_character, fonts_used

def get_pages_from_pdf(file_path):
    pages = extract_pages(file_path)
    return pages


def generate_color(length):
    possible_colors = ["#A4262C", "#407855", "#40587C", "#8764B8",
                       "#CA5010", "#038387", "#4052AB", "#737373",
                       "#8F7034", "#0078d4", "#854085", "#867365"]

    if length > 12:
        randomely_selected_colors = []
        hex_chars = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9",
                     "A", "B", "C", "D", "E", "F"]

        for _ in range(length - 12):
            color = "#"
            for _ in range(6):
                color += hex_chars[randint(0, 15)]
            randomely_selected_colors.append(color)

        return possible_colors + randomely_selected_colors

    else:
        return possible_colors[0: length]


def generate_css_for_coloring(fonts_used, colors):
    css = ""

    for font, color in zip(fonts_used, colors):
        css += f".{font}{{background: linear-gradient(transparent 5%, {color} 0%);}}"
    return css