# form_schema_generator

## Requirements
- Python >= 3.7

- Django >= 3.1

- Django REST Framework (3.10, 3.11, 3.12)

### Add INSTALLED_APPS
```
INSTALLED_APPS = [
    ...other apps...
    
    'rest_framework',
    'drf_spectacular',
    'form_schema_generator'
]        
```

## settings.py drf-spectacular setting (base)
- 개발당시 사용하였던 옵션들입니다. swagger-ui 세팅 값은 원하시는 값으로 오버라이드 해서 사용하면 됩니다.
```
REST_FRAMEWORK = {
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10
}

SPECTACULAR_SETTINGS = {
    # General schema metadata. Refer to spec for valid inputs
    # https://github.com/OAI/OpenAPI-Specification/blob/master/versions/3.0.3.md#openapi-object
    'TITLE': 'drf-spectacular API Document',
    'DESCRIPTION': 'drf-specatular 를 사용해서 만든 API 문서입니다.',
    # Optional: MAY contain "name", "url", "email"
    'CONTACT': {'name': '임동욱', 'url': 'http://www.example.com/support', 'email': 'donguk.im@datamaker.io'},
    # Swagger UI를 좀더 편리하게 사용하기위해 기본옵션들을 수정한 값들입니다.
    'SWAGGER_UI_SETTINGS': {
        # https://swagger.io/docs/open-source-tools/swagger-ui/usage/configuration/  <- 여기 들어가면 어떤 옵션들이 더 있는지 알수있습니다.
        'dom_id': '#swagger-ui',  # required(default)
        'layout': 'BaseLayout',  # required(default)
        'deepLinking': True,  # API를 클릭할때 마다 SwaggerUI의 url이 변경됩니다. (특정 API url 공유시 유용하기때문에 True설정을 사용합니다)
        'persistAuthorization': True,  # True 이면 SwaggerUI상 Authorize에 입력된 정보가 새로고침을 하더라도 초기화되지 않습니다.
        'displayOperationId': True,  # True이면 API의 urlId 값을 노출합니다. 대체로 DRF api name둘과 일치하기때문에 api를 찾을때 유용합니다.
        'filter': True,  # True 이면 Swagger UI에서 'Filter by Tag' 검색이 가능합니다
    },
    # Optional: MUST contain "name", MAY contain URL
    'LICENSE': {
        'name': 'MIT License',
        'url': 'https://github.com/KimSoungRyoul/DjangoBackendProgramming/blob/main/LICENSE',
    },
    'VERSION': '1.0.0',
    'SERVE_INCLUDE_SCHEMA': False,  # OAS3 Meta정보 API를 비노출 처리합니다.

    # https://www.npmjs.com/package/swagger-ui-dist 해당 링크에서 최신버전을 확인후 취향에 따라 version을 수정해서 사용하세요.
    'SWAGGER_UI_DIST': '//unpkg.com/swagger-ui-dist@3.38.0',
    'COMPONENT_SPLIT_REQUEST': False
}
```

## urls.py
>Spectacular Document API url<br/>
> SpectacularSwaggerView 와 SpectacularRedocView 는 내부적으로 SpectacularAPIView를 호출한다.<br/>
> 그래서 .as_view(url_name= "SpectacularAPIView의 url_name") 형식으로 적어줘야 올바르게 작동한다



```
# API urls.py
app_name = 'api'

# Form_schema_generator
urlpatterns += [
    path('', include('form_schema_generator.urls')),
]

# Spectacular Document API
urlpatterns += [
    path("docs/json/", SpectacularJSONAPIView.as_view(), name="schema-json"),
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='api:schema'), name='swagger-ui'),
    path('schema/redoc/', SpectacularRedocView.as_view(url_name='api:schema'), name='redoc'),
]
```
<br/><br/><br/>
