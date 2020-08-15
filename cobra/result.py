# -*- coding: utf-8 -*-

"""
    result
    ~~~~~~

    Implements result structure

    :author:    Feei <feei@feei.cn>
    :homepage:  https://github.com/wufeifei/cobra
    :license:   MIT, see LICENSE for more details.
    :copyright: Copyright (c) 2017 Feei. All rights reserved
"""


class VulnerabilityResult:
    def __init__(self):
        self.id = ''
        self.file_path = None
        self.analysis = ''
        self.chain = ""

        self.rule_name = ''
        self.language = ''
        self.line_number = None
        self.code_content = None
        self.commit_author = 'Unknown'

    def convert_to_dict(self):
        _dict = {}
        _dict.update(self.__dict__)
        return _dict
