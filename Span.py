import utils as util

class FiltersAndTypes:
    def __init__(self):
        self.all_properties = {}

    def add_properties(self, properties):
        for prop_name, prop_value in properties.items():
            if prop_value is None:
                continue
            if prop_name in util.boolean_properties:
                if prop_name not in self.all_properties:
                    self.all_properties[prop_name] = True
            else:
                # considers two things
                # 1) whether property name exists already
                # 2) if so, whether property value (for the property) exists already or not
                if prop_name in self.all_properties and prop_value not in self.all_properties[prop_name]:
                    self.all_properties[prop_name].append(prop_value)
                else:
                    self.all_properties[prop_name] = [prop_value]

    def get_as_dict(self):
        return self.all_properties

class DataSpan:
    all_properties = FiltersAndTypes()

    def __init__(self):
        self.innertext = ""
        self.properties = {}

    def add_properties(self, properties):
        # process filters_and_types and append it to self.data
        self.properties.update(properties)
        DataSpan.all_properties.add_properties(properties)

    def add_text(self, text):
        self.innertext += text

    def get_properties(self):
        return self.properties

    def get_as_dict(self):
        # TODO this part inefficient
        span_data = {}
        span_data.update(self.properties)
        span_data["innertext"] = self.innertext
        return span_data



class DataParagraph:
    all_properties = FiltersAndTypes()
    def __init__(self):
        self.properties = {}
        self.spans = []

    def add_properties(self, properties):
        self.properties.update(properties)
        DataParagraph.all_properties.add_properties(properties)

    def add_span(self, span):
        self.spans.append(span)

    def add_break(self):
        self.spans.append("br")

    def __getitem__(self, index):
        return self.spans[index]

    def get_as_list(self):
        paragraph_data = [self.properties, []]
        for span in self.spans:
            paragraph_data[1].append(span.get_as_dict())

        return paragraph_data


class DataDocx:
    def __init__(self):
        self.paragraphs = []

    def add_paragraph(self, paragraph: DataParagraph):
        self.paragraphs.append(paragraph)

    def get_as_list(self) -> list:
        paragraphs = []
        for paragraph in self.paragraphs:
            paragraphs.append(paragraph.get_as_list())

        return paragraphs
