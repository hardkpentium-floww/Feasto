import graphene

from feasto_gql.dummy import PublishBook, AuthorBooksResponse, AuthorBooksParams


class Query(graphene.ObjectType):
    get_author_books = graphene.Field(
        AuthorBooksResponse,
        params=AuthorBooksParams(required=True),
        required=True,
    )


class Mutation(graphene.ObjectType):
    publish_book = PublishBook.Field(required=True)


schema = graphene.Schema(query=Query, mutation=Mutation)
