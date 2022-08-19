from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_rating()) == 2

# Проверка __init__ Проверяем каждое из полей books_rating и favorites что они не None
    def test_inits_elements_not_none(self):
        collector = BooksCollector()
        assert collector.books_rating != None, f"books_rating is None"
        assert collector.favorites != None, f"favorites is None"

# Проверка на повторное добавление имеющейся книги
    def test_add_new_book_possible_to_add_once(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Гордость и предубеждение и зомби')
        assert len(collector.get_books_rating()) == 1, f"The book has been re-added"

# Проверка добавления книги и значения рейтинга по умолчанию = 1
    def test_add_new_book_default_rating(self):
        collector = BooksCollector()
        collector.add_new_book('Идиот')

        assert len(collector.get_books_rating()) == 1, f"Add book test failed"
        assert collector.get_book_rating('Идиот') == 1, f"Default rating is not 1"

# Проверка что у не добавленной книги нет рейтинга
    def test_get_book_rating_get_rating_for_an_unlisted_book(self):
        collector = BooksCollector()
        assert collector.get_book_rating('Что делать?') == None, f"Received a rating for an unlisted book"

# Проверка на установку рейтинга для книги, которой нет в списке
    def test_set_book_rating_set_rating_for_an_unlisted_book(self):
        collector = BooksCollector()
        collector.set_book_rating('Сто лет одиночества', 5)
        assert collector.get_book_rating('Сто лет одиночества') == None, f"Received a rating for an unlisted book"

# Проверки установления значений рейтинга
    def test_set_book_rating_only_1_to_10(self):
        collector = BooksCollector()

        collector.add_new_book('Двенадцать стульев')
        collector.set_book_rating('Двенадцать стульев', 0)
        zero_value = collector.get_book_rating('Двенадцать стульев')
        assert zero_value == 1, f"set_book_rating with value 0 sets rating {zero_value}"

        collector.add_new_book('Золотой теленок')
        collector.set_book_rating('Золотой теленок', 11)
        eleven_value = collector.get_book_rating('Золотой теленок')
        assert eleven_value == 1, f"set_book_rating with value 11 sets rating {eleven_value}"

        collector.add_new_book('Одноэтажная Америка')
        collector.set_book_rating('Одноэтажная Америка', 10)
        ten_value = collector.get_book_rating('Одноэтажная Америка')
        assert ten_value == 10, f"set_book_rating with value 10 sets rating {ten_value}"

# Проверка для списка книг с одинаковым рейтингом
    def test_get_books_with_specific_rating_for_books_with_the_same_rating(self):
        collector = BooksCollector()

        collector.add_new_book('Братья Карамазовы')
        collector.set_book_rating('Братья Карамазовы', 5)

        collector.add_new_book('Остров сокровищ')
        collector.set_book_rating('Остров сокровищ', 9)

        collector.add_new_book('Война и Мир')
        collector.set_book_rating('Война и Мир', 10)

        collector.add_new_book('Сердца трех')
        collector.set_book_rating('Сердца трех', 9)
        assert len(collector.get_books_with_specific_rating(9)) == 2, f"The number of books with the same rating is incorrect"

# Проверка функции вывода текущего словаря
    def test_get_books_rating_for_four_books(self):
        collector = BooksCollector()
        collector.add_new_book('Вокруг света за 80 дней')
        collector.add_new_book('Затерянный мир')
        collector.add_new_book('Граф Монте-Кристо')
        collector.add_new_book('Приключения Тома Сойера')
        assert len(collector.get_books_rating()) == 4

# Проверка функции добавления книги в Избранное
# Невозможно дважды добавить одну книгу
    def test_add_book_in_favorites_cannot_be_added_twice(self):
        collector = BooksCollector()
        collector.add_new_book('Книга Джунглей')
        collector.add_new_book('Таинственный остров')
        collector.add_new_book('Робинзон Крузо')
        collector.add_book_in_favorites('Книга Джунглей')
        collector.add_book_in_favorites('Робинзон Крузо')
        collector.add_book_in_favorites('Книга Джунглей')
        assert len(collector.favorites) == 2, f"The book has been added to favorites twice"

# Проверка невозможности добавить в Избранное книги, отсутствующей в словаре
    def test_add_book_in_favorites_unable_to_add_missing_book(self):
        collector = BooksCollector()
        collector.add_new_book('Книга Джунглей')
        collector.add_book_in_favorites('Книга Джунглей')
        collector.add_book_in_favorites('Робинзон Крузо')
        assert len(collector.favorites) == 1, f"A book not on the books_rating has been added to favorites"

# Проверка удадения книги из избранного
    def test_delete_book_from_favorites_remove_one_book_from_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Книга Джунглей')
        collector.add_new_book('Робинзон Крузо')

        collector.add_book_in_favorites('Книга Джунглей')
        collector.add_book_in_favorites('Робинзон Крузо')
        collector.delete_book_from_favorites('Книга Джунглей')
        assert len(collector.favorites) == 1, f"Book not removed from favorites"

# Проверка функции получения списка избранного
    def test_get_list_of_favorites_books_get_two_books(self):
        collector = BooksCollector()
        collector.add_new_book('Книга Джунглей')
        collector.add_new_book('Робинзон Крузо')
        collector.add_book_in_favorites('Книга Джунглей')
        collector.add_book_in_favorites('Робинзон Крузо')
        assert len(collector.get_list_of_favorites_books()) == 2, f"Favorites list is not correct"








