.. _ru_test:

Тестирование OutWiker
=====================


Для юнит-тестирования в OutWiker используется стандартный пакет unittest_. Тесты проверяют работу внутренних компонентов OutWiker, а также элементов графического интерфейса.

Все тесты располагаются в папке :file:`src/test`, а запускаемые их скрипты располагаются в папке :file:`src` и имеют имена, соответствующие маске: :file:`tests_*.py` (также см. раздел :ref:`ru_sources_struct_src`). Файлы, соответствующие маске :file:`tests_plugin_*.py` запускают тесты плагинов.

Для запуска тестов предназначена следующая команда fabfile (см. раздел :ref:`ru_fabfile`):

.. code:: bash

    fab test

С помощью дополнительных параметров команды `fab test` можно ограничить наборы тестов, которые должны быть запущены.

``fab test:core`` - запуск тестов для ядра движка OutWiker (см. раздел :ref:`ru_outwiker_core`).

``fab test:wiki`` - запуск тестов парсера викинотации (см. раздел :ref:`ru_outwiker_wiki_parser`).

``fab test:gui`` - запуск тестов графических элементов интерфейса (см. раздел :ref:`ru_outwiker_gui`).

``fab test:actions`` - запуск тестов actions (см. раздел :ref:`ru_outwiker_actions`).

``fab test:plugins`` - запуск тестов для всех плагинов (см. раздел :ref:`ru_outwiker_plugins`).

``fab test:plugins,имя_плагина`` - запуск тестов для указанного плагина.

Можно также передавать дополнительные параметры для движка запуска тестов. Например, если требуется прервать тестирование после первого провалившегося теста, то можно выполнить следующую команду:

.. code:: bash

    fab test:core,-f

В данный момент нельзя использовать дополнительные параметры без ограничения набора выполняемых тестов. Т.е. **следующая команда работать не будет**:


.. code:: bash

    fab test:-f

Можно запустить тесты выбранного набора тестов (test case) из набора тестов. Например, следующая команда запускает только тесты закладок из набора тестов `core`:

.. code:: bash

    fab test:BookmarksTest

Можно запустить конкретный тест. Например:

.. code:: bash

    fab test:BookmarksTest.testAddToBookmarks


.. note:: Изначально разделение тестов на несколько групп было сделано из-за того, что при выполнении тестов графического интерфейса наблюдается утечка ресурсов GDI (GDI handlers), и после запуска большого количества тестов под Windows количество выделенных GDI-ресурсов превышало 10 000, после чего возникали ошибки. Проблема утечек до сих пор наблюдается, но не влияет на тестирование. Данная утечка скорее всего связана со множественным созданием главного окна OutWiker и не проявляется в работе OutWiker.

.. _ru_test_dir:

Структура папки src/test
------------------------

Все тесты располагаются в папке :file:`src/test`. Имена файлов, содержащие тесты, соответствуют маске :file:`test_*.py`

Тесты для плагинов располагаются в папке :file:`src/test/plugins/`. Для каждого плагина создана отдельная папка внутри :file:`src/test/plugins/`. Например, тесты для плагина markdown_ располагаются в папке :file:`src/test/plugins/markdown`.


.. _unittest: https://docs.python.org/2/library/unittest.html
.. _markdown: http://jenyay.net/Outwiker/Markdown
