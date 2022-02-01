#  api_final_yatube

В проекте api_yatube реализованы API для всех моделей приложения posts проекта Yatube. Yatube не весь, а только его бэкенд: приложения, модели. Исключен фронтенд и view-функции. Логика API вынесена в отдельное приложение api. В проекте используется аутентификация по JWT-токену. Аутентифицированный пользователь авторизован на изменение и удаление своего контента; в остальных случаях доступ предоставляется только для чтения.

Для взаимодействия с ресурсами настроены следующие эндпоинты:
- api/v1/jwt/create/ (POST): передаём логин и пароль, получаем "refresh" и "access" токены.
- api/v1/jwt/refresh/ (POST): поучаем обновленный JWT-токен.
- api/v1/jwt/verify/ (POST): проверяем обновленный JWT-токен.
- api/v1/posts/ (GET, POST): получаем список всех постов или создаём новый пост.
- api/v1/posts/{post_id}/ (GET, PUT, PATCH, DELETE): получаем, редактируем или удаляем пост по id.
- api/v1/groups/ (GET): получаем список всех групп.
- api/v1/groups/{group_id}/ (GET): получаем информацию о группе по id.
- api/v1/posts/{post_id}/comments/ (GET, POST): получаем список всех комментариев поста с id=post_id или создаём новый, указав id поста, который хотим прокомментировать.
- api/v1/posts/{post_id}/comments/{comment_id}/ (GET, PUT, PATCH, DELETE): получаем, редактируем или удаляем комментарий по id у поста с id=post_id.
- api/v1/follow/ (GET, POST): получаем список всех своих подписок или создаём новую, указав username пользователя, на которого хотим подписаться.



## Примеры запросов
Пример POST-запроса: добавление нового поста.

POST .../api/v1/posts/

```sh
{
    "text": "текст текст",
    "group": 1
} 
```

Пример ответа:

```sh
{
    "id": 14,
    "text": "текст текст",
    "author": "<author username>",
    "image": null,
    "group": 1,
    "pub_date": "2021-06-01T08:47:11.084589Z"
} 
```

Пример POST-запроса: отправляем новый комментарий к посту с id=14.

POST .../api/v1/posts/14/comments/

```sh
{
    "text": "текст текст"
} 
```

Пример ответа:

```sh
{
    "id": 4,
    "author": "<author username>",
    "post": 14,
    "text": "текст текст",
    "created": "2021-06-01T10:14:51.388932Z"
} 
```

Пример GET-запроса: получаем информацию о группе.

GET .../api/v1/groups/2/

Пример ответа:

```sh
{
    "id": 2,
    "title": "Математика",
    "slug": "math",
    "description": "Посты на тему математики"
}
```
 
Пример GET-запроса: получаем все подписки свои пользователя. Анонимные запросы запрещены.

GET .../api/v1/follow/

Пример ответа:

```sh
[
    {
        "user": "<self username>",
        "following": "<following username>"
    }
]
```
 
Пример POST-запроса: подписка на пользователя переданного в теле запроса. Анонимные запросы запрещены.

POST .../api/v1/follow/

```sh
{
    "following": "<following username>"
} 
```

Пример ответа:

```sh
{
    "user": "<self username>",
    "following": "<following username>"
}
```

Пример POST-запроса: получаем "refresh" и "access" токены.

POST ...api/v1/jwt/create/

```sh
{
    "username": "string",
    "password": "string"
}
```

Пример ответа:

```sh
{
    "refresh": "string",
    "access": "string"
}
```

Пример POST-запроса: поучаем обновленный JWT-токен.

POST ...api/v1/jwt/refresh/

```sh
{
    "refresh": "string"
}
```

Пример ответа:

```sh
{
    "access": "string"
}
```

Пример POST-запроса: проверяем обновленный JWT-токен.

POST ...api/v1/jwt/verify/

```sh
{
    "token": "string"
} 
```