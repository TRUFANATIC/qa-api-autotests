# Тест-кейсы REST API JSONPlaceholder

**Базовый URL:** `https://jsonplaceholder.typicode.com`  
**Тест-сьют (Suite):** `API Tests`  
**Уровень тестирования (Layer):** `API`  
**Статус автоматизации:** `Automated` (`Python + pytest + requests`)

---

## API-1. Получение существующего пользователя по валидному ID

| Поле | Значение |
| :--- | :--- |
| **ID** | API-1 |
| **Type** | Functional |
| **Behavior** | Positive |
| **Severity / Priority** | Major / High |
| **Automation status** | Automated |

**Предусловия (Pre-conditions):**
- Сервис JSONPlaceholder доступен.
- Пользователь с `id = 1` существует в системе.

| № | Шаг (Step action) | Тестовые данные (Data) | Ожидаемый результат (Expected result) |
| :--- | :--- | :--- | :--- |
| 1 | Отправить `GET`-запрос на эндпоинт `/users/1` | — | • HTTP-статус ответа: `200 OK`.<br>• В теле ответа (JSON) поле `id` равно `1`.<br>• В теле ответа поле `username` равно `"Bret"`. |

---

## API-2. Получение пользователя по несуществующему ID

| Поле | Значение |
| :--- | :--- |
| **ID** | API-2 |
| **Type** | Functional |
| **Behavior** | Negative |
| **Severity / Priority** | Normal / Medium |
| **Automation status** | Automated |

**Предусловия (Pre-conditions):**
- Сервис JSONPlaceholder доступен.
- Пользователь с `id = 99999` отсутствует в системе.

| № | Шаг (Step action) | Тестовые данные (Data) | Ожидаемый результат (Expected result) |
| :--- | :--- | :--- | :--- |
| 1 | Отправить `GET`-запрос на эндпоинт `/users/99999` | — | • HTTP-статус ответа: `404 Not Found`. |

---

## API-3. Создание нового поста с валидным JSON-телом

| Поле | Значение |
| :--- | :--- |
| **ID** | API-3 |
| **Type** | Functional |
| **Behavior** | Positive |
| **Severity / Priority** | Critical / High |
| **Automation status** | Automated |

**Предусловия (Pre-conditions):**
- Сервис JSONPlaceholder доступен.
- В системе существует пользователь с `userId = 1`.

| № | Шаг (Step action) | Тестовые данные (Data) | Ожидаемый результат (Expected result) |
| :--- | :--- | :--- | :--- |
| 1 | Отправить `POST`-запрос на эндпоинт `/posts` | `{"title": "QA Automation Post", "body": "Created by automated test", "userId": 1}` | • HTTP-статус ответа: `201 Created`.<br>• В теле ответа поле `title` равно `"QA Automation Post"`.<br>• В теле ответа присутствует присвоенный `id` созданного поста (используется в API-4). |

---

## API-4. Удаление созданного поста по ID

| Поле | Значение |
| :--- | :--- |
| **ID** | API-4 |
| **Type** | Functional |
| **Behavior** | Positive |
| **Severity / Priority** | Major / Medium |
| **Automation status** | Automated |

**Предусловия (Pre-conditions):**
- Сервис JSONPlaceholder доступен.
- Успешно выполнен `API-3`: пост создан и получен его `id`.

| № | Шаг (Step action) | Тестовые данные (Data) | Ожидаемый результат (Expected result) |
| :--- | :--- | :--- | :--- |
| 1 | Отправить `DELETE`-запрос на эндпоинт `/posts/{id}` | `id = {created_post_id}` | • HTTP-статус ответа: `200 OK`. |