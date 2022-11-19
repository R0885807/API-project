# API-project

- Mijn hosted **API** link: **https://guitar-service-r0885807.cloud.okteto.net**
- Mijn hosted **front-end** link: **https://r0885807.github.io/api-project/**


## Beschrijving
Het thema van mijn API is gitaar. Ik speel al een aantal jaar zelf gitaar en ben heel geïntereseerd in verschillende soorten gitaren.
De front-end is gehost via **github pages**, **[Front-End](https://r0885807.github.io/api-project/)**. De back-end is gehost op **Okteto**, **[Back-End](https://guitar-service-r0885807.cloud.okteto.net)**. De container is opgesteld via **docker-compose**.

## Endpoints
### Get endpoint 1

Get endpoint 1: https://guitar-service-r0885807.cloud.okteto.net/guitars. Geeft een object terug met data over een willekeurige gitaar.

![Get "/guitars"](https://github.com/R0885807/api-project/blob/main/screenshots/Get%20guitars.png)
### Get endpoint 2

Get endpoint 2: https://guitar-service-r0885807.cloud.okteto.net/guitars/{guitar_id}. Geeft een object terug met data over de gitaar met als key guitar_id.

![Get "/guitars/{guitar_id}"](https://github.com/R0885807/api-project/blob/main/screenshots/Get%20guitars-guitarid.png)
### Post endpoint

Post endpoint: https://guitar-service-r0885807.cloud.okteto.net/guitars. Hiermee kan je een object posten naar de api.

![Get "/guitars/{guitar_id}"](https://github.com/R0885807/api-project/blob/main/screenshots/Post%20guitars.png)
### Put endpoint

Put endpoint: https://guitar-service-r0885807.cloud.okteto.net/guitars/{guitar_id}. Hiermee pas je een object aan met als key guitar_id.
