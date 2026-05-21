import argparse
import json
import users_wrapper as users


parser = argparse.ArgumentParser(
    description="CLI para CRUD de usuários"
)

subparsers = parser.add_subparsers(dest="command")


# LIST
subparsers.add_parser("list")


# READ
read_parser = subparsers.add_parser("read")
read_parser.add_argument("id", type=int)


# CREATE
create_parser = subparsers.add_parser("create")
create_parser.add_argument("--name", required=True)
create_parser.add_argument("--email", required=True)


# UPDATE
update_parser = subparsers.add_parser("update")
update_parser.add_argument("id", type=int)
update_parser.add_argument("--name")
update_parser.add_argument("--email")


# DELETE
delete_parser = subparsers.add_parser("delete")
delete_parser.add_argument("id", type=int)


args = parser.parse_args()


if args.command == "list":
    result = users.list()

elif args.command == "read":
    result = users.read(args.id)

elif args.command == "create":
    data = {
        "name": args.name,
        "email": args.email
    }
    result = users.create(data)

elif args.command == "update":
    data = {}

    if args.name:
        data["name"] = args.name

    if args.email:
        data["email"] = args.email

    result = users.update(args.id, data)

elif args.command == "delete":
    result = users.delete(args.id)

else:
    parser.print_help()
    exit()

print(json.dumps(result, indent=2, ensure_ascii=False))