
RESOURCE_METHODS = ['GET', 'POST', 'DELETE']
ITEM_METHODS = ['GET', 'PATCH', 'PUT', 'DELETE']

MONGO_HOST = 'ds013340.mlab.com'
MONGO_PORT = 13340
MONGO_USERNAME = 'testuser'
MONGO_PASSWORD = 'testpass'
MONGO_DBNAME = 'xeem-data'

XML = False

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
    },
    'questions': {
        'type': 'list',
        'schema': {
            'type': "dict",
            'schema': {
                'text': {
                    'type': 'string',
                    'minlength': 1,
                    'maxlength': 150,
                    'required': True
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
                                'minlength': 1,
                                'required': True,
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

result_schema = {
	'testid': {
		'type': 'string',
		'required': True,
	},
	'testetag': {
		'type': 'string'
	},
	'userid': {
		'type': 'string',
		'required': True
	},
	'regdate': {
		'type': 'integer'
	},
}

user_schema = {
	'userid': {
		'type': 'string',
		'required': True,
	},
	'username': {
		'type': 'string',
		'minlength': 1
	},
	'userpic': {
		'type': 'string'
	},	
	'regdate': {
		'type': 'integer'
	},
}

DOMAIN = {
    'blanks': {
        'schema': blank_schema
    },
    'users': {
    	'schema': user_schema
    },
    'results': {
    	'schema': result_schema
    }
}