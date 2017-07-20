#!/usr/bin/python3
# coding: utf-8

""" Import standart python modules """
import sys
import os
import copy

""" Import other python modules """
import requests
import http.cookiejar

""" Import my  python modules """

#TODO 
""" Список задач:
    - унифицировать внутренние каманды и параметры

"""

""" Coding """
def __init__():
    pass

class NetObj(object):

    def __init__(self):
        self.session = requests.session()

class TransliteObj(object):

    def __init__(self):
        self.translite = dict()


class CmdObj(object):

    def __init__(self):
        pass
    """ Блок проверки не нужен.
           Считаем анализ в момент загрузки инструкций и комманд.

           if not order_group in self.dict_obj.keys():
               return result = 'Словарь отсутствует'
               # Добавить  модуль  унифицированный перевод
           if not order in self.dict_obj[order_group].keys():
               return result = 'Распоряжение отсутствует'
    """

    def order(self, order, order_group):
        # TODO найти решение простой копии словаря
        #d = self.dict_obj[order_group][order].copy()
        cmd_dict = copy.deepcopy(self.dict_obj[order_group][order])
        #print(cmd_dict.items())
        for cmd in cmd_dict.keys():
            result = self.command(cmd, cmd_dict[cmd])
        return 'Распоряжение выполнено'

    """ Блок проверки не нужен.
        Считаем анализ в момент загрузки инструкций и комманд.

        if not cmd in .keys():
            result = 'Команда не найдена.'
            print result
            return result
    """

    def command(self, cmd, cmd_dict):
        for i in cmd_dict.keys():
            if i != '_prm':
                #sub_dict = copy.deepcopy(self.command(i,cmd_dict[i]))
                #print (cmd_dict.items())
                result = self.command(i, cmd_dict[i])
        #modul = (self.dict_obj['_modules'])[(self.dict_obj['_commands'])[cmd]]
        #result = getattr(modul, cmd)(self,  cmd_dict['_prm'])
        result = self.operation(cmd, cmd_dict['_prm'])
        #print ('Команда выполнена.')
        return result

    def operation(self, opr, prm):
        m = self.dict_obj['_commands'][opr]
        modul = self.dict_modules[m]
        result = getattr(modul, opr)(self, prm)
        return result


class PreviewObj(object):

    def __init__(self,name):
        pass

    def chrUpdate(self, new):
        pass


class Obj(CmdObj):

    def __init__(self,name):
        self.session = requests.session()
        self.name = name
        self.dict_obj = {
                         '_heroes': dict(),
                         '_characters': dict(),
                         '_mentors': dict(),
                         '_journal': dict(),
                         '_protokols': dict(),
                        }
        #Словарь импортированых  модулей.
        self.dict_modules = dict()
        #Импорт менеджера управления модулями.
        import importlib
        module = importlib.import_module('manager_modules')
        (self.dict_modules).update({'manager_modules': module})
        mngr_modules = self.dict_modules['manager_modules']
        mngr_modules.init(self, {})
        #-----------------------------------
        self.global_headers  = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'ru-RU',
            'Host': 'godville.net',
            'Connection': 'Keep-Alive',
            'Accept': 'text/html, application/xhtml+xml, */*',
            'Referer': 'https://godville.net/',
            'Content-Type': 'application/x-www-form-urlencoded',
            }
        self.data_headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'ru-RU',
            'Host': 'godville.net',
            'Connection': 'Keep-Alive',
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'X-Requested-With': 'XMLHttpRequest',
            'Referer': 'https://godville.net/superhero',
            }
        self.cookie = http.cookiejar.CookieJar()
        self.session.cookies = self.cookie
        self.ws = False
