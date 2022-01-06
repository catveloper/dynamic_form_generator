import copy

from apps.form_schema_generator.convertors.base import FormConvertMixin, SchemaConvertor


class VueJSFConvertor(FormConvertMixin, SchemaConvertor):

    def convert(self, schema: dict, name="", prefix=""):
        prefix_name = "-".join([prefix, name]) if prefix and name else name
        schema_keys = schema.keys()
        schema_type = schema.get('type')

        # object
        if schema_type == 'object' and 'properties' in schema_keys:
            for p_name, p_schema in schema['properties'].items():
                schema['properties'][p_name] = self.convert(p_schema, p_name, prefix_name)

        # nested objects
        elif schema_type == 'array' and 'items' in schema_keys and schema['items'].get('type') == 'object':
            schema['items'] = self.convert(schema['items'], name, prefix)

        else:
            return self._get_form_schema(schema, schema.get('x-widget'))

        return schema

    def get_text_input_schema(self, schema):
        form_schema = copy.deepcopy(schema)
        form_schema.update(
            {
                "type": "string",
            }
        )
        return form_schema

    def get_number_schema(self, schema):
        form_schema = copy.deepcopy(schema)
        form_schema.update(
            {
                "type": "number",
            }
        )
        return form_schema

    def get_integer_schema(self, schema):
        form_schema = copy.deepcopy(schema)
        form_schema.update(
            {
                "type": "integer",
            }
        )
        return form_schema

    def get_date_schema(self, schema):
        form_schema = copy.deepcopy(schema)
        form_schema.update(
            {
                "type": "string",
                "format": "date",
            }
        )
        return form_schema

    def get_checkbox_schema(self, schema):
        form_schema = copy.deepcopy(schema)
        form_schema.update(
            {
                "type": "string",
                "x-display": "checkbox",
            }
        )
        return form_schema

    def get_select_schema(self, schema):
        form_schema = copy.deepcopy(schema)
        form_schema.update(
            {
                "type": "string",
                "x-display": "combobox",
            }
        )
        return form_schema

    def get_textarea_schema(self, schema):
        form_schema = copy.deepcopy(schema)
        form_schema.update(
            {
                "type": "string",
                "x-display": "textarea",
            }
        )
        return form_schema

    def get_json_schema(self, schema):
        form_schema = copy.deepcopy(schema)
        form_schema.update(
            {
                "type": "string",
                "x-display": "textarea",
            }
        )
        return form_schema

    def get_hidden_schema(self, schema):
        form_schema = copy.deepcopy(schema)
        form_schema.update(
            {
                "readOnly": True,
                "x-display": 'hidden'
            }
        )
        return form_schema

    # 최악의 case
    # def get_text_input

        # if widget == Widget.TEXT_INPUT:
        #
        # elif widget == Widget.NUMBER:
        #
        # elif widget == Widget.URI:
        #
        # elif widget == Widget.DATE:
        #
        # elif widget == Widget.CHECKBOX:
        #
        # elif widget == Widget.SELECT:
        #
        # elif widget == Widget.TEXTAREA:
        #
        # elif widget == Widget.JSON:
        #
        # elif widget == Widget.HIDDEN: