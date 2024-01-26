# UberServer 
To run the app 

```docker compose up --build ```

By default the server is running on the port 8083. To test the endpoints use swagger

``` http //localhost:8083/docs ```
Or curl commands for example
```
curl http://localhost:8083/v1/now
curl -u user1:111 http://localhost:8083/v1/VIP/1
```
Also it's possible to run the tests locally(view config.py)