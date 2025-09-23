FROM golang:1.24.6 AS go_build
RUN git clone --branch v0.99 https://github.com/wtsi-hgi/movie-server /server
WORKDIR /server

#Fix make file
RUN sed -i "s|@|	@|g" ./Makefile

# Build + make the binary executable
RUN make build
RUN chmod +x movie-server


FROM python:3.12.3 AS cli

# Copy the requierments from the go_build container
COPY --from=go_build /server/movie-server /server/movie-server

# Copy CLI source and install
COPY tools/src tools/pyproject.toml ./cli/

WORKDIR /cli

RUN pip install -e .

# Add healthchek and run server
HEALTHCHECK --interval=5s --timeout=5s --retries=3 CMD curl localhost:8080;

CMD ["/server/movie-server"]
