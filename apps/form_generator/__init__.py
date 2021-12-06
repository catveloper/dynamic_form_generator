var = {
    'type': 'object',
    'properties': {
        'name': {
            'type': 'string',
            'maxLength': 30
        },
        'annotations': {
            'type': 'array',
            'items': {
                'type': 'object',
                'properties': {
                    'data': {
                        'type': 'object',
                        'additionalProperties': {}
                    },
                    'task': {
                        'type': 'integer'
                    },
                    'user': {
                        'type': 'integer'
                    }
                },
                'required': ['task', 'user']
            }
        },
        'project': {
            'type': 'object',
            'properties': {
                'name': {
                    'type': 'string',
                    'maxLength': 30
                },
                'url': {
                    'type': 'string',
                    'format': 'uri',
                    'maxLength': 200
                }
            },
            'required': ['name', 'url']
        }
    },
    'required': ['annotations', 'name', 'project']
}

ui_schema = {
    'type': 'object',
    'properties': {
        'name': {
            'widget': 'INPUT',
            'name': 'name',
            'label': 'name',
            'value': None,
            'choices': [],
            'extra_options': {}
        },
        'annotations': {
            'type': 'array',
            'items': {
                'type': 'object',
                'properties': {
                    'data': {
                        'widget': 'INPUT',
                        'name': 'data',
                        'label': 'data',
                        'value': None,
                        'choices': [],
                        'extra_options': {}
                    },
                    'task': {
                        'widget': 'INPUT',
                        'name': 'task',
                        'label': 'task',
                        'value': None,
                        'choices': [],
                        'extra_options': {}
                    },
                    'user': {
                        'widget': 'INPUT',
                        'name': 'user',
                        'label': 'user',
                        'value': None,
                        'choices': [],
                        'extra_options': {}
                    }
                }
            }
        },
        'project': {
            'type': 'object',
            'properties': {
                'name': {
                    'widget': 'INPUT',
                    'name': 'name',
                    'label': 'name',
                    'value': None,
                    'choices': [],
                    'extra_options': {}
                },
                'url': {
                    'widget': 'INPUT',
                    'name': 'url',
                    'label': 'url',
                    'value': None,
                    'choices': [],
                    'extra_options': {}
                }
            }
        }
    }
}
