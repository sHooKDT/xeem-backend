
RESOURCE_METHODS = ['GET', 'POST', 'DELETE']
ITEM_METHODS = ['GET', 'PATCH', 'PUT', 'DELETE']

MONGO_HOST = 'ds013340.mlab.com'
MONGO_PORT = 13340
MONGO_USERNAME = 'testuser'
MONGO_PASSWORD = 'testpass'
MONGO_DBNAME = 'xeem-data'

blank_schema = {
    'title': {
        'type': 'string',
        'minlength': 1,
        'maxlength': 50,
        'required': True,
    },
    'date': {
        'type': 'integer',
        'required': True,
    },
    'public': {
        'type': 'boolean',
    },
    'author': {
        'type': 'string',
        'minlength': 3,
        'maxlength': 15,
        'required': True,
    },
    'questions': {
        'type': 'list',
        'schema': {
            'type': "dict",
            'schema': {
                'text': {
                    'type': 'string',
                    'minlength': 5,
                    'maxlength': 150
                },
                'pic': {
                    'type': 'string'
                },
                'correct': {
                    'type': 'integer',
                    'min': 0
                },
                'points': {
                    'type': 'number'
                },
                'answers': {
                    'type': 'list',
                    'schema': {
                        'type': 'dict',
                        'schema': {
                            'text': {
                                'type': 'string',
                                'minlength': 5
                            },
                            'pic': {
                                'type': 'string'
                            },
                        },
                    },
                },
            },
        },
    },
}

DOMAIN = {
    'blanks': {
        'schema': blank_schema
    }
}