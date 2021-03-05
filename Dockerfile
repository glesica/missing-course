FROM pandoc/core

RUN apk update && apk add coreutils make

VOLUME [ "/code" ]
WORKDIR /code

ENTRYPOINT [ "make" ]

