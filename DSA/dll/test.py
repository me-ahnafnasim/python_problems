"""doubly_linked_list = {
    "head": {
        "data": 10,
        "next": {
            "data": 20,
            "next": {
                "data": 30,
                "next": None,  # Indicates the end of the list
                "prev": {      # Points back to the previous node
                    "data": 20,
                    "next": {
                        "data": 30,
                        "next": None,
                        "prev": {
                            "data": 10,
                            "next": {
                                "data": 20,
                                "next": {
                                    "data": 30,
                                    "next": None,
                                    "prev": {
                                        "data": 20,
                                        "next": {
                                            "data": 30,
                                            "next": None,
                                            "prev": {
                                                "data": 10,
                                                "next": {
                                                    "data": 20,
                                                    "next": {
                                                        "data": 30,
                                                        "next": None,
                                                        "prev": None  # Start of the list
                                                    },
                                                    "prev": {
                                                        "data": 10,
                                                        "next": {
                                                            "data": 20,
                                                            "next": {
                                                                "data": 30,
                                                                "next": None,
                                                                "prev": None
                                                            },
                                                            "prev": None
                                                        },
                                                        "prev": None
                                                    }
                                                },
                                                "prev": None
                                            }
                                        },
                                        "prev": {
                                            "data": 10,
                                            "next": {
                                                "data": 20,
                                                "next": {
                                                    "data": 30,
                                                    "next": None,
                                                    "prev": None
                                                },
                                                "prev": None
                                            },
                                            "prev": None
                                        }
                                    },
                                    "prev": {
                                        "data": 20,
                                        "next": {
                                            "data": 30,
                                            "next": None,
                                            "prev": None
                                        },
                                        "prev": {
                                            "data": 10,
                                            "next": {
                                                "data": 20,
                                                "next": {
                                                    "data": 30,
                                                    "next": None,
                                                    "prev": None
                                                },
                                                "prev": None
                                            },
                                            "prev": None
                                        }
                                    }
                                },
                                "prev": {
                                    "data": 20,
                                    "next": {
                                        "data": 30,
                                        "next": None,
                                        "prev": None
                                    },
                                    "prev": {
                                        "data": 10,
                                        "next": {
                                            "data": 20,
                                            "next": {
                                                "data": 30,
                                                "next": None,
                                                "prev": None
                                            },
                                            "prev": None
                                        },
                                        "prev": None
                                    }
                                }
                            },
                            "prev": None
                        }
                    },
                    "prev": {
                        "data": 10,
                        "next": {
                            "data": 20,
                            "next": {
                                "data": 30,
                                "next": None,
                                "prev": None
                            },
                            "prev": None
                        },
                        "prev": None
                    }
                }
            },
            "prev": {
                "data": 10,
                "next": {
                    "data": 20,
                    "next": {
                        "data": 30,
                        "next": None,
                        "prev": None
                    },
                    "prev": None
                },
                "prev": None
            }
        },
        "prev": None  # Indicates the start of the list
    }
}"""





dll = {
    "head": {
        "data": 10,
        "next": {
            "data": 20,
            "next": {
                "data": 30,
                "next": None,  # End of the list
                "prev": {      # Points back to the previous node
                    "data": 20,
                    "next": {"data": 30},  # Circular reference here
                    "prev": {              # Points back to the head node
                        "data": 10,
                        "next": {"data": 20},
                        "prev": None       # Start of the list
                    }
                }
            },
            "prev": {          # Points back to the head node
                "data": 10,
                "next": {"data": 20},
                "prev": None   # Start of the list
            }
        },
        "prev": None  # Start of the list
    }
}


"""dll ={{'head': {'data': 10, 'next': {'data': 20, 'next': {'data': 30, 'next': None, 'prev': {'data': 20, 'next': {'data': 30},'prev': {'data': 10, 'next': {'data': 20}, 'prev': None}}}, 'prev': {'data': 10, 'next': {'data': 20}, 'prev': None}}, 'prev': None}}}



print(dll["head"])"""


dll = {
    'head': {
        'data': 10,
        'next': {
            'data': 20,
            'next': {
                'data': 30,
                'next': None,
                'prev': {
                    'data': 20,
                    'next': {'data': 30},
                    'prev': {
                        'data': 10,
                        'next': {'data': 20},
                        'prev': None
                    }
                }
            },
            'prev': {
                'data': 10,
                'next': {'data': 20},
                'prev': None
            }
        },
        'prev': None
    }
}

print(dll["tail"])