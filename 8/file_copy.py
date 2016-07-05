#!/usr/bin/env python3

'''
Хохлов Андрей

'''

import json
import os
import shutil
import concurrent.futures


def get_workers(file='settings.json'):
    with open(file) as f:
        from_settings = json.load(f)
    if from_settings['workers'] != 3:
        return from_settings['workers']
    else:
        return 3


def get_folders():
    while True:
        source_path = input('Введите путь к папке из которой нужно скопировать файлы: ')
        if not os.path.exists(source_path):
            continue
        destination_path = input('Введите путь к папке назначения: ')
        if not os.path.exists(destination_path):
            continue
        else:
            break
    return (source_path, destination_path)


def main():
    workers = get_workers()
    source_path, destination_path = get_folders()
    source_files = [f for f in os.listdir(source_path)
                        if os.path.isfile(os.path.join(source_path, f))]
    with concurrent.futures.ThreadPoolExecutor(workers) as executor:
        for file in source_files:
            src = os.path.join(source_path, file)
            dst = os.path.join(destination_path, file)
            executor.submit(shutil.copyfile, src, dst)


if __name__ == '__main__':
    main()
