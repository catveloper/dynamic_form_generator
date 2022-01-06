from abc import abstractmethod, ABCMeta


class SchemaConvertor(metaclass=ABCMeta):

    @abstractmethod
    def convert(self, schema: dict, ui_type, name=None):
        pass


class UiSchemaConvertor(SchemaConvertor):

    def convert(self, schema: dict, name="", prefix=""):
        prefix_name = "-".join([prefix, name]) if prefix and name else name
        schema_keys = schema.keys()
        schema_type = schema.get('type')

        # object
        schema['title'] = schema.get('title', name)
        schema['description'] = schema.get('description', '')
        if schema_type == 'object' and 'properties' in schema_keys:
            schema['title'] = schema.get('title', name)
            for p_name, p_schema in schema['properties'].items():
                schema['properties'][p_name] = self.convert(p_schema, p_name, prefix_name)

        # nested objects
        elif schema_type == 'array' and 'items' in schema_keys and schema['items'].get('type') == 'object':
            schema['items'] = self.convert(schema['items'], name, prefix)

        else:
            # TODO: 모델 베이스로 생성 가능한 스키마의 종류를 정리 후에 적용
            schema['name'] = prefix_name
            schema['x-widget'] = self._get_widget(schema, name)

        return schema

    def _get_widget(self, schema, name):
        from apps.form_schema_generator.enums import Widget
        schema_keys = schema.keys()
        schema_type = schema.get('type')

        # text(base)
        widget = Widget.TEXT_INPUT

        # id
        if name == 'id':
            widget = Widget.HIDDEN
        # number
        elif schema_type == 'number':
            widget = Widget.NUMBER
        # integer
        elif schema_type == 'integer':
            widget = Widget.INTEGER
        # single-choice
        elif schema_type == 'string' and 'oneOf' in schema_keys:
            widget = Widget.SELECT
        # multiple choice
        elif schema_type == 'array' and 'items' in schema_keys and 'oneOf' in schema['items'].keys():
            widget = Widget.CHECKBOX
        # long_text
        elif schema_type == 'string' and schema.get('maxLength', 300) >= 300:
            widget = Widget.TEXTAREA
        # json_text
        elif schema_type == 'object' and 'additionalProperties' in schema_keys:
            widget = Widget.TEXTAREA

        return widget.name


class FormConvertMixin:
    def __new__(cls, *args, **kwargs):
        new_class = super().__new__(cls, *args, **kwargs)

        not_implement_errors = []

        from apps.form_schema_generator.enums import Widget
        for w in Widget:
            widget_name = w.name.lower()
            method_name = f"get_{widget_name}_schema"
            if not getattr(new_class, method_name, False):
                error = f'"def {method_name}(self, schema)" method must be defined!'
                not_implement_errors.append(error)

        if len(not_implement_errors) > 0:
            error_msg = f'{cls.__name__} Class\n'
            error_msg += '\n'.join(not_implement_errors)
            raise NotImplementedError(error_msg)
        return new_class

    def _get_form_schema(self, schema, widget):
        method_name = f"get_{widget.lower()}_schema"
        return getattr(self, method_name)(schema)
