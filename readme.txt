# 1. Zaktualizuj swojego pipa z plik requirements pip install -r requirements.txt
# 3. Stwórz bazę danych o nazwie video_store w sqoim sql
# 3. uzupełnij plik session.py donosnikiem do swojej bazy danych z aktualnym hasełm,
# rootem, local hostem
# 4. odpal skrypt create_tables.py
# 5. odpal skrypt fake_data.py (kolejność funkcji wywoływanych w funkcji main() ma znacznie,
# nie przstawiaj bo nie zadziała!)
# 6. Napisz do mnie jeśli coś będzie nie tak, lub będziesz miał/a pomysł,
# co mozna było zrobić inaczej w kwestii modeli(podkreślam, modeli!)
#6.1 dodam jeszcze tylko, że według mnie ten schemat z prezentacji jest spierdolony,
# to znaczy odzwzorowanie go identycznie tak samo sprawia, że to nie działa, tak na poziomie logiki, jak i nie da się teog odpalić,
#  albo prowadzi do absurdów (na przykład jeden customer może mieć tylko jedno wypozyczenie, a to bez sensu, wg mnie każdy wypożyczenie
#  może mieć tylko jednego klienta, ale jeden klient może mieć kilka wypozyczeń)
# 7. Fake_data wymaga paru poprawek i jestem tego świadom, pare danych jest przypisano
# na sztywno, jak na przykład każdy klient i obługiwacz zawsze jest active,
# ale nie chciało mi się już tracić na to więcej czasu :P