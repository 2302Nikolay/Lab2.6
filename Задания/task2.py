#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

if __name__ == '__main__':
    num = {'two': 2, 'three': 3, 'four': 4}
    print(num)

    dict_items = num.items()
    dict_inv = (lambda d: {v: k for k, v in d})
    print(dict_inv(dict_items))
