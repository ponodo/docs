with Route.group(
        middleware=['auth'],
        prefix='books'
) as group:
    group.get('/', to='books@index')
