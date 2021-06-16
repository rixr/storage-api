# Server interaction examples using curl

If you want to check the `CORS` response, you should populate the environment variable named `CORS_DOMAINS` with a value, let's say `http://localhost:1234`, then any request with that value in it's `ORIGIN` _HTTP Header_ should pass the `CORS` check politics in your browser.

You can go ahead and check the differences between a `cors` and `no-cors` request by executing the following command.

```

# This is a cors valid request
curl -vq http://localhost:8080/storage/json \
    -X OPTIONS \
    -H 'ORIGIN: http://localhost:1234' \
    2>&1 | grep '^<'

# This is a cors in valid request
curl -vq http://localhost:8080/storage/json \
    -X OPTIONS \
    -H 'ORIGIN: http://example.com' \
    2>&1 | grep '^<'
```
