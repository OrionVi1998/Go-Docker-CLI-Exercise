if __package__:
    from .parser import get_parser
    from .commands.count_movie_years import count_movies_years
    from .gateway import ApiGateway
    from .commands.search_movies import search_movies
else:
    from cli.parser import get_parser
    from cli.commands.count_movie_years import count_movies_years
    from cli.gateway import ApiGateway
    from tools.src.cli.commands.search_movies import search_movies


def main() -> None:
    parser = get_parser()
    args = parser.parse_args()
    api = ApiGateway(
        user=args.user,
        password=args.password,
        api_url=args.api_url,
        grace_period=args.grace_period,
    )

    if args.years and not args.search:
        res = count_movies_years(api, args.years)
        print(res)
    elif args.years and args.search:
        res = search_movies(api, args.years, args.count_only, args.search)
        print(res)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
