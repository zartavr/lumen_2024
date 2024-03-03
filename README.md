# lumen_2024

## Запуск скриптов

Понадобится активировать виртуальное окружение.

Должна быть установлена [miniconda](https://docs.anaconda.com/free/miniconda/)

Перед первым запуском скрипта потребуется создать окружение из файла `conda.yaml`

```
conda env create -f conda.yml
```

Затем активировать окружение
```
conda activate tension-control
```

Если conda.yaml обновился потребуется выполнить следующую команду, чтобы обновить окружение:
```
conda env update --file conda.yaml --prune
```