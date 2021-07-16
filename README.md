# Docker SMTP Server

<p align="center"><img height="200" alt="rogervila/docker-smtp-server" src="https://i.ibb.co/bRcsvQp/fail.png" /></p>

<p align="center">
  <a href="https://hub.docker.com/r/rogervila/docker-smtp-server"><img alt="DockerHub Downloads" src="https://img.shields.io/docker/pulls/rogervila/docker-smtp-server.svg" /></a>
  <a href="https://github.com/rogervila/docker-smtp-server/blob/main/LICENSE"><img alt="GitHub license" src="https://img.shields.io/github/license/rogervila/docker-smtp-server" /></a>
</p>

## Setup

The image is available on DockerHub.

```sh
docker run -p 2525:25 rogervila/docker-smtp-server
```

## Simulate failures

If `SMTP_FAIL` environment variable is present, the SMTP server will return a error on every request, which is useful for debugging.

```yml
version: "3.8"

smtp:
    image: rogervila/docker-smtp-server:latest
    environment:
        - "SMTP_FAIL=1"
    ports:
        - "2525:25"
```

## License

This project is open-sourced software licensed under the [MIT license](https://opensource.org/licenses/MIT).


<div>Icons made by <a href="https://www.freepik.com" title="Freepik">Freepik</a> from <a href="https://www.flaticon.com/" title="Flaticon">www.flaticon.com</a></div>
