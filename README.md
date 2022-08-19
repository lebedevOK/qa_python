# qa_python

# Проверка __init__ Проверяем каждое из полей books_rating и favorites что они не None
    def test_inits_elements_not_none(self)

# Проверка на повторное добавление имеющейся книги
    def test_add_new_book_possible_to_add_once(self)

# Проверка добавления книги и значения рейтинга по умолчанию = 1
    def test_add_new_book_default_rating(self)

# Проверка что у не добавленной книги нет рейтинга
    def test_get_book_rating_get_rating_for_an_unlisted_book(self)

# Проверка на установку рейтинга для книги, которой нет в списке
    def test_set_book_rating_set_rating_for_an_unlisted_book(self)

# Проверки установления значений рейтинга
    def test_set_book_rating_only_1_to_10(self)

# Проверка для списка книг с одинаковым рейтингом
    def test_get_books_with_specific_rating_for_books_with_the_same_rating(self)

# Проверка функции вывода текущего словаря
    def test_get_books_rating_for_four_books(self)

# Проверка функции добавления книги в избранное
# Невозможно дважды добавить одну книгу
    def test_add_book_in_favorites_cannot_be_added_twice(self)

# Проверка невозможности добавить в Избранное книги, отсутствующей в словаре
    def test_add_book_in_favorites_unable_to_add_missing_book(self)

# Проверка удадения книги из избранного
    def test_delete_book_from_favorites_remove_one_book_from_favorites(self)

# Проверка функции получения списка избранного
    def test_get_list_of_favorites_books_get_two_books(self)

