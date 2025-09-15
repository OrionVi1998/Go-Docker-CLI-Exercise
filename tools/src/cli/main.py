from .parser import get_parser
from .commands.count_movie_years import count_movies_years
from .gateway import ApiGateway


def main() -> None:
    parser = get_parser()
    args = parser.parse_args()
    if args.years:
        api = ApiGateway(
            user=args.user,
            password=args.password,
            api_url=args.api_url,
            grace_period=args.grace_period,
        )
        res = count_movies_years(api, args.years)
        print(res)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
