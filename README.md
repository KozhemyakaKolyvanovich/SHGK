markdown
## Разработка

### Установка зависимостей
    ```bash
    pip install -r requirements.txt
Запуск тестов
  bash
  pytest tests/ -v
Проверка стиля кода
  bash
  flake8 src/
Форматирование кода
  bash
  black src/
  text

```python
def card_value(card):
    Подчёт очков карт в руке

def calculate_score(hand):
     Суммируем очки, учитывая что туз = 11 или 1
     Если перебор и есть тузы, меняем их стоимость с 11 на 1

  
