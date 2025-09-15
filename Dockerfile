FROM golang:1.24.6 AS go_build
COPY . ./

#Fix make file
RUN sed -i "s|@|	@|g" ./Makefile

# Build + make the binary executable
RUN make build
RUN chmod +x movie-server


FROM python:3.12.3 AS cli

# Copy the requierments from the go_build container
COPY --from=go_build /go/movies.db /server/movies.db
COPY --from=go_build /go/movie-server /server/movie-server
COPY --from=go_build /go/version.go /server/version.go

# Copy CLI source and install
COPY tools/src ./cli/src
COPY tools/pyproject.toml ./cli/pyproject.toml

WORKDIR /cli

RUN pip install -e .

WORKDIR ../

# Add healthchek and run server
HEALTHCHECK --interval=5s --timeout=5s --retries=3 CMD curl localhost:8080;

CMD ["./server/movie-server"]
